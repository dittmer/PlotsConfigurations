import os
import subprocess
import string
import ROOT
import sys

if not len(sys.argv) == 2:
  print("Usage: python computeQCDScaleWeights.py <signal>")
  exit()

signal = sys.argv[1]

signals = {
  'WH_hww'   : {'HWplusJ_HToWW_M125'     : 0.1810, 'HWminusJ_HToWW_M125' : 0.1160},
  'ZH_hww'   : {'HZJ_HToWW_M125'         : 0.187},
  'ggZH_hww' : {'GluGluZH_HToWW_M125'    : 1.0000},
  'ttH_hww'  : {'ttHToNonbb_M125'        : 0.2120},
  'WH_htt'   : {'HWplusJ_HToTauTau_M125' : 0.0532, 'HWminusJ_HToTauTau_M125' : 0.0341},
  'ZH_htt'   : {'HZJ_HToTauTau_M125'     : 0.0550},
}

if signal not in signals.keys():
  print("Signal must be one of: WH_hww, ZH_hww, ggZH_hww, ttH_hww, WH_htt, ZH_htt")
  exit()

if os.path.exists('/afs/cern.ch/user/d/dittmer/private/hww2018/CMSSW_9_4_12/src/PlotsConfigurations/Configurations/ZH3l/STXS_nanoAOD/v7/HTXS_stage1p2_categories.py') :
  handle = open('/afs/cern.ch/user/d/dittmer/private/hww2018/CMSSW_9_4_12/src/PlotsConfigurations/Configurations/ZH3l/STXS_nanoAOD/v7/HTXS_stage1p2_categories.py','r')
  contents = handle.read()
  exec(contents)
  handle.close()

yields = {}
counts = {}
qcdSF = {}

print(signal)
prod = signal.split('_')[0]

for dataset in signals[signal].keys():

  yields[dataset] = {}

  chain = ROOT.TChain("Events")

  with open("/afs/cern.ch/user/d/dittmer/private/hww2018/CMSSW_9_4_12/src/PlotsConfigurations/Configurations/ZH3l/STXS_nanoAOD/v7/"+dataset+".txt","r") as f:
    for ifile in f.readlines():
      chain.Add('root://cms-xrd-global.cern.ch:/'+ifile)

  counts[dataset] = chain.GetEntries()

  hup = ROOT.TH1F("hup","hup",1,0,2)
  hnom = ROOT.TH1F("hnom","hnom",1,0,2)
  hdown = ROOT.TH1F("hdown","hdown",1,0,2)

  for cat,num in HTXSStage1_2Categories.iteritems():
    if (prod == "WH" and ("QQ2HQQ" in cat or "QQ2HLNU" in cat)) or (prod == "ZH" and ("QQ2HQQ" in cat or "QQ2HLL" in cat)) or (prod == "ggZH" and "GG2HLL" in cat) or (prod == "ttH" and "TTH" in cat):
      chain.Draw("1>>hnom" ,"(HTXS_stage1_2_cat_pTjet30GeV=="+str(num)+")*genWeight","goff")
      chain.Draw("1>>hup"  ,"(HTXS_stage1_2_cat_pTjet30GeV=="+str(num)+")*genWeight*LHEScaleWeight[0]","goff")
      chain.Draw("1>>hdown","(HTXS_stage1_2_cat_pTjet30GeV=="+str(num)+")*genWeight*LHEScaleWeight[8]","goff")
      yields[dataset][cat] = (hnom.Integral(),hup.Integral(),hdown.Integral())

for cat in HTXSStage1_2Categories.keys():
  nnom = nup = ndown = 0.0
  for dataset,xsec in signals[signal].items():
    if cat in yields[dataset]:
      nnom  += yields[dataset][cat][0]*xsec/counts[dataset]
      nup   += yields[dataset][cat][1]*xsec/counts[dataset]
      ndown += yields[dataset][cat][2]*xsec/counts[dataset]
  if nnom != 0:
    qcdSF[cat] = [str(nup/nnom), str(ndown/nnom)]

print(qcdSF)

