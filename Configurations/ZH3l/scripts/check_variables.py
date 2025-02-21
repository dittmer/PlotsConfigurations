import ROOT
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("rootfile", help="file path")
args = parser.parse_args()

directory = args.rootfile.rsplit('/',1)[0]
systematic = directory.rsplit('__',1)[1]
systematic = systematic.strip('_suffix')
systematic = systematic.strip('up')
systematic = systematic.strip('down')

f0 = ROOT.TFile(args.rootfile)
t0 = f0.Get("Events")
branchnames = [branch.GetName() for branch in t0.GetListOfBranches()]
file_var = [name.split('_'+systematic)[0] for name in branchnames]
file_var = list(set(file_var))
print file_var
handle = open('/afs/cern.ch/user/d/dittmer/private/hww2018/CMSSW_9_4_12/src/LatinoAnalysis/NanoGardener/python/data/BranchMapping_cfg.py','r')
exec(handle)
handle.close()

cfg_var = []
if ("JES" in systematic)   : cfg_var = _JES_branches
if ("ElepT" in systematic) : cfg_var = _ElepT_branches
if ("MupT" in systematic)  : cfg_var = _MupT_branches
if ("MET" in systematic)   : cfg_var = _MET_branches

print 'Variables in both config and file:'
for name in cfg_var: 
    if (name in file_var): print name

print
print 'Variables in config but not file:'
for name in cfg_var:
    if not (name in file_var): print name

file_var.sort()
print
print 'Variables in file but not config:'
for name in file_var:
    if not (name in cfg_var): print name
