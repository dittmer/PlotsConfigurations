from ROOT import TFile, TH1D, TObject
import fnmatch
import os

norms = {
    'Full2016nanov6': {'Down': 1.037, 'Up': 0.961}, 
    'Full2017nanov6': {'Down': 1.036, 'Up': 0.962}, 
    'Full2018nanov6': {'Down': 1.036, 'Up': 0.962}
}

for root, dirnames, filenames in os.walk('.',followlinks=True):
    if root.endswith('shapes'):
        filepath = os.path.join(root,filenames[0])
        f0 = TFile.Open(filepath,"UPDATE")
        key = root.split('/')[1]
        for var in norms[key]:
            try:
                hist = f0.Get("histo_WZ_QCDscale_VV"+var)
                hist.Scale(norms[key][var])
            except:
                print "Couldn't find histo_WZ_QCDscale_VV"+var
        f0.Write("",TObject.kOverwrite)


