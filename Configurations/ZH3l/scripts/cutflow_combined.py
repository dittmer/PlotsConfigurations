# This script will make a latex document with event count tables for the VH leptonic channels, using the datacards
# in /eos/user/l/lviliani/HWWRun2LegacyCombination/ . It relies on the common structure where datacards are organized
# by /eos/user/l/lviliani/HWWRun2LegacyCombination/<channel>/<year>/<cut>

import os
import scandir
import math
import fnmatch
import collections
from ROOT import *

def pretty(mystr):
  newstr = mystr.replace('_','\\_')
  return newstr

datacardDir = '/afs/cern.ch/work/d/dittmer/private/hww2018/hig-19-017/VHlep/'
channels = ['WH2l_SS','WH3l','ZH3l','ZH4l']
years = ['2016','2017','2018']

cuts_format = collections.OrderedDict()
cuts_format['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = '$e\mu$ 1j'
cuts_format['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = '$\mu\mu$ 1j'
cuts_format['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = '$e\mu$ 2j'
cuts_format['hww2l2v_13TeV_of2j_WH_SS_uu_2j'] = '$\mu\mu$ 2j'
cuts_format['wh3l_13TeV_ossf'] = 'OSSF'
cuts_format['wh3l_13TeV_sssf'] = 'SSSF'
cuts_format['wh3l_wz_13TeV']   = 'WZ'
cuts_format['wh3l_zg_13TeV']   = '$Z\gamma$'
cuts_format['zh3l_SR_1j']      = '1j SR'
cuts_format['zh3l_SR_2j']      = '2j SR'
cuts_format['zh3l_WZ_CR_1j']   = '1j WZ CR'
cuts_format['zh3l_WZ_CR_2j']   = '2j WZ CR'
cuts_format['zh4l_XDF_13TeV']  = 'XDF'
cuts_format['zh4l_XSF_13TeV']  = 'XSF'
cuts_format['zh4l_ZZ_13TeV']   = 'ZZ'

signals_format = collections.OrderedDict()
signals_format['ggH_hww']  = 'ggH(H$\\rightarrow W^{+}W^{-}$)'
signals_format['qqH_hww']  = 'qqH(H$\\rightarrow W^{+}W^{-}$)'
signals_format['WH_hww']   = 'WH(H$\\rightarrow W^{+}W^{-}$)'
signals_format['ZH_hww']   = 'ZH(H$\\rightarrow W^{+}W^{-}$)'
signals_format['ggZH_hww'] = 'ggZH(H$\\rightarrow W^{+}W^{-}$)'
signals_format['ttH_hww']  = 'ttH(H$\\rightarrow W^{+}W^{-}$)'
signals_format['ggH_htt']  = 'ggH(H$\\rightarrow \\tau^{+}\\tau^{-}$)'
signals_format['qqH_htt']  = 'qqH(H$\\rightarrow \\tau^{+}\\tau^{-}$)'
signals_format['WH_htt']   = 'WH(H$\\rightarrow \\tau^{+}\\tau^{-}$)'
signals_format['ZH_htt']   = 'ZH(H$\\rightarrow \\tau^{+}\\tau^{-}$)'
signals_format['H_htt']    = 'H(H$\\rightarrow \\tau^{+}\\tau^{-}$)'

backgrounds_format = collections.OrderedDict()
backgrounds_format['DY']      = 'Z+jets'
backgrounds_format['Wg']      = '$W\gamma$'
backgrounds_format['WgS']     = '$W\gamma^{*}$'
backgrounds_format['Zg']      = '$Z\gamma$'
backgrounds_format['ZgS']     = '$Z\gamma^{*}$'
backgrounds_format['WW']      = 'WW'
backgrounds_format['WWewk']   = 'WWewk'
backgrounds_format['ggWW']    = 'ggWW'
backgrounds_format['WZ']      = 'WZ'
backgrounds_format['WZhad']   = 'WZ had'
backgrounds_format['ZZ']      = 'ZZ'
backgrounds_format['ZZhad']   = 'ZZ had'
backgrounds_format['ggZZ']    = 'ggZZ'
backgrounds_format['WWW']     = 'WWW'
backgrounds_format['VVV']     = 'VVV'
backgrounds_format['top']     = 'Top'
backgrounds_format['ttW']     = 'ttW'
backgrounds_format['ttZ']     = 'ttZ'
backgrounds_format['ttV']     = 'ttV'
backgrounds_format['Fake']    = 'Fake'
backgrounds_format['Fake_e']  = 'Fake e'
backgrounds_format['Fake_m']  = 'Fake m'
backgrounds_format['Fake_em'] = 'Fake em'
backgrounds_format['Fake_mm'] = 'Fake mm'

#Print document header
print '\\documentclass[12pt]{amsart}'
print '\\usepackage{geometry}'
print '\\geometry{a4paper}\n'
print '\\begin{document}\n'

for channel in channels:
  table = {}
  for year in years : 
    table[year] = {}
  bindirs = [f.path for f in scandir.scandir(datacardDir+channel+'/2016/') if f.is_dir()] #Assume same cuts in all years
  cuts = [bindir.rsplit('/',1)[1] for bindir in bindirs]
  for cut in cuts:
    for year in years:
      table[year][cut] = {}
      rootfile = ''
      for basedir, dirnames, filenames in os.walk(datacardDir+channel+'/'+year+'/'+cut): #Recursively search through directory
        filenames = fnmatch.filter(filenames, '*.root')
        if len(filenames) > 0:
          rootfile = os.path.join(basedir, filenames[0]) #Just use the first rootfile you find    
          continue
      if rootfile is not '': #We found a rootfile
        f0 = TFile.Open(rootfile)
        for histkey in f0.GetListOfKeys():
          histname = histkey.GetName()
          if not any(var in histname for var in ['Up','Down','Var']): #Want nominal histogram, not systematic
            sample = histname.replace('histo_','')
            if sample != 'Data': #Blinded tables
              hist = f0.Get(histname)
              err = Double()
              count = hist.IntegralAndError(0,hist.GetNbinsX()+1,err) #Normalization and stat error
              table[year][cut][sample] = [count,err]
            
  #Combine years
  table['Comb'] = {}
  for cut in table['2016']:
    table['Comb'][cut] = {}
    allsamples = list(set(table['2016'][cut].keys()+table['2017'][cut].keys()+table['2018'][cut].keys()))
    for sample in allsamples:
      count = sum(table[year][cut][sample][0] if sample in table[year][cut] else 0.0 for year in years)
      err = sum(table[year][cut][sample][1]**2 if sample in table[year][cut] else 0.0 for year in years)
      err = math.sqrt(err)
      table['Comb'][cut][sample] = [count,err]

  #Pretty print everything
  for year in ['2016','2017','2018','Comb']:
    print 'Event counts in '+pretty(channel)+' '+year+'\n'
    lines = {}    
    header = '        '
    cuts_unsorted = table[year].keys()
    cuts_ordered = cuts_format.keys()
    cuts_sorted = sorted(set(cuts_ordered).intersection(cuts_unsorted), key=lambda x:cuts_ordered.index(x))
    for cut in cuts_sorted:
      header += ' & '+cuts_format[cut]
      for sample in table[year][cut]:
        if sample in lines:
          lines[sample] += ' & %.1f $\\pm$ %.1f'%(table[year][cut][sample][0],table[year][cut][sample][1])
        else:
          lines[sample] =  ' & %.1f $\\pm$ %.1f'%(table[year][cut][sample][0],table[year][cut][sample][1])

    #Sort samples using hardcoded order
    signals_ordered = signals_format.keys()
    backgrounds_ordered = backgrounds_format.keys()
    signals = sorted(set(signals_ordered).intersection(lines.keys()), key=lambda x:signals_ordered.index(x))
    backgrounds = sorted(set(backgrounds_ordered).intersection(lines.keys()), key=lambda x:backgrounds_ordered.index(x))
    if len(signals)+len(backgrounds) != len(lines.keys()):
      print 'Error! Missing sample(s)'
      print set(lines.keys()).difference(signals+backgrounds)

    #Get signal and background sums

    #Finally, actually print table
    print '\\begin{table*}[htbp]'
    print '\\begin{center}'
    print '\\begin{tabular}{l|'+'c|'*len(table[year].keys())+'}'
    print '\\hline'
    print pretty(header)+'  \\\\'
    print '\\hline'
    for sample in signals:
      print pretty(signals_format[sample]).ljust(10)+lines[sample]+'  \\\\'
    print '\\hline'
    for sample in backgrounds:
      print pretty(backgrounds_format[sample]).ljust(10)+lines[sample]+'  \\\\'
    print '\\hline'
    print '\\end{tabular}'
    print '\\end{center}'
    print '\\end{table*}\n'

print '\\end{document}'
