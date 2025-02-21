import os
from ROOT import *
import collections
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("rootfile", help="file path")
args = parser.parse_args()

fittemplate = 'BDT'

gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
gROOT.SetBatch(1)

samples = collections.OrderedDict()
with open('samples.py', 'r') as f:
  exec(f)

signals = ['ZH_hww','ggZH_hww']
backgrounds = [s for s in samples if s not in signals and s is not 'DATA']
append = []
for background in backgrounds:
  if samples[background].has_key('subsamples'):
    backgrounds.remove(background)
    for sub in samples[background]['subsamples']:
      append.append(background+'_'+sub)
backgrounds.extend(append)

#true_bins = ['PTV_0_75','PTV_75_150','PTV_150_250_0J','PTV_150_250_GE1J','PTV_GT250']
true_bins = ['PTV_LT150','PTV_GT150']

cuts = collections.OrderedDict()
with open('cuts.py', 'r') as f:
  exec(f)

all_cuts = []
for cut in cuts:
  if isinstance(cuts[cut],dict) and cuts[cut].has_key('categories'):
    all_cuts.extend(cut+'_'+cat for cat in cuts[cut]['categories'])
  else:
    all_cuts.append(cut)
all_cuts.sort()

reco_bins = []
for tbin in true_bins:
  for ibin in all_cuts:
    if re.search(tbin, ibin, re.IGNORECASE):
      reco_bins.append(ibin)

f0 = TFile.Open(args.rootfile)

c = TCanvas("c","c",900,700)
c.SetLeftMargin(0.18)
c.SetBottomMargin(0.25)
c.SetTopMargin(0.05)

for sample in signals:
  response = TH2F('response_'+sample,'response_'+sample,len(true_bins),0,len(true_bins),len(reco_bins),0,len(reco_bins))
  for rbin in reco_bins:
    for tbin in true_bins:
      tmp = f0.Get(rbin+'/events/histo_'+sample+'_'+tbin).GetEntries()
      response.Fill(rbin,tbin,tmp)
  response.LabelsDeflate("X")
  response.LabelsDeflate("Y")
  response.LabelsOption("v")
  response.Draw("text,colz")
  c.SaveAs("response_"+sample+".pdf")

print 'MC event counts for backgrounds'
print ", ".join(backgrounds)
for rbin in reco_bins:
  print rbin+', '+', '.join(["%.1f"%(f0.Get(rbin+'/events/histo_'+background).GetEntries()) for background in backgrounds])
print

print 'Normalized counts'
printline = ''
bkg_to_remove = {}
print " & ".join(backgrounds)+' & '+' & '.join(signals)
for cut in all_cuts:
  printline = cut
  for background in backgrounds:
    printline += ' & %.1f'%(f0.Get(cut+'/events/histo_'+background).Integral())
    if f0.Get(cut+'/events/histo_'+background).Integral() < 0.0:
      if cut not in bkg_to_remove.keys():
        bkg_to_remove[cut] = [background]
      else:
        bkg_to_remove[cut].append(background)
  for signal in signals:
    sigtot = 0.0
    for ib in true_bins:
      sigtot += f0.Get(cut+'/events/histo_'+signal+'_'+ib).Integral()
    printline += ' & %.1f'%(sigtot)
  print printline
print

print 'Remove following backgrounds: '
print bkg_to_remove
print

for cut in f0.GetListOfKeys():
  cutdir = f0.Get(cut.GetName())
  countdir = cutdir.Get("events") if 'CR' in cut.GetName() else cutdir.Get(fittemplate)
  for histname in countdir.GetListOfKeys():
    if cut.GetName() in bkg_to_remove.keys() and any(bkg in histname.GetName() for bkg in bkg_to_remove[cut.GetName()]):
      continue
    hist = countdir.Get(histname.GetName())
    if hist.GetEntries() is 0:
      print 'WARNING: empty histogram %s in %s/events' % (hist.GetName(),cut.GetName())
    if hist.Integral() < 0.0:
      print 'ERROR: histogram %s in %s/events has negative integral (%d)' % (hist.GetName(),cut.GetName(),hist.Integral())
      
