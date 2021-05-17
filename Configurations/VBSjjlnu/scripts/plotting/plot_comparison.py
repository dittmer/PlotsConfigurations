import sys
from math import sqrt
import pandas as pd 
import canvas_utils
import argparse
import CMS_lumi
import numpy as np
import root_numpy as rnp

''' 
This script plots the closure test prefit factors for W+jets
'''

parser = argparse.ArgumentParser()
parser.add_argument("-i","--input", type=str)
parser.add_argument("-o","--output", type=str)
parser.add_argument("-l","--label", type=str)
parser.add_argument("--samples", type=str, nargs=2)
parser.add_argument("-v","--vars", type=str, nargs="+")
parser.add_argument("--yratio", type=float, nargs="+",default=[0.5,1.5])
args = parser.parse_args()

import ROOT as R 
# R.gStyle.SetPalette(R.kLightTemperature)
R.gROOT.SetBatch(True)
import LatinoAnalysis.ShapeAnalysis.tdrStyle as tdrStyle
tdrStyle.setTDRStyle()

iF = R.TFile.Open(args.input)


def Pad2TAxis(hist):
    xaxis = hist.GetXaxis()
    xaxis.SetLabelFont ( 42)
    xaxis.SetLabelOffset( 0.025)
    xaxis.SetLabelSize ( 0.1)
    xaxis.SetNdivisions ( 505)
    xaxis.SetTitleFont ( 42)
    xaxis.SetTitleOffset( 1.35)   
    xaxis.SetTitleSize ( 0.11)

    yaxis = hist.GetYaxis()
    yaxis.CenterTitle ( )
    yaxis.SetLabelFont ( 42)
    yaxis.SetLabelOffset( 0.02)
    yaxis.SetLabelSize ( 0.1)
    yaxis.SetNdivisions ( 505)
    yaxis.SetTitleFont ( 42)
    yaxis.SetTitleOffset( .6)
    yaxis.SetTitleSize ( 0.11)

cache = []

colors = [ R.TColor.GetColor(128, 215, 255),  R.TColor.GetColor(242, 108, 13)] #R.TColor.GetColor(72, 145, 234) 158, 218, 255


for var in args.vars:
    hs = [] 
    hs_name = []
    errs = []
    maxH = -1
    minH = 10 

    for sample in args.samples:
        h = iF.Get("{}_{}".format(sample, var))
        hs.append(h)

    print(hs)


    for h in hs:
        if h.GetMaximum() > maxH : maxH = h.GetMaximum()
        if h.GetMinimum() < minH : minH = h.GetMinimum()
        
    tcanvasRatio = R.TCanvas("c","c", 800,800) 

    hs[0].SetTitle(";{};Events".format(var))
    hs[0].GetYaxis().SetRangeUser(minH*0.8, maxH*1.3)
    hs[0].SetLineColor(colors[0])
    hs[0].SetLineWidth(4)
    hs[0].SetFillStyle(3001)
    hs[0].SetFillColor(colors[0])
    hs[1].SetLineColor(colors[1])
    hs[1].SetLineWidth(3)

    n_cr = rnp.hist2array( hs[0], copy=False)
    n_sig = rnp.hist2array( hs[1], copy=False)
    tgrRatio = R.TGraphErrors()

    for iBin in range(0, len(n_cr)) :
        tgrRatio.SetPoint(iBin, hs[0].GetBinCenter(iBin+1), n_sig[iBin]/ n_cr[iBin])
        tgrRatio.SetPointError(iBin, hs[0].GetBinWidth(iBin+1)/2., 0.)


    tlegend = R.TLegend(0.20, 0.65, 0.45, 0.88)
    tlegend.SetFillColor(0)
    tlegend.SetTextFont(42)
    tlegend.SetTextSize(0.036)
    tlegend.SetLineColor(0)
    tlegend.SetShadowColor(0)
    tlegend.AddEntry(hs[0], args.samples[0] + " [{:.2f}]".format(hs[0].Integral()))
    tlegend.AddEntry(hs[1], args.samples[1] + " [{:.2f}]".format(hs[1].Integral()))

    tcanvasRatio.cd()
    canvasPad1Name = 'pad1_' + "_" + var
    pad1 = R.TPad(canvasPad1Name,canvasPad1Name, 0, 1-0.72, 1, 1)
    pad1.SetTopMargin(0.098)
    pad1.SetBottomMargin(0.000) 
    pad1.Draw()

    minXused = hs[0].GetXaxis().GetBinLowEdge(1)
    maxXused = hs[0].GetXaxis().GetBinUpEdge(hs[1].GetNbinsX())
    minYused = hs[0].GetMinimum()
    maxYused = hs[0].GetMaximum()
        
    pad1.cd()
    #print " pad1 = ", pad1
    canvasFrameDistroName = 'frame_distro_' + "_" + var
    frameDistro = pad1.DrawFrame(minXused, 0.0, maxXused, 1.0, canvasFrameDistroName)
    xAxisDistro = frameDistro.GetXaxis()
    xAxisDistro.SetNdivisions(6,5,0)

    print(var)
    xAxisDistro.SetTitle(var)
    frameDistro.GetYaxis().SetTitle("Events")
    frameDistro.GetYaxis().SetRangeUser( 0, maxH*1.5 )

    hs[0].SetFillStyle(1001)
    hs[0].Draw("hist same")
    hs[1].Draw("hist same")

    tlegend.Draw("same")

    CMS_lumi.writeExtraText = 1
    CMS_lumi.extraText = "Preliminary"
    CMS_lumi.lumi_sqrtS = args.label # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

    iPos = 0
    iPeriod = 0
    if( iPos==0 ): CMS_lumi.relPosX = 0.14
    CMS_lumi.CMS_lumi(pad1, iPeriod, iPos)    

    # draw back all the axes            
    #frameDistro.Draw("AXIS")
    pad1.RedrawAxis()

    tcanvasRatio.cd()
    canvasPad2Name = 'pad2_' + "_" + var
    pad2 = R.TPad(canvasPad2Name,canvasPad2Name,0,0,1,1-0.72)
    pad2.SetTopMargin(0.000)
    pad2.SetBottomMargin(0.392)
    pad2.Draw()
    #pad2.cd().SetGrid()
    pad2.cd()

    #print " pad1 = ", pad1
    #print " pad2 = ", pad2, " minXused = ", minXused, " maxXused = ", maxXused
    canvasFrameRatioName = 'frame_ratio_'  + "_" + var
    #print " canvasFrameRatioName = ", canvasFrameRatioName
    frameRatio = pad2.DrawFrame(minXused, 0.0, maxXused, 2.0, canvasFrameRatioName)
    #print " pad2 = ", pad2
    # style from https://ghm.web.cern.ch/ghm/plots/MacroExample/myMacro.py
    xAxisDistro = frameRatio.GetXaxis()
    xAxisDistro.SetNdivisions(6,5,0)

    frameRatio.GetXaxis().SetTitle(var)
    frameRatio.GetYaxis().SetTitle("ratio")
    #frameRatio.GetYaxis().SetRangeUser( 0.0, 2.0 )
    frameRatio.GetYaxis().SetRangeUser(*args.yratio  )

    Pad2TAxis(frameRatio)
    # tgrErrRatio.Draw("2 same")
    tgrRatio.SetLineWidth(2)
    tgrRatio.Draw("P same")

    pad2.RedrawAxis()
    pad2.SetGrid()

    #frameDistro.GetYaxis().SetRangeUser(  )
    #pad1.SetLogy(True)

    tcanvasRatio.cd()

    tcanvasRatio.Update()
    tcanvasRatio.Draw()
    tcanvasRatio.SaveAs(args.output + "_{}.png".format(var))

    _minLogC =  1
    _maxLogC = 1e2
    frameDistro.GetYaxis().SetRangeUser( min(_minLogC, maxH/1000), _maxLogC * maxH )
    pad1.SetLogy(True)
    tcanvasRatio.SaveAs(args.output + "_{}_log.png".format(var))
