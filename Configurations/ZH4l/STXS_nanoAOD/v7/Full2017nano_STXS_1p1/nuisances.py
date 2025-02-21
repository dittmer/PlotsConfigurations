# nuisances
# name of samples here must match keys in samples.py 
from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

try:
    mc = [skey for skey in samples if skey != 'DATA' and not skey.startswith('Fake')]
except NameError:
    mc = []
    cuts = {}
    nuisances = {}
    def makeMCDirectory(x=''):
        return ''

from LatinoAnalysis.Tools.HiggsXSection import HiggsXSection
HiggsXS = HiggsXSection()


################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2017',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc if skey not in ['ZZ'])
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.008') for skey in mc if skey not in ['ZZ'])
}

nuisances['lumi_BBDefl'] = {
    'name': 'lumi_13TeV_BBDefl',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc if skey not in ['ZZ'])
}

nuisances['lumi_DynBeta'] = {
    'name': 'lumi_13TeV_DynBeta',
    'type': 'lnN',
    'samples': dict((skey, '1.005') for skey in mc if skey not in ['ZZ'])
}

nuisances['lumi_Ghosts'] = {
    'name': 'lumi_13TeV_Ghosts',
    'type': 'lnN',
    'samples': dict((skey, '1.001') for skey in mc if skey not in ['ZZ'])
}

nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc if skey not in ['ZZ'])
}

nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc if skey not in ['ZZ'])
}
'''
#### FAKES

nuisances['fake_syst'] = {
    'name': 'CMS_fake_syst',
    'type': 'lnN',
    'samples': {
        #'Fakes': '1.3'
        'Fakes_ee': '1.3',
        'Fakes_mm': '1.3',
        'Fakes_em': '1.3'
    },
}

nuisances['fake_ele'] = {
    'name': 'CMS_fake_e_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        #'Fakes': ['fakeWEleUp', 'fakeWEleDown'],
        'Fakes_ee': ['fakeWEleUp', 'fakeWEleDown'],
        'Fakes_em': ['fakeWEleUp', 'fakeWEleDown']
        
    }
}

nuisances['fake_ele_stat'] = {
    'name': 'CMS_fake_stat_e_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        #'Fakes': ['fakeWStatEleUp', 'fakeWStatEleDown']
        'Fakes_ee': ['fakeWStatEleUp', 'fakeWStatEleDown'],
        'Fakes_em': ['fakeWStatEleUp', 'fakeWStatEleDown']
    }
}

nuisances['fake_mu'] = {
    'name': 'CMS_fake_m_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        #'Fakes': ['fakeWMuUp', 'fakeWMuDown'],
        'Fakes_mm': ['fakeWMuUp', 'fakeWMuDown'],
        'Fakes_em': ['fakeWMuUp', 'fakeWMuDown']
    }
}

nuisances['fake_mu_stat'] = {
    'name': 'CMS_fake_stat_m_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        #'Fakes': ['fakeWStatMuUp', 'fakeWStatMuDown'],
        'Fakes_mm': ['fakeWStatMuUp', 'fakeWStatMuDown'],
        'Fakes_em': ['fakeWStatMuUp', 'fakeWStatMuDown']
    }
}
'''
###### B-tagger

for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2017'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
    }

##### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_4l_u)/(TriggerEffWeight_4l))*(TriggerEffWeight_4l>0.02) + (TriggerEffWeight_4l<=0.02)', '(TriggerEffWeight_4l_d)/(TriggerEffWeight_4l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc)
}

prefire_syst = ['PrefireWeight_Up/PrefireWeight', 'PrefireWeight_Down/PrefireWeight']

nuisances['prefire'] = {
    'name': 'CMS_eff_prefiring_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, prefire_syst) for skey in mc)
}

##### Electron Efficiency and energy scale

nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc)
}

nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2017',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp' : 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('ElepTup_suffix'),
    'folderDown': makeMCDirectory('ElepTdo_suffix'),
    'AsLnN': '1'
}

##### Muon Efficiency and energy scale

nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc)
}

nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2017',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('MupTup_suffix'),
    'folderDown': makeMCDirectory('MupTdo_suffix'),
    'AsLnN': '1'
}

##### Jet energy scale


jes_systs = ['JESAbsolute','JESAbsolute_2017','JESBBEC1','JESBBEC1_2017','JESEC2','JESEC2_2017','JESFlavorQCD','JESHF','JESHF_2017','JESRelativeBal','JESRelativeSample_2017']
folderup = ""
folderdo = ""

for js in jes_systs:
  if 'Absolute' in js: 
    folderup = makeMCDirectory('JESAbsoluteup_suffix')
    folderdo = makeMCDirectory('JESAbsolutedo_suffix')
  elif 'BBEC1' in js:
    folderup = makeMCDirectory('JESBBEC1up_suffix')
    folderdo = makeMCDirectory('JESBBEC1do_suffix')
  elif 'EC2' in js:
    folderup = makeMCDirectory('JESEC2up_suffix')
    folderdo = makeMCDirectory('JESEC2do_suffix')
  elif 'HF' in js:
    folderup = makeMCDirectory('JESHFup_suffix')
    folderdo = makeMCDirectory('JESHFdo_suffix')
  elif 'Relative' in js:
    folderup = makeMCDirectory('JESRelativeup_suffix')
    folderdo = makeMCDirectory('JESRelativedo_suffix')
  elif 'FlavorQCD' in js:
    folderup = makeMCDirectory('JESFlavorQCDup_suffix')
    folderdo = makeMCDirectory('JESFlavorQCDdo_suffix')

  nuisances[js] = {
      'name': 'CMS_scale_'+js,
      'kind': 'suffix',
      'type': 'shape',
      'mapUp': js+'up',
      'mapDown': js+'do',
      'samples': dict((skey, ['1', '1']) for skey in mc),
      'folderUp': folderup,
      'folderDown': folderdo,
      'AsLnN': '1'
  }
'''
jes_systs = ['JESAbsolute','JESAbsolute_2017','JESBBEC1','JESBBEC1_2017','JESEC2','JESEC2_2017','JESFlavorQCD','JESHF','JESHF_2017','JESRelativeBal','JESRelativeSample_2017']

#jes_systs = ['JES']

for js in jes_systs:
  nuisances[js] = {
      'name': 'CMS_scale_'+js,
      'kind': 'suffix',
      'type': 'shape',
      'mapUp': js+'up',
      'mapDown': js+'do',
      'samples': dict((skey, ['1', '1']) for skey in mc),
      'folderUp': makeMCDirectory('JESup_suffix'),
      'folderDown': makeMCDirectory('JESdo_suffix'),
      'AsLnN': '1'
}
'''
##### MET energy scale

nuisances['met'] = {
    'name': 'CMS_scale_met_2017',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'METup',
    'mapDown': 'METdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('METup_suffix'),
    'folderDown': makeMCDirectory('METdo_suffix'),
    'AsLnN': '1'
}

##### Pileup#####

nuisances['PU'] = {
    'name': 'CMS_PU_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
 #       'DY': ['0.993259983266*(puWeightUp/puWeight)', '0.997656381501*(puWeightDown/puWeight)'],
        'top': ['1.00331969187*(puWeightUp/puWeight)', '0.999199609528*(puWeightDown/puWeight)'],
        'WW': ['1.0033022059*(puWeightUp/puWeight)', '0.997085330608*(puWeightDown/puWeight)'],
        'ggH_hww': ['1.0036768006*(puWeightUp/puWeight)', '0.995996570285*(puWeightDown/puWeight)'],
        'qqH_hww': ['1.00374694528*(puWeightUp/puWeight)', '0.995878596852*(puWeightDown/puWeight)'],
    },
    'AsLnN': '1',
}


### PU ID SF uncertainty
puid_syst = ['Jet_PUIDSF_up/Jet_PUIDSF', 'Jet_PUIDSF_down/Jet_PUIDSF']

nuisances['jetPUID'] = {
    'name': 'CMS_PUID_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, puid_syst) for skey in mc)
}

##### PS
'''
nuisances['PS_ISR_0jet']  = {
    'name': 'PS_ISR',
    'type': 'lnN',
    'samples': {
        'WW'     : '1.0004147/0.9990865',
        'top'    : '1.0038372/0.9949470',
        'DY'     : '1.0040364/0.9947131',
        'ggH_hww': '1.0024342/0.9966181',
        'qqH_hww': '1.0004923/0.9995787',
        'WH_hww' : '1.0012062/0.9985316',
        'ZH_hww' : '1.0007957/0.9989884',
    },
    'cuts'  : [
              'zh4l_XSF_13TeV',
              'zh4l_XDF_13TeV',
              'zh4l_ZZ_13TeV',   
]
}

nuisances['PS_FSR_0jet']  = {
    'name': 'PS_FSR',
    'type': 'lnN',
    'samples': { 
        'WW'     : '0.9968231/1.0051404',
        'top'    : '0.9705783/1.0474730',
        'DY'     : '0.9974074/1.0048384',
        'ggH_hww': '0.9955678/1.0060251',
        'qqH_hww': '0.9866768/1.0239547',
        'WH_hww' : '0.9891188/1.0215866',
        'ZH_hww' : '0.9896471/1.0173018',
    },
    'cuts'  : [
              'zh4l_XSF_13TeV',
              'zh4l_XDF_13TeV',
              'zh4l_ZZ_13TeV',
]
}
'''


# PS and UE
#FIXME: Add PS uncertainty
'''
nuisances['PS_zh4l']  = {
                'name'  : 'PS_zh4l',
                'skipCMS' : 1,
                'type'  : 'lnN',
                'samples'  : {
                   'WH_hww'   : '1.037',
                   'ZH_hww'   : '1.037',
                   'qqH_hww'    : '1.037',
                   'ggH_hww'   : '1.037',
                   'WW'   : '1.037',
                },
}
'''
nuisances['UE_CP5']  = {
                'name'  : 'UE_CP5',
                'skipCMS' : 1,
                'type'  : 'lnN',
                'samples': dict((skey, '1.015') for skey in mc if skey not in ['ZH_hww','ggZH_hww','ZH_htt']),
}


nuisances['CMS_hww_ZZ4lnorm']  = {
        'name'  : 'CMS_hww_ZZ4lnorm',
        'samples'  : {
            'ZZ' : '1.00',
            },
        'type'  : 'rateParam',
        'cuts'  : [
            'zh4l_ZZ_13TeV',
            'zh4l_XSF_13TeV_ptv_lt150',
            'zh4l_XSF_13TeV_ptv_gt150',
            'zh4l_XDF_13TeV_ptv_lt150',
            'zh4l_XDF_13TeV_ptv_gt150',
            ]
}


## Shape nuisance due to QCD scale variations for DY
# LHE scale variation weights (w_var / w_nominal)

## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
variations = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']

nuisances['QCDscale_VV'] = {
    'name': 'QCDscale_VV',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'WZ': variations,
        'ZZhad': variations,
        'WZhad': variations,
    }
}


# ggww and interference
nuisances['QCDscale_ggVV'] = {
    'name': 'QCDscale_ggVV',
    'type': 'lnN',
    'samples': {
        'ggWW': '1.15',
    },
}


nuisances['QCDscale_WWewk'] = {
    'name': 'QCDscale_WWewk',
    'samples': {
        'WWewk': '1.11',
    },
    'type': 'lnN'
}

##### QCD scale uncertainties for Higgs signals other than ggH


from LatinoAnalysis.Tools.HiggsXSection  import *
HiggsXS = HiggsXSection()


nuisances['QCDscale_qqH']  = {
               'name'  : 'QCDscale_qqH', 
               'samples'  : {
                   'qqH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm'),
                   'qqH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm'),
                   },
               'type'  : 'lnN',
              }

#nuisances['QCDscale_VH']  = {
#               'name'  : 'QCDscale_VH', 
#               'samples'  : {
#                   'WH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','scale','sm'),
#                   'WH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','scale','sm'),
#                   'ZH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','scale','sm'),
#                   'ZH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','scale','sm'),
#                   },
#               'type'  : 'lnN',
#              }

#nuisances['QCDscale_ggZH']  = {
#               'name'  : 'QCDscale_ggZH', 
#               'samples'  : {
#                   'ggZH_hww': HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggZH','125.09','scale','sm'),                  
#                   },
#               'type'  : 'lnN',
#              }


nuisances['QCDscale_ttH']  = {
               'name'  : 'QCDscale_ttH',
               'samples'  : {
                   'ttH_hww': HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH','125.09','scale','sm'),
                   },
               'type'  : 'lnN',
              }


nuisances['QCDscale_qqbar_ACCEPT']  = {
               'name'  : 'QCDscale_qqbar_ACCEPT', 
               'type'  : 'lnN',
               'samples'  : {
                   'qqH_hww' : '1.003',
                   'qqH_htt' : '1.003',
                   #'WH_hww'  : '1.010',
                   #'WH_htt'  : '1.010',
                   #'ZH_hww'  : '1.015',
                   #'ZH_htt'  : '1.015',
                   'VZ'      : '1.029',
                   },
              }


nuisances['QCDscale_gg_ACCEPT']  = {
               'name'  : 'QCDscale_gg_ACCEPT', 
               'samples'  : {
                   'ggWW'    : '1.012',
                   'ggH_hww' : '1.012',
                   'ggH_htt' : '1.012',
                   #'ggZH_hww': '1.012',                   
                   },
               'type'  : 'lnN',
              }

####### pdf uncertainty

nuisances['pdf_Higgs_gg']  = {
               'name'  : 'pdf_Higgs_gg', 
               'samples'  : {
                   'ggH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH' ,'125.09','pdf','sm'),
                   'ggH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH' ,'125.09','pdf','sm'),
                   #'ggZH_hww': HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggZH','125.09','pdf','sm'), 
                   'bbH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','bbH' ,'125.09','pdf','sm'),
                   },
               'type'  : 'lnN',
              }

nuisances['pdf_Higgs_ttH']  = {
               'name'  : 'pdf_Higgs_ttH',
               'samples'  : {
                   'ttH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH' ,'125.09','pdf','sm'),
                   },
               'type'  : 'lnN',
              }

nuisances['pdf_Higgs_qqbar']  = {
               'name'  : 'pdf_Higgs_qqbar', 
               'type'  : 'lnN',
               'samples'  : {
                   'qqH_hww' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm'),
                   'qqH_htt' : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm'),
                   #'WH_hww'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH' ,'125.09','pdf','sm'),
                   #'WH_htt'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH' ,'125.09','pdf','sm'),
                   #'ZH_hww'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH' ,'125.09','pdf','sm'),
                   #'ZH_htt'  : HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH' ,'125.09','pdf','sm'),
                   },
              }

nuisances['pdf_qqbar']  = {
               'name'  : 'pdf_qqbar',
               'type'  : 'lnN',
               'samples'  : {
                   'VZ'      : '1.04',  # PDF: 0.0064 / 0.1427 = 0.0448493
                   },
              }


nuisances['pdf_Higgs_gg_ACCEPT']  = {
               'name'  : 'pdf_Higgs_gg_ACCEPT', 
               'samples'  : {
                   'ggH_hww' : '1.006',
                   'ggH_htt' : '1.006',
                   'bbH_htt' : '1.006',
                   #'ggZH_hww': '1.006', 
                   },
               'type'  : 'lnN',
              }


nuisances['pdf_gg_ACCEPT']  = {
               'name'  : 'pdf_gg_ACCEPT',
               'samples'  : {
                   'ggWW'    : '1.005',
                   },
               'type'  : 'lnN',
              }


nuisances['pdf_Higgs_qqbar_ACCEPT']  = {
               'name'  : 'pdf_Higgs_qqbar_ACCEPT',
               'type'  : 'lnN',
               'samples'  : {
                   'qqH_hww' : '1.002',
                   'qqH_htt' : '1.002',
                   #'WH_hww'  : '1.003',
                   #'WH_htt'  : '1.003',
                   #'ZH_hww'  : '1.002',
                   #'ZH_htt'  : '1.002',
                   },
              }

nuisances['pdf_qqbar_ACCEPT']  = {
               'name'  : 'pdf_qqbar_ACCEPT',
               'type'  : 'lnN',
               'samples'  : {
                   #
                   'WZ'      : '1.001',
                   'ZZhad'      : '1.001',
                   'WZhad'      : '1.001',                 
                   },
              }

### QCD STXS accept                                                                                                                           

STXS_QCDUnc = {
    'VH_scale_0jet'           : ['QQ2HQQ_0J'], 
    'VH_scale_1jet'           : ['QQ2HQQ_1J'],
    'VH_scale_lowmjj'         : ['QQ2HQQ_GE2J_MJJ_0_60', 'QQ2HQQ_GE2J_MJJ_60_120', 'QQ2HQQ_GE2J_MJJ_120_350'],
    'VH_scale_highmjj_lowpt'  : ['QQ2HQQ_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_0_25', 'QQ2HQQ_GE2J_MJJ_350_700_PTH_0_200_PTHJJ_GT25', 'QQ2HQQ_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_0_25', 'QQ2HQQ_GE2J_MJJ_GT700_PTH_0_200_PTHJJ_GT25'],
    'VH_scale_highmjj_highpt' : ['QQ2HQQ_GE2J_MJJ_GT350_PTH_GT200'],
    'ZH_scale_lowpt'          : ['QQ2HLL_PTV_0_75', 'QQ2HLL_PTV_75_150', 'QQ2HLL_PTV_150_250_0J', 'QQ2HLL_PTV_150_250_GE1J', 'GG2HLL_PTV_0_75', 'GG2HLL_PTV_75_150', 'GG2HLL_PTV_150_250_0J', 'GG2HLL_PTV_150_250_GE1J'],
    'ZH_scale_highpt'         : ['QQ2HLL_PTV_GT250', 'GG2HLL_PTV_GT250']
}

# Norm factors -- note norm factors in QCDScaleFactors are [LHEScaleWeight[0]/nom, LHEScaleWeight[8]/nom]
import json
QCDScaleFactors = json.load(open('%s/src/PlotsConfigurations/Configurations/ZH3l/STXS_nanoAOD/v7/QCDScaleFactors.json'%os.getenv('CMSSW_BASE')))

for unc in STXS_QCDUnc.keys():
    nuisances[unc] = {
        'name' : unc,
        'kind' : 'weight',
        'type' : 'shape',
        'samples' : {}
    }

    for signal in ['ZH_hww','ggZH_hww','ZH_htt']:
        bins_applied = list(set(QCDScaleFactors[signal].keys()) & set(STXS_QCDUnc[unc]))
        if len(bins_applied) > 0:
            norm_QCD = ['+'.join(['(HTXS_stage1_2_cat_pTjet30GeV == {})*({})'.format(HTXSStage1_2Categories[binname],QCDScaleFactors[signal][binname][0]) for binname in bins_applied]),
                        '+'.join(['(HTXS_stage1_2_cat_pTjet30GeV == {})*({})'.format(HTXSStage1_2Categories[binname],QCDScaleFactors[signal][binname][1]) for binname in bins_applied])]
            nuisances[unc]['samples'][signal] = ['Alt$(LHEScaleWeight[0],1)/('+norm_QCD[0]+')','Alt$(LHEScaleWeight[8],1)/('+norm_QCD[1]+')']

#STXS VHlep migration uncertainties
STXS_migUnc = {
    'THU_ZH_inc'      : {'PTV_0_75' : '0.994/1.005', 'PTV_75_150' : '0.994/1.005', 'PTV_150_250_0J' : '0.994/1.005', 'PTV_150_250_GE1J' : '0.994/1.005', 'PTV_GT250' : '0.994/1.005'},
    'THU_ZH_mig75'    : {'PTV_0_75' : '0.963',       'PTV_75_150' : '1.040',       'PTV_150_250_0J' : '1.04',        'PTV_150_250_GE1J' : '1.04',        'PTV_GT250' : '1.04'},
    'THU_ZH_mig150'   : {                            'PTV_75_150' : '0.995',       'PTV_150_250_0J' : '1.013',       'PTV_150_250_GE1J' : '1.013',       'PTV_GT250' : '1.013'},
    'THU_ZH_mig250'   : {                                                          'PTV_150_250_0J' : '1.9958',      'PTV_150_250_GE1J' : '0.9958',      'PTV_GT250' : '1.014'},
    'THU_ZH_mig01'    : {                                                          'PTV_150_250_0J' : '0.956',       'PTV_150_250_GE1J' : '1.053'},
    'THU_ggZH_inc'    : {'PTV_0_75' : '0.811/1.251', 'PTV_75_150' : '0.811/1.251', 'PTV_150_250_0J' : '0.811/1.251', 'PTV_150_250_GE1J' : '0.811/1.251', 'PTV_GT250' : '0.811/1.251'},
    'THU_ggZH_mig75'  : {'PTV_0_75' : '1.9/0.1',     'PTV_75_150' : '1.27',        'PTV_150_250_0J' : '1.27',        'PTV_150_250_GE1J' : '1.27',        'PTV_GT250' : '1.27'},
    'THU_ggZH_mig150' : {                            'PTV_75_150' : '0.882',       'PTV_150_250_0J' : '1.142',       'PTV_150_250_GE1J' : '1.142',       'PTV_GT250' : '1.142'},
    'THU_ggZH_mig250' : {                                                          'PTV_150_250_0J' : '0.963',       'PTV_150_250_GE1J' : '0.963',       'PTV_GE250' : '1.154'},
    'THU_ggZH_mig01'  : {                                                          'PTV_150_250_0J' : '1.6/0.393',   'PTV_150_250_GE1J' : '1.277'} 
}

prefix = {'ZH' : 'QQ2HLL', 'ggZH' : 'GG2HLL'}

for unc in STXS_migUnc.keys():
    prod = unc.split('_')[1]
    samples_prod = [skey for skey in mc if skey.split('_')[0] == prod]
    nuisances[unc] = {
        'name' : unc,
        'type' : 'lnN',
        'samples': dict((skey+'_'+prefix[prod]+'_'+binname, STXS_migUnc[unc][binname]) for binname in STXS_migUnc[unc] for skey in samples_prod)
    }

### Generic "cross section uncertainties"

apply_on = {
    'top': [
        '(topGenPt * antitopGenPt <= 0.) * 1.0816 + (topGenPt * antitopGenPt > 0.)',
        '(topGenPt * antitopGenPt <= 0.) * 0.9184 + (topGenPt * antitopGenPt > 0.)'
    ]
}

nuisances['singleTopToTTbar'] = {
    'name': 'singleTopToTTbar',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': apply_on
}

## Top pT reweighting uncertainty

nuisances['TopPtRew'] = {
    'name': 'CMS_topPtRew',   # Theory uncertainty
    'kind': 'weight',
    'type': 'shape',
    'samples': {'top': ["1.", "1./Top_pTrw"]},
    'symmetrize': True
}

#nuisances['VgStar'] = {
#    'name': 'CMS_hww_VgStarScale',
#    'type': 'lnN',
#    'samples': {
#        'VgS': '1.25'
#    }
#}
#
#nuisances['VZ'] = {
#    'name': 'CMS_hww_VZScale',
#    'type': 'lnN',
#    'samples': {
#        'VZ': '1.16'
#    }
#}

## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat']  = {
              'type'  : 'auto',
              'maxPoiss'  : '10',
              'includeSignal'  : '1',
              #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
              #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
              'samples' : {}
             }


for n in nuisances.values():
    n['skipCMS'] = 1
