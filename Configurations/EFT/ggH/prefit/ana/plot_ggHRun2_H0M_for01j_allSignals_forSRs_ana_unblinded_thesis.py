# plot configuration



groupPlot = OrderedDict()
plot = {}

# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#

plot['DATA']  = {
                  'nameHR' : 'Data',
                  'color': 1 ,
                  'isSignal' : 0,
                  'isData'   : 1 ,
                  'isBlind'  : 0
              }

groupPlot['top']  = {
                  'nameHR' : 'tW and t#bar{t}',
                  'isSignal' : 0,
                  'color': 400,   # kYellow
                  'samples'  : ['top']
              }

groupPlot['WW']  = {
                  'nameHR' : 'WW',
                  'isSignal' : 0,
                  'color': 851, # kAzure -9 
                  'samples'  : ['WW', 'ggWW', 'WWewk']
              }

groupPlot['Fake']  = {
                  'nameHR' : 'Nonprompt',
                  'isSignal' : 0,
                  'color': 921,    # kGray + 1
                  'samples'  : ['Fake']
              }
groupPlot['DY']  = {
                  'nameHR' : "DY",
                  'isSignal' : 0,
                  'color': 418,    # kGreen+2
                  'samples'  : ['DY','Dyemb']
              }
groupPlot['VV']  = {
                  'nameHR' : 'Multiboson',
                  'isSignal' : 0,
                  'color': 857,   # kViolet +1
                  'samples'  : ['VZ', 'Vg', 'VgS_L', 'VgS_H', 'VVV']
              }
bsm = "H0M"
factors = { 'H0PH' : "1.", 'H0M' : "1.", "H0L1" : "0.5", "H0LZg" : "0.5" }
groupPlot['SM']  = {
                  'nameHR' : 'Higgs (SM)',
                  'isSignal' : 1,
                  'color': 2,
                  'scale': 1.,
                  'samples'  : ['ggH_T1','VBF_T1','WH_T1','ZH_T1']
              }
groupPlot['BSM']  = {
                  'nameHR' : 'Higgs (a_{3})',
                  'isSignal' : 2,
                  'color': 4,
                  'scale': 1.,
                  'samples'  : ['ggH_T3','WH_T5','ZH_T5','VBF_T5']
              }
####### individual samples ###########
#ggF
plot['ggH_T1']  = {
                      'nameHR' : 'ggH SM',
                      'color' : 851,
                      'isSignal' : 1,
                      'isData'   : 0,
                      'scale'    : 1,
                    }
plot['ggH_T3']  = {
                      'nameHR' : 'ggH T3',
                      'color' : 851,
                      'isSignal' : 2,
                      'isData'   : 0,
                      'scale'    : 1.,
                    }

# VBF
plot['VBF_T1']  = {
                      'nameHR' : 'VBF SM',
                      'color' : 851,
                      'isSignal' : 1,
                      'isData'   : 0,
                      'scale'    : 1,
                    }

plot['VBF_T5']  = {
                      'nameHR' : 'VBF INT22',
                      'color' : 409,
                      'isSignal' : 2,
                      'isData'   : 0,
                      'scale'    : 1.,
                    }
# WH

plot['WH_T1']  = {
                      'nameHR' : 'WH SM',
                      'color' : 851,
                      'isSignal' : 1,
                      'isData'   : 0,
                      'scale'    : 1,
                    }
plot['WH_T5']  = {
                      'nameHR' : 'WH T5',
                      'color' : 851,
                      'isSignal' : 2,
                      'isData'   : 0,
                      'scale'    : 1.,
                    }
#ZH
plot['ZH_T1']  = {
                      'nameHR' : 'ZH SM',
                      'color' : 851,
                      'isSignal' : 1,
                      'isData'   : 0,
                      'scale'    : 1,
                    }
plot['ZH_T5']  = {
                      'nameHR' : 'ZH INT22',
                      'color' : 409,
                      'isSignal' : 2,
                      'isData'   : 0,
                      'scale'    : 1.,
                    }
#other
'''
plot['ttH_hww'] = {plot_combined_Hgg_2017.py
                  'nameHR' : 'ttH',
                  'color': 632+6, # kRed+6
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1    #
                  }
'''
#SM backgrounds 
plot['DY']  = {  
                  'color': 418,    # kGreen+2
                  'isSignal' : 0,
                  'isData'   : 0, 
                  'scale'    : 1.0,
              }

plot['Dyemb']  = {  
                  'color': 418,    # kGreen+2
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0,
              }


plot['Fake']  = {  
                  'color': 921,    # kGray + 1
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0                  
              }
              
plot['top'] = {   
                  'nameHR' : 'tW and t#bar{t}',
                  'color': 400,   # kYellow
                  'isSignal' : 0,
                  'isData'   : 0, 
                  'scale'    : 1.0,
                  }

plot['WW']  = {
                  'color': 851, # kAzure -9 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
                  }

plot['ggWW']  = {
                  'color': 850, # kAzure -10
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1.0
                  }

plot['WWewk']  = {
                  'color': 851, # kAzure -9 
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
                  }

plot['Vg']  = { 
                  'color': 859, # kAzure -1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['VgS_L'] = { 
                  'color'    : 617,   # kViolet + 1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['VgS_H'] = {
                  'color'    : 617,   # kViolet + 1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['VZ']  = { 
                  'color': 858, # kAzure -2  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['VVV']  = { 
                  'color': 857, # kAzure -3  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

# Htautau as background
'''
plot['ggH_htt'] = {
                  'nameHR' : 'ggHtt',
                  'color': 632+4, # kRed+4 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

plot['WH_htt'] = {
                  'nameHR' : 'WHtt',
                  'color': 632+2, # kRed+2 
                  'plot_combined_Hgg_2017.pyisSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

plot['ZH_htt'] = {
                  'nameHR' : 'ZHtt',
                  'color': 632+3, # kRed+3 
                  'isSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

plot['qqH_htt'] = {
                  'nameHR' : 'qqHtt',
                  'color': 632+1, # kRed+1 
                  'isSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }
'''

#original SM MC signals - not used
'''
plot['ZH_hww'] = {
                  'nameHR' : 'ZH',
                  'color': 632+3, # kRed+3 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

plot['ggZH_hww'] = {
                  'nameHR' : 'ggZH',
                  'color': 632+4, # kRed+4
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

plot['WH_hww'] = {
                  'nameHR' : 'WH',
                  'color': 632+2, # kRed+2 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }


plot['qqH_hww'] = {
                  'nameHR' : 'qqH',
                  'color': 632+1, # kRed+1 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }


plot['ggH_hww'] = {
                  'nameHR' : 'ggH',
                  'color': 632, # kRed 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }
'''
# additional options
legend = {}
legend['lumi'] = 'L = 138 fb^{-1}'
legend['sqrt'] = '(13 TeV)'

#comboPlot['SMvsALT'] = {
#                      'groups' : ['H0PM','H0PH','H0M','H0L1']
#}

