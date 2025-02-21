from optparse import OptionParser
parser = OptionParser()
(options, args) = parser.parse_args()
options.bin = True 
options.noJMax = False
options.nuisancesToExclude = ''
options.verbose = 1
options.stat = False

def diff_lists(list0,list1,name):

    only0 = list(set(list0)-set(list1))
    only1 = list(set(list1)-set(list0))
    for entry in only0:
        print '< %s %s'%(name,entry)
    for entry in only1:
        print '> %s %s'%(name,entry)
    return list(set(list0).intersection(set(list1)))

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.gSystem.Load("libHiggsAnalysisCombinedLimit")

from HiggsAnalysis.CombinedLimit.DatacardParser import *

DC0 = parseCard(file(args[0]), options)
DC1 = parseCard(file(args[1]), options)

# check if cards have different bins
bins0 = DC0.bins
bins1 = DC1.bins
common_bins = diff_lists(bins0,bins1,'Bin')

# check if cards have different observations, for common bins
for ibin in common_bins:
    if DC0.obs[ibin] != DC1.obs[ibin]:
        print 'Different observations in bin %s: %f vs %f'%(ibin,DC0.obs[ibin],DC1.obs[ibin])

# check if cards have different processes (overall)
proc0 = DC0.processes
proc1 = DC1.processes
common_processes = diff_lists(proc0,proc1,'Process')

# check if cards have different processes (per-bin level)
common_processes_bin = {}
for ibin in common_bins:
    procs0 = list(set(DC0.exp[ibin].keys()).intersection(set(common_processes)))
    procs1 = list(set(DC1.exp[ibin].keys()).intersection(set(common_processes)))
    common_processes_bin[ibin] = diff_lists(procs0,procs1,'Bin %s process'%ibin)
    # check if expectations are different for common processes
    for iproc in common_processes_bin[ibin]:
        if DC0.exp[ibin][iproc] != DC1.exp[ibin][iproc] :
            print 'Different expectations for %s in bin %s: %f vs %f'%(iproc,ibin,DC0.exp[ibin][iproc],DC1.exp[ibin][iproc]) 

# check if cards have different systematics
nuis_dict0 = {}
nuis_dict1 = {}
for line in DC0.systs:
    nuis_dict0[line[0]] = line[4]
    nuis_dict0[line[0]]['type'] = line[2]
for line in DC1.systs:
    nuis_dict1[line[0]] = line[4]
    nuis_dict1[line[0]]['type'] = line[2]

common_nuisances = diff_lists(nuis_dict0.keys(),nuis_dict1.keys(),'Nuisance')

# check if systematics applied differently on per-bin / per-process level
for nuisance in common_nuisances:
    if nuis_dict0[nuisance]['type'] != nuis_dict1[nuisance]['type']:
        print 'Systematic %s has different types: %s vs %s'%(nuisance,nuis_dict0[nuisance]['type'],nuis_dict1[nuisance]['type'])
        continue
    for ibin in common_bins:
        for iproc in common_processes_bin[ibin]:
            val0 = nuis_dict0[nuisance][ibin][iproc]
            val1 = nuis_dict1[nuisance][ibin][iproc]
            if val0 != val1:
                val0string = '/'.join([str(val) for val in val0]) if isinstance(val0,list) else str(val0)
                val1string = '/'.join([str(val) for val in val1]) if isinstance(val1,list) else str(val1)
                print 'Systematic %s has different values for %s in bin %s: %s vs %s'%(nuisance,iproc,ibin,val0string,val1string)

# check rateParams?
# rateParams : dict of rateParam                                                                                                                                                                          
