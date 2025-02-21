import sys
import re
import os
import fnmatch
from ROOT import TFile, TCanvas, gStyle, gROOT

gROOT.SetBatch(True)

for root, dirnames, filenames in os.walk('.',followlinks=True):
    if 'datacard.txt.pruned.txt' in filenames:
        if 'sigFix' not in root: continue
        bla0,ydir,bla1,cut,shape = root.split('/')
        filename = root+'/datacard.txt.pruned.txt'
        print filename
'''
        with open(filename,'r') as infile:
            lines = infile.readlines()

        table = {}

        samplelist = []
        shapefile = ''
        for line in lines:
            splitline = line.split()
            if len(splitline) == 0 : continue #skip if empty
            if splitline[0] == 'shapes': shapefile = splitline[3]
            if splitline[0] == 'process' : 
                samplelist = splitline[1:]
                break

        shapefilepath = '%s/%s'%(root,shapefile)
        year = ydir.rstrip('nano_STXS_1p1').lstrip('Full')

        f0 = TFile.Open(shapefilepath)
        gStyle.SetOptStat(0)
        c = TCanvas("c","c",900,700)
        idx_to_remove = []
        for i,sample in enumerate(samplelist):
            hist = f0.Get("histo_"+sample)
            if hist.Integral() < 0:
                idx_to_remove.append(i)
                continue
            lowstat = True
            for ibin in xrange(1,hist.GetNbinsX()+1):
                if abs(hist.GetBinContent(ibin)) > abs(hist.GetBinError(ibin)) : lowstat = False
            if lowstat:
                #if hist.Integral() != 0:
                #    hist.Draw("ep1")
                #    c.SaveAs("lowStat/"+cut+"_"+year+"_"+shape+"_"+sample+".pdf")
                idx_to_remove.append(i)

        print 'Removing '+', '.join([samplelist[i] for i in idx_to_remove])+' for %s/%s/%s'%(year,cut,shape)

        lines_out = []
        systime = False
        for line in lines:
            splitline = line.split()
            if len(splitline) > len(samplelist):
                spaces = re.findall('\s+',line)
                if systime:
                    parts = splitline[2:]
                    newline = splitline[0]+spaces[0]+splitline[1]+spaces[1]+('').join([part+spaces[i+2] for i,part in enumerate(parts) if not i in idx_to_remove])+'\n'
                    if all([var == '-' for var in newline.split()[2:]]):
                        print 'Dropping %s for %s/%s/%s'%(splitline[0],year,cut,shape)
                    else:
                        lines_out.append(newline)
                else:
                    parts = splitline[1:]
                    newline = splitline[0]+spaces[0]+('').join([part+spaces[i+1] for i,part in enumerate(parts) if not i in idx_to_remove])+'\n'
                    lines_out.append(newline)
                if splitline[0] == 'rate': systime = True
            elif len(splitline) == 5 and splitline[1] == 'rateParam' and any([splitline[3] == samplelist[i] for i in idx_to_remove]):
                pass
            else:
                lines_out.append(line)

        outfile = open(filename,'w')

        for line in lines_out :
            outfile.write(line)

'''
