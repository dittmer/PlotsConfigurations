import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2016
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight,getBaseWnAOD

def nanoGetSampleFiles(inputDir, sample):
    try:
        if _samples_noload:
            return []
    except NameError:
        pass

    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

# samples

try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()

################################################
################# SKIMS ########################
################################################


dataReco = 'Run2017_102X_nAODv7_Full2017v7'

mcProduction = 'Fall2017_102X_nAODv7_Full2017v7'

mcSteps = 'MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7{var}'

fakeSteps = 'DATAl1loose2017v7__l2loose__fakeW'

dataSteps = 'DATAl1loose2017v7__l2loose__l2tightOR2017v7'


##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
        # return '/afs/cern.ch/user/y/yiiyama/public/hwwvirtual/Summer16/l2tightOR__{var}'.format(var=var)
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))
        # return '/afs/cern.ch/user/y/yiiyama/public/hwwvirtual/Summer16/l2tightOR'

mcDirectory = makeMCDirectory()
fakeDirectory = os.path.join(treeBaseDir, dataReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
    ['B','Run2017B-02Apr2020-v1'],
    ['C','Run2017C-02Apr2020-v1'],
    ['D','Run2017D-02Apr2020-v1'],
    ['E','Run2017E-02Apr2020-v1'],
    ['F','Run2017F-02Apr2020-v1']
]

DataSets = ['MuonEG','SingleMuon','SingleElectron','DoubleMuon', 'DoubleEG']

DataTrig = {
    'MuonEG'         : ' Trigger_ElMu' ,
    'SingleMuon'     : '!Trigger_ElMu && Trigger_sngMu' ,
    'SingleElectron' : '!Trigger_ElMu && !Trigger_sngMu && Trigger_sngEl',
    'DoubleMuon'     : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && Trigger_dblMu',
    'DoubleEG'       : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && !Trigger_dblMu && Trigger_dblEl'
}


#########################################
############ MC COMMON ##################
#########################################

# SFweight does not include btag weights
mcCommonWeight        = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeightMatched = 'XSWeight*SFweight*PromptGenLepMatch3l*METFilter_MC'

###########################################
#############  BACKGROUNDS  ###############
###########################################

###### WW ########

samples['WW'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu'),
    'weight': mcCommonWeightMatched + '*nllW', # temporary
    'FilesPerJob': 5
}

######## Vg ########
samples['Wg'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM'),
    'weight': mcCommonWeight + '*(Gen_ZGstar_mass <= 0)',
    'FilesPerJob': 4
}
samples['Zg'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'ZGToLLG'),
    'weight': "*".join([mcCommonWeight, '(Gen_ZGstar_mass <= 0)']),
    'FilesPerJob': 1
    # 'FilesPerJob': 4
}

######## VgS ########

samples['WgS'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM'),
    'weight': "*".join([mcCommonWeightMatched, '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)']),
    'FilesPerJob': 4,
}
samples['ZgS'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'ZGToLLG'),
    'weight': "*".join([mcCommonWeightMatched, "(Gen_ZGstar_mass > 0)"]),
    'FilesPerJob': 4,
}

############ ZZ ############

samples['ZZ']  = {  
    'name'   :   nanoGetSampleFiles(mcDirectory,'ZZTo4L'),
    'weight': mcCommonWeightMatched,
    'FilesPerJob': 1,
                 }
addSampleWeight(samples,'ZZ','ZZTo4L',"1.17") 
# samples['ZZ'] = {
    # 'name': nanoGetSampleFiles(mcDirectory,'ZZTo4L')+nanoGetSampleFiles(mcDirectory,'ZZTo4L_ext1'),
    # 'weight': mcCommonWeightMatched,
    # 'FilesPerJob' : 1,
    # # 'FilesPerJob' : 5,
# }
# ZZbaseW   = getBaseWnAOD(mcDirectory,'Fall2017_102X_nAODv4_Full2017v5',['ZZTo4L',  'ZZTo4L_ext1'])
# addSampleWeight(samples,'ZZ','ZZTo4L',        "1.17*"+ZZbaseW+"/baseW") ## The NNLO/NLO k-factor, cited from https://arxiv.org/abs/1405.2219v1
# addSampleWeight(samples,'ZZ','ZZTo4L_ext1',   "1.17*"+ZZbaseW+"/baseW")


############ WZ ############

samples['WZ'] = {
    'name': nanoGetSampleFiles(mcDirectory,'WZTo3LNu_mllmin01'),
    'weight': mcCommonWeightMatched,
    'FilesPerJob' : 5,
}
addSampleWeight(samples,'WZ','WZTo3LNu_mllmin01', '(Gen_ZGstar_mass>=0.1)')

########## VVV #########

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWW')

samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeightMatched,
    'FilesPerJob': 4
}

###########################################
#############   SIGNALS  ##################
###########################################

signals = []
if os.path.exists('%s/src/PlotsConfigurations/Configurations/ZH3l/STXS_nanoAOD/v7/HTXS_stage1p2_categories.py'%os.getenv('CMSSW_BASE')) :
  handle = open('%s/src/PlotsConfigurations/Configurations/ZH3l/STXS_nanoAOD/v7/HTXS_stage1p2_categories.py'%os.getenv('CMSSW_BASE'),'r')
  exec(handle)
  handle.close()

#### ggH -> WW

samples['ggH_hww'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4,
}

signals.append('ggH_hww')

############ VBF H->WW ############
samples['qqH_hww'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4,
}

signals.append('qqH_hww')

############# ZH H->WW ############

samples['ZH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'HZJ_HToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4,
    'subsamples' : {}
}

signals.append('ZH_hww')

samples['ggZH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'GluGluZH_HToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4,
    'subsamples' : {}
}

signals.append('ggZH_hww')

############ WH H->WW ############

samples['WH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToWW_M125') + nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToWW_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4,
    'subsamples' : {}
}

signals.append('WH_hww')

############ ttH ############

samples['ttH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'ttHToNonbb_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4,
}

signals.append('ttH_hww')

############ H->TauTau ############

samples['ggH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToTauTau_M125_ext1'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4,
}

signals.append('ggH_htt')

samples['qqH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4,
}

signals.append('qqH_htt')

samples['ZH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'HZJ_HToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4,
    'subsamples' : {}
}

signals.append('ZH_htt')

samples['WH_htt'] = {
    'name':  nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToTauTau_M125') + nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4,
    'subsamples' : {}
}
signals.append('WH_htt')

for cat,num in HTXSStage1_2Categories.iteritems():
    if 'QQ2HQQ' in cat: #qqVH had
        samples['WH_hww']['subsamples'][cat]   = 'HTXS_stage1_2_cat_pTjet30GeV == '+str(num)
        samples['WH_htt']['subsamples'][cat]   = 'HTXS_stage1_2_cat_pTjet30GeV == '+str(num)
        samples['ZH_hww']['subsamples'][cat]   = 'HTXS_stage1_2_cat_pTjet30GeV == '+str(num)
        samples['ZH_htt']['subsamples'][cat]   = 'HTXS_stage1_2_cat_pTjet30GeV == '+str(num)
    elif 'QQ2HLNU' in cat: #qqWH lep
        samples['WH_hww']['subsamples'][cat]   = 'HTXS_stage1_2_cat_pTjet30GeV == '+str(num)
        samples['WH_htt']['subsamples'][cat]   = 'HTXS_stage1_2_cat_pTjet30GeV == '+str(num)
    elif 'QQ2HLL' in cat: #qqZH lep
        samples['ZH_hww']['subsamples'][cat]   = 'HTXS_stage1_2_cat_pTjet30GeV == '+str(num)
        samples['ZH_htt']['subsamples'][cat]   = 'HTXS_stage1_2_cat_pTjet30GeV == '+str(num)
    elif 'GG2HLL' in cat: #ggZH lep
        samples['ggZH_hww']['subsamples'][cat] = 'HTXS_stage1_2_cat_pTjet30GeV == '+str(num)

############ WH H->WW ############

# samples['WH_hww'] = {
    # 'name':   nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToWW_M125') + nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToWW_M125'),
    # 'weight': mcCommonWeightMatched,
    # 'FilesPerJob': 4
# }

# signals.append('WH_hww')

############ H->TauTau ############

# samples['WH_htt'] = {
    # 'name':  nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToTauTau_M125') + nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToTauTau_M125'),
    # 'weight': mcCommonWeightMatched,
    # 'FilesPerJob': 4
# }
# signals.append('WH_htt')

# samples['H_htt'] = {
    # 'name':  nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToTauTau_M125')
           # + nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToTauTau_M125')
           # + nanoGetSampleFiles(mcDirectory, 'GluGluHToTauTau_M125')
           # + nanoGetSampleFiles(mcDirectory, 'VBFHToTauTau_M125')
           # + nanoGetSampleFiles(mcDirectory, 'HZJ_HToTauTau_M125'),
    # 'weight': mcCommonWeightMatched,
    # 'FilesPerJob': 4
# }
# signals.append('H_htt')


###########################################
################## FAKE ###################
###########################################

samples['Fake'] = {
  'name': [],
  'weight': 'METFilter_DATA*fakeW',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 50
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(fakeDirectory, pd + '_' + sd)
    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))

###########################################
################## DATA ###################
###########################################

samples['DATA'] = {
  'name': [],
  'weight': 'METFilter_DATA*LepWPCut',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 200
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd)
    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))

