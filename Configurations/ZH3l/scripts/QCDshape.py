from ROOT import TFile, TH1, TCanvas, TPad, gROOT, TLegend, gStyle
import collections

TH1.AddDirectory(0)
gROOT.SetBatch(True)
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

c = TCanvas("c","c",900,700)
p1 = TPad("p1","p1",0,0.3,1,1)
p2 = TPad("p2","p2",0,0,1,0.3)
p1.Draw()
p2.Draw()

files = {#'2016' : 'Full2016_v7/rootFiles_ZH3l_2016_v7/plots_ZH3l_2016_v7.root',
         '2017' : 'Full2017_v7/rootFiles_ZH3l_2017_v7/plots_ZH3l_2017_v7.root',
         '2018' : 'Full2018_v7/rootFiles_ZH3l_2018_v7/plots_ZH3l_2018_v7.root'
}

colors = [2,4,5,6,7,8]
names = ['#muR=0.5, #muF=0.5','#muR=0.5, #muF=1.0','#muR=1.0, #muF=0.5','#muR=1.0, #muF=2.0','#muR=2.0, #muF=1.0','#muR=2.0, #muF=2.0']

def allVars(year,cut,sample):
    dist = 'mTlmetjj' if '2j' in cut else 'mTlmetj'
    f0 = TFile(files[year])
    hnom = f0.Get("%s/%s/histo_%s"%(cut,dist,sample))
    hnom.SetLineWidth(2)
    hnom.GetXaxis().SetTitle("mTlmetj(j)")
    p1.cd()
    hnom.Draw("hist")
    leg = TLegend(0.6,0.6,0.9,0.9)
    leg.AddEntry(hnom,"Nominal","l")
    rvar = []
    for ivar in xrange(0,6):
        hvar = f0.Get('%s/%s/histo_%s_QCDscale_VVV%dVar'%(cut,dist,sample,ivar))
        hvar.SetLineWidth(2)
        hvar.SetLineColor(colors[ivar])
        leg.AddEntry(hvar,names[ivar]+" (%.2f)"%(hvar.Integral()/hnom.Integral()),"l")
        rtmp = hvar.Clone()
        rtmp.Divide(hnom)
        rvar.append(rtmp)
        hvar.Draw("hist,same")
    leg.Draw()        
    p2.cd()
    rvar[0].GetYaxis().SetRangeUser(0.9,1.1)
    rvar[0].GetYaxis().SetNdivisions(2,5,1)
    rvar[0].GetYaxis().SetLabelSize(0.08)
    rvar[0].GetXaxis().SetLabelSize(0.08)
    rvar[0].Draw("hist")
    for ivar in xrange(1,6):
        rvar[ivar].Draw("hist,same")
    c.SaveAs("plots/%s/compareAllVarsQCDscale_VV_%s_%s.png"%(year,cut,sample))


for year in files.keys():
    for cut in ['zh3l_SR_1j','zh3l_SR_2j']:
        for sample in ['WZ','ZZ']:
            allVars(year,cut,sample)
            allVars(year,cut,sample)
            allVars(year,cut,sample)
