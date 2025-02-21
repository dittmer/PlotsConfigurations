import os
import sys
from ROOT import *

gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
gROOT.SetBatch(True)

sample = 'DY'
years = ['2016','2017','2018']
cuts = ['zh3l_SR_1j','zh3l_SR_2j']

nUnc = 5
colors = [2,3,4,6,7]

c = TCanvas("c","c",900,900)
p1 = TPad("p1","p1",0.0,0.2,1.0,1.0)
p2 = TPad("p2","p2",0.0,0.0,1.0,0.2)
p1.Draw()
p2.Draw()

for year in years:
    inputFile = 'Full%s_v6/rootFiles_ZH3l_%s_v6_freeze/plots_ZH3l_%s_v6_freeze.root'%(year,year,year)
    f0 = TFile.Open(inputFile)
    for cut in cuts:
        fitvar = "mTlmetj" if '1j' in cut else "mTlmetjj"
        nom = f0.Get(cut+"/"+fitvar+"/histo_"+sample)
#        nom.Rebin(2)
        nom.Scale(1.0/nom.Integral())

        def diffscore(unc):
            histup = f0.Get(cut+"/"+fitvar+"/histo_"+sample+"_"+unc+"Up").Clone()
#            histup.Rebin(2)
            histup.Scale(1.0/histup.Integral())
            histup.Add(nom,-1.0)
            histup.Divide(nom)
            upscore = sum([abs(histup.GetBinContent(ibin)) for ibin in xrange(1,histup.GetNbinsX()+1)])
            histdown = f0.Get(cut+"/"+fitvar+"/histo_"+sample+"_"+unc+"Down").Clone()
#            histdown.Rebin(2)
            histdown.Scale(1.0/histdown.Integral())
            histdown.Add(nom,-1.0)
            histdown.Divide(nom)
            downscore = sum([abs(histdown.GetBinContent(ibin)) for ibin in xrange(1,histdown.GetNbinsX()+1)])
            return max([upscore,downscore])
        
        histdir = f0.Get(cut+"/"+fitvar)
        allhists = [key.GetName() for key in histdir.GetListOfKeys()]
        alluncs = [hist.split(sample+'_')[1].replace('Up','') for hist in allhists if sample in hist and 'Up' in hist]
        alluncs = list(set(alluncs))

        alluncs = [unc for unc in alluncs if 'CMS_scale' in unc]

        alluncs.sort(key=diffscore,reverse=True)
        
        nom.SetLineWidth(2)
        nom.SetLineColor(1)

        varhists = {}
        ratiohists = {}
        for iunc in range(nUnc):
            for var in ["Up","Down"]:
                tmphist = f0.Get(cut+"/"+fitvar+"/histo_"+sample+"_"+alluncs[iunc]+var).Clone()
#                tmphist.Rebin(2)
                tmphist.Scale(1.0/tmphist.Integral())
                tmphist.SetLineWidth(2)
                tmphist.SetLineColor(colors[iunc])
                if var == "Down" : tmphist.SetLineStyle(2)
                varhists[alluncs[iunc]+var] = tmphist
                tmpratio = tmphist.Clone()
                tmpratio.Divide(nom)
                ratiohists[alluncs[iunc]+var] = tmpratio

        p1.cd()
        nom.Draw("ep1")
        for iunc in range(nUnc):
            varhists[alluncs[iunc]+"Up"].Draw("hist,same")
            varhists[alluncs[iunc]+"Down"].Draw("hist,same")

        leg = TLegend(0.55,0.6,0.9,0.9)
        leg.AddEntry(nom,"Nominal shape","l")
        for iunc in range(nUnc):
            leg.AddEntry(varhists[alluncs[iunc]+"Up"],alluncs[iunc],"l")
        leg.Draw()

        p2.cd()
        one = nom.Clone()
        one.Divide(nom)
        one.GetYaxis().SetRangeUser(0.9,1.1)
        one.GetXaxis().SetLabelFont(63)
        one.GetXaxis().SetLabelSize(18)
        one.GetYaxis().SetLabelFont(63)
        one.GetYaxis().SetLabelSize(18)
        one.GetYaxis().SetNdivisions(2,4,0)
        one.Draw("ep1")
        
        for iunc in range(nUnc):
            ratiohists[alluncs[iunc]+"Up"].Draw("hist,same")
            ratiohists[alluncs[iunc]+"Down"].Draw("hist,same")

        outname = "compare"+sample+"scale_"+cut+"_"+year+".pdf"
        c.SaveAs(outname)
