import os
import sys
from ROOT import *

histfile = sys.argv[1]

if len(sys.argv) < 2:
    print 'Usage: checkSTXS.py <rootfile>'
    exit()

#ZH3l
#srcuts = ['zh3l_SR_1j_ptv_lt150','zh3l_SR_1j_ptv_gt150','zh3l_SR_2j_ptv_lt150','zh3l_SR_2j_ptv_gt150']
#samples = ['WH_hww','ZH_hww','ggZH_hww','ttH_hww','WH_htt','ZH_htt']
#ZH4l
srcuts = ['zh4l_XSF_13TeV_ptv_lt150','zh4l_XSF_13TeV_ptv_gt150','zh4l_XDF_13TeV_ptv_lt150','zh4l_XDF_13TeV_ptv_gt150']
samples = ['ZH_hww','ggZH_hww','ZH_htt']
status = dict((sample,dict((cut,{}) for cut in srcuts)) for sample in samples)

f0 = TFile.Open(histfile)
for srcut in srcuts:
    cutdir = f0.Get(srcut)
    if 'XSF' in srcut:
        shape = 'class0_XSF'
    else:
        shape = 'class1_XDF'
    histdir = cutdir.Get(shape)
    allhists = [key.GetName() for key in histdir.GetListOfKeys()]
    nomhists = [hist for hist in allhists if not ('Up' in hist or 'Down' in hist or 'Var' in hist)]
    sighists = [hist for hist in nomhists if any([sample in hist for sample in samples])]
    for sighist in sighists:
        hist = histdir.Get(sighist)
        parts = sighist.split('_')
        sample, STXS_bin = '_'.join(parts[1:3]), '_'.join(parts[3:])
        if hist.Integral() == 0.0:
            status[sample][srcut][STXS_bin] = 0 #empty
        else:
            lowstat = True
            for ibin in xrange(1,hist.GetNbinsX()+1):
                if abs(hist.GetBinContent(ibin)) > abs(hist.GetBinError(ibin)) : lowstat = False
            if lowstat:
                status[sample][srcut][STXS_bin] = 1 #low stat hist
            else:
                status[sample][srcut][STXS_bin] = 2 #ok

stringmap = ["empty", "lstat", "ok   "]

for sample in status.keys():
    print(sample)
    STXS_bins = status[sample].values()[0]
    for STXS_bin in STXS_bins:
        if sum([status[sample][cut][STXS_bin] for cut in srcuts]) == 0:
            print (STXS_bin.ljust(45)+": all empty")
        else:
            print (STXS_bin.ljust(45)+": "+" ".join(["{} : {}".format(cut,stringmap[status[sample][cut][STXS_bin]]) for cut in srcuts]))

