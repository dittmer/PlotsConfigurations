import os
import sys
from ROOT import *

#root = root directory, dirnames = list of subdirectories in root directory, filenames = list of files in root directory
# In our case, we are looking for the rootfiles in shapes/, so we can check that root ends with shapes/
for root, dirnames, filenames in os.walk('STXS_nanoAOD/v7',followlinks=True):
    if root.endswith('shapes'):
        if 'sigFix' not in root: continue
        histfile = root+'/'+filenames[0]
        f0 = TFile.Open(histfile,"UPDATE")
        allhists = [key.GetName() for key in f0.GetListOfKeys()]
        nomhists = [hist for hist in allhists if not ('Up' in hist or 'Down' in hist or 'Var' in hist)]
        varhists = [hist for hist in allhists if not hist in nomhists]
        
        for nomhist in nomhists:
            nom = f0.Get(nomhist)
            for varhist in varhists:
                if not varhist.replace(nomhist,'').startswith('_'): continue
                var = f0.Get(varhist)
                if var.Integral() < 0.0: continue #Will drop this nuisance regardless
                for ibin in xrange(1,nom.GetNbinsX()+1):
                    if nom.GetBinContent(ibin) > 0 and var.GetBinContent(ibin) < 0:
                        print '%s: Setting bin %d of %s to 0 (was %.3f)'%(histfile,ibin,varhist,var.GetBinContent(ibin))
                        var.SetBinContent(ibin,0.00001)

        f0.Write("",TObject.kOverwrite)
