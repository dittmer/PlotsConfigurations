import argparse

'''
The script adds up/down shapes equal to nominals in all cuts and vars of the inputfile
if they do not exists.
'''
parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", help="Input file", type=str)
parser.add_argument("--nuisances", help="Nuisances", type=str, nargs="+")
args = parser.parse_args()


samples= ['VBS','DY','top','VV','VVV','Vg','VgS', 'VBF-V']
wjets_bins = []
for ir in range(1,7):
    wjets_bins.append("Wjets_HT_res_"+str(ir))
for ir in range(1,6):
    wjets_bins.append("Wjets_HT_boost_"+str(ir))
samples += wjets_bins

import ROOT as R

iF = R.TFile.Open(args.input, "UPDATE")


for cut in iF.GetListOfKeys():
    R.gDirectory.cd(cut.GetName())
    for var in R.gDirectory.GetListOfKeys():
        R.gDirectory.cd(var.GetName())
        for sample in samples:
            hnom = R.gDirectory.Get("histo_{}".format(sample))
            for nuis in args.nuisances:
                print cut, var, sample, nuis
                try:
                    R.gDirectory.GetObject("histo_{}_{}Up".format(sample, nuis),hnom )
                    print ">>> shape already exists"
                except LookupError:
                    hup = hnom.Clone("histo_{}_{}Up".format(sample, nuis))
                    hup.SetTitle("histo_{}_{}Up".format(sample, nuis))
                    hdo = hup.Clone("histo_{}_{}Down".format(sample, nuis))
                    hdo.SetTitle("histo_{}_{}Down".format(sample, nuis))
                    iF.cd("{}/{}".format(cut.GetName(), var.GetName()))
                    hup.Write()
                    hdo.Write()
        R.gDirectory.cd("../")
    iF.cd()
iF.Close()
