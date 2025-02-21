import os
import subprocess

signals = ['HWplusJ_HToWW_M125','HWminusJ_HToWW_M125','HZJ_HToWW_M125','GluGluZH_HToWW_M125','ttHToNonbb_M125','HWplusJ_HToTauTau_M125','HWminusJ_HToTauTau_M125','HZJ_HToTauTau_M125']

if os.path.exists('/afs/cern.ch/user/d/dittmer/private/hww2018/CMSSW_9_4_12/src/LatinoAnalysis/NanoGardener/python/framework/samples/Autumn18_102X_nAODv7.py'):
  handle = open('/afs/cern.ch/user/d/dittmer/private/hww2018/CMSSW_9_4_12/src/LatinoAnalysis/NanoGardener/python/framework/samples/Autumn18_102X_nAODv7.py','r')
  contents = handle.read()
  exec(contents)
  handle.close()

for dataset_short in signals:
  dataset = Samples[dataset_short]['nanoAOD']
  out = subprocess.run(['dasgoclient', '-query=file dataset=%s'%dataset],capture_output=True,text=True)
  with open(dataset_short+".txt","w") as f:
    for ifile in out.stdout.splitlines():
      f.write(ifile+'\n')
    
