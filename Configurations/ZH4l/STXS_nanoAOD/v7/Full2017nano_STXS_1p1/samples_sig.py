import os
import subprocess
import string
import inspect 

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # Full2017nano_STXS_1p1
configurations = os.path.dirname(configurations) # v7
configurations = os.path.dirname(configurations) # STXS_nanoAOD
configurations = os.path.dirname(configurations) # ZH4l

global getSampleFiles
from LatinoAnalysis.Tools.commonTools import getSampleFiles, addSampleWeight, getBaseWnAOD

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

########################################
########################skims############
#########################################

dataReco = 'Run2017_102X_nAODv7_Full2017v7'

mcProduction = 'Fall2017_102X_nAODv7_Full2017v7'

mcSteps = 'MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7{var}'

dataSteps = 'DATAl1loose2017v7__l2loose__l2tightOR2017v7'
###########################################
###### Tree Directory according to site ######
##############################################

SITE=os.uname()[1]
xrootdPath=''
if    'iihe' in SITE :
  xrootdPath  = 'dcap://maite.iihe.ac.be/'
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015/'
elif  'cern' in SITE :
  #xrootdPath='root://eoscms.cern.ch/'
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
        #return '/afs/cern.ch/user/y/yiiyama/public/hwwvirtual/Summer16/l2tightOR__{var}'.format(var=var)
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))
        #return '/afs/cern.ch/user/y/yiiyama/public/hwwvirtual/Summer16/l2tightOR'

mcDirectory = makeMCDirectory()

dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)

#directory = treeBaseDir+'Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6__l2loose__l2tightOR2016v6/'
#directory1= treeBaseDir+'Summer16_102X_nAODv5_SigOnly_Full2016v5/MCl1loose2016v5__MCCorr2016v5__l2loose__l2tightOR2016v5/'+skim
################################################
############ NUMBER OF LEPTONS #################
################################################

Nlep='4'
#Nlep='3'
#Nlep='4'

################################################
############### Lepton WP ######################
##############################################
eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'

LepWPCut        = 'LepCut'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
LepWPweight     = 'LepSF'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP


################################################
############ BASIC MC WEIGHTS ##################
################################################

XSWeight      = 'XSWeight'
SFweight      = 'SFweight'+Nlep+'l*'+LepWPweight+'*'+LepWPCut+'*PrefireWeight'+'*Jet_PUIDSF'
PromptGenLepMatch   = 'PromptGenLepMatch'+Nlep+'l'
PromptGenLepMatch2l   = 'PromptGenLepMatch'+'2l'
PromptGenLepMatch3l   = 'PromptGenLepMatch'+'3l'


################################################
############## FAKE WEIGHTS ####################
################################################

if Nlep == '2' :
  fakeW = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP
else:
  fakeW = 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l'


################################################
############### B-Tag  WP ######################
################################################

#FIXME b-tagging to be optimized
# Definitions in aliases.py


SFweight += '*btagSF'

################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

##########################################
################ SIGNALS #################
##########################################

if os.path.exists('%s/src/PlotsConfigurations/Configurations/ZH3l/STXS_nanoAOD/v7/HTXS_stage1p2_categories.py'%os.getenv('CMSSW_BASE')) :
  handle = open('%s/src/PlotsConfigurations/Configurations/ZH3l/STXS_nanoAOD/v7/HTXS_stage1p2_categories.py'%os.getenv('CMSSW_BASE'),'r')
  exec(handle)
  handle.close()

############ ZH H->WW ############

samples['ZH_hww']  = {  'name': nanoGetSampleFiles(mcDirectory,'HZJ_HToWWTo2L2Nu_M125'),
                        'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch+'*'+METFilter_MC,
                        'suppressNegativeNuisances' :['all'],
                        'FilesPerJob' : 3,
                        'subsamples' : {}
                    }

samples['ggZH_hww'] = {  'name': nanoGetSampleFiles(mcDirectory,'GluGluZH_HToWWTo2L2Nu_M125'),
                         'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch+'*'+METFilter_MC,
                         'suppressNegativeNuisances' :['all'],
                         'FilesPerJob' : 5,
                        'subsamples' : {}
                     }

############ H->TauTau ############

samples['ZH_htt']  = {  'name'   : nanoGetSampleFiles(mcDirectory,'HZJ_HToTauTau_M125'),
                           'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch+'*'+METFilter_MC ,
                           'suppressNegative' :['all'],
                           'suppressNegativeNuisances' :['all'],
                           'subsamples' : {}
                        }

for cat,num in HTXSStage1_2Categories.iteritems():
    if 'QQ2HQQ' in cat: #qqVH had
        samples['ZH_hww']['subsamples'][cat]   = 'HTXS_stage1_2_cat_pTjet30GeV == '+str(num)
        samples['ZH_htt']['subsamples'][cat]   = 'HTXS_stage1_2_cat_pTjet30GeV == '+str(num)
    elif 'QQ2HLL' in cat: #qqZH lep
        samples['ZH_hww']['subsamples'][cat]   = 'HTXS_stage1_2_cat_pTjet30GeV == '+str(num)
        samples['ZH_htt']['subsamples'][cat]   = 'HTXS_stage1_2_cat_pTjet30GeV == '+str(num)
    elif 'GG2HLL' in cat: #ggZH lep
        samples['ggZH_hww']['subsamples'][cat] = 'HTXS_stage1_2_cat_pTjet30GeV == '+str(num)

