import os
import sys
from ROOT import *

histfile = sys.argv[1]

if len(sys.argv) < 2:
    print 'Usage: pruneSamples.py <rootfile>'
    exit()

samples_to_cut = {}

f0 = TFile.Open(histfile)
for cutkey in f0.GetListOfKeys():
    cutname = cutkey.GetName()
    cutdir = f0.Get(cutname)
    shape = 'events'
    if 'SR_1j' in cutname:
        shape = 'mTlmetj'
    if 'SR_2j' in cutname:
        shape = 'mTlmetjj'
    histdir = cutdir.Get(shape)
    allhists = [key.GetName() for key in histdir.GetListOfKeys()]
    nomhists = [hist for hist in allhists if not ('Up' in hist or 'Down' in hist or 'Var' in hist)]
    varhists = [hist for hist in allhists if not hist in nomhists]
    for nomhist in nomhists:
        nom = histdir.Get(nomhist)
        sample = nomhist.replace('histo_','')
        if 'H_hww' in sample or 'H_htt' in sample: continue
        if nom.Integral() <= 0.0:
            if sample in samples_to_cut:
                samples_to_cut[sample].append(cutname)
            else:
                samples_to_cut[sample] = [cutname]
            continue
        for varhist in varhists:
            if not varhist.replace(nomhist,'').startswith('_'): continue
            var = histdir.Get(varhist)
            if var.Integral() < 0.0:
                print 'nuisance edit drop %s %s %s'%(sample,cutname,varhist.replace(nomhist+'_','').replace('Up','').replace('Down',''))

for sample in samples_to_cut:
    print "structure['"+sample+"']['removeFromCuts'] = ['"+"','".join(samples_to_cut[sample])+"']"
