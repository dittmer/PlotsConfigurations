import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2018
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations
configurations = os.path.dirname(configurations)

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

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

mcProduction = 'Autumn18_102X_nAODv7_Full2018v7'

dataReco = 'Run2018_102X_nAODv7_Full2018v7'

fakeReco = 'Run2018_102X_nAODv7_Full2018v7'

mcSteps = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7{var}'

fakeSteps = 'DATAl1loose2018v7__l2loose__fakeW'

dataSteps = 'DATAl1loose2018v7__l2loose__l2tightOR2018v7'

##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano' ##ours CERN

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

mcDirectory = makeMCDirectory()
fakeDirectory = os.path.join(treeBaseDir, fakeReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)


#signalDirectory = '/eos/user/r/rocio/MonoH/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'
signalDirectory = '/eos/user/t/tcarnaha/Summer_2022/HWW_Ntuples/Autumn18_102X_nAODv7_Full2018v7' ##TC

################################################
############ Data DECLARATION ##################
################################################

DataRun = [
            ['A','Run2018A-02Apr2020-v1'] ,
            ['B','Run2018B-02Apr2020-v1'] ,
            ['C','Run2018C-02Apr2020-v1'] ,
            ['D','Run2018D-02Apr2020-v1'] ,
          ]

DataSets = ['MuonEG','DoubleMuon','SingleMuon','EGamma']

DataTrig = {
            'MuonEG'         : 'Trigger_ElMu' ,
            'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
            'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
            'EGamma'         : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && (Trigger_sngEl || Trigger_dblEl)' ,
           }


#########################################
############ MC COMMON ##################
#########################################

mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'


##TC
###########################################
#############  BACKGROUNDS  ###############
###########################################

###### DY #######

filesDYHT = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO_ext1') + \
nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-100to200') + \
nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-200to400') + \
nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-400to600') + \
nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-600toInf') + \
nanoGetSampleFiles(mcDirectory, 'DYJetsToTT_MuEle_M-50') + \
nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-70to100') + \
nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-100to200') + \
nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-200to400') + \
nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-400to600') + \
nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-600to800') + \
nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-800to1200') + \
nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-1200to2500') + \
nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-2500toInf')

samples['DY'] = {
    'name': filesDYHT,
    'weight': mcCommonWeight + '*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 && Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )',
    'suppressNegative':['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 2,
}

addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO_ext1',  'LHE_HT<100.0')
addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50',  'LHE_HT<70.0')


###### Top #######

files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
    nanoGetSampleFiles(mcDirectory, 'ST_s-channel_ext1') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop_ext1') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_top_ext1')

samples['top'] = {
    'name': files,
    'weight': mcCommonWeight,
    'suppressNegative':['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 1,
}

addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')

###### WW ########

samples['WW'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu'),
    'weight': mcCommonWeight + '*nllW*ewknloW',
    'suppressNegative':['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 3
}

samples['WWewk'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WpWmJJ_EWK'),
    'weight': mcCommonWeight + '*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)', #filter tops and Higgs
    'suppressNegative':['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}

# k-factor 1.4 already taken into account in XSWeight
files = nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENEN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENMN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENTN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNEN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNMN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNTN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNEN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNMN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNTN')

samples['ggWW'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.53/1.4', # updating k-factor
    'suppressNegative':['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}

######## Vg ########

files = nanoGetSampleFiles(mcDirectory, 'Wg_AMCNLOFXFX') + \
      nanoGetSampleFiles(mcDirectory, 'Wg_AMCNLOFXFX_PDFWeights') + \
      nanoGetSampleFiles(mcDirectory, 'Wg_AMCNLOFXFX_PDFWeights_ext1') + \
      nanoGetSampleFiles(mcDirectory, 'ZGToLLG')
  
samples['Vg'] = {
      'name': files,
      'weight': mcCommonWeightNoMatch + '*(Gen_ZGstar_mass <= 0)',
    'suppressNegative':['all'],
    'suppressNegativeNuisances' :['all'],
      'FilesPerJob': 4
  }


# wgbasew = getBaseWnAOD(mcDirectory,'Autumn18_102X_nAODv7_Full2018v7',['Wg_AMCNLOFXFX','Wg_AMCNLOFXFX_PDFWeights','Wg_AMCNLOFXFX_PDFWeights_ext1'])
# addSampleWeight(samples,'Vg','Wg_AMCNLOFXFX','191.4/586.*'+wgbasew+'/baseW')
# addSampleWeight(samples,'Vg','Wg_AMCNLOFXFX_PDFWeights','191.4/586.*'+wgbasew+'/baseW')
# addSampleWeight(samples,'Vg','Wg_AMCNLOFXFX_PDFWeights_ext1','191.4/586.*'+wgbasew+'/baseW')

######## VgS ########

files = nanoGetSampleFiles(mcDirectory, 'Wg_AMCNLOFXFX') + \
        nanoGetSampleFiles(mcDirectory, 'Wg_AMCNLOFXFX_PDFWeights') + \
        nanoGetSampleFiles(mcDirectory, 'Wg_AMCNLOFXFX_PDFWeights_ext1') + \
        nanoGetSampleFiles(mcDirectory, 'ZGToLLG') + \
        nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')
  

samples['VgS'] = {
      'name': files,
    'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'suppressNegative':['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4,
}
  
# addSampleWeight(samples, 'VgS', 'Wg_AMCNLOFXFX', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)*191.4/586.*'+wgbasew+'/baseW')
# addSampleWeight(samples, 'VgS', 'Wg_AMCNLOFXFX_PDFWeights', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)*191.4/586.*'+wgbasew+'/baseW')
# addSampleWeight(samples, 'VgS', 'Wg_AMCNLOFXFX_PDFWeights_ext1', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)*191.4/586.*'+wgbasew+'/baseW')
# addSampleWeight(samples, 'VgS', 'ZGToLLG', '(Gen_ZGstar_mass > 0)')
# addSampleWeight(samples, 'VgS', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')



############ VZ ############

files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu_ext2') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Q') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo4L_ext2') + \
    nanoGetSampleFiles(mcDirectory, 'WZTo2L2Q')

samples['VZ'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.11',
    'suppressNegative':['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}

########## VVV #########

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWW')

samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'suppressNegative':['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}


########## Higgs #########

files =  nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125') + \
         nanoGetSampleFiles(mcDirectory, 'VBFHToWWTo2L2Nu_M125') + \
         nanoGetSampleFiles(mcDirectory, 'HZJ_HToWWTo2L2Nu_M125') + \
         nanoGetSampleFiles(mcDirectory, 'GluGluZH_HToWWTo2L2Nu_M125') + \
         nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToWW_M125') + \
         nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToWW_M125') + \
         nanoGetSampleFiles(mcDirectory, 'ttHToNonbb_M125') + \
         nanoGetSampleFiles(mcDirectory, 'GluGluHToTauTau_M125') + \
         nanoGetSampleFiles(mcDirectory, 'VBFHToTauTau_M125') + \
         nanoGetSampleFiles(mcDirectory, 'HZJ_HToTauTau_M125') + \
         nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToTauTau_M125') + \
         nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToTauTau_M125')
         
samples['Higgs_onshell'] = {
    'name': files,
    'weight': mcCommonWeight + '* (LHE_mWW < 160.)', ##onshell range 2*W ~160
    'suppressNegative':['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 5,
}


signalDirectory = '/eos/user/t/tcarnaha/Summer_2022/HWW_Ntuples/Autumn18_102X_nAODv7_Full2018v7/AddLHE_MEs__AddMC_baseW__AddHWW_Offshell_Wgts_v3__MCl1loose2018v7__MCCorr2018v7_l2tight/'

files =  nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M160') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M170') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M180') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M190') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M200') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M210') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M230') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M250') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M270') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M300') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M350') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M400') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M450') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M500') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M550') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M600') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M700') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M800') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M900') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M1000') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M1500') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M2000') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M2500') + \
         nanoGetSampleFiles(signalDirectory, 'GluGluHToWWTo2L2Nu_M3000') 

samples['Higgs_offshell'] = {
    'name': files,
    'weight': mcCommonWeight + ' * p_Gen_CPStoBWPropRewgt * p_Gen_GG_SIG_kappaTopBot_1_ghz1_1_MCFM * HWWOffshell_combineWgt * (LHE_mWW > 160.)', ##all wgts applied CPStoBW SMH - computing LHE_mWW fly - include in aliases.py
    'suppressNegative':['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 10,
}


###########################################
################## FAKE ###################
###########################################

samples['Fake'] = {
  'name': [],
  'weight': 'METFilter_DATA*fakeW',
  'weights': [],
  'suppressNegative':['all'],
  'suppressNegativeNuisances' :['all'],
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
  'FilesPerJob': 50
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd)
    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))

