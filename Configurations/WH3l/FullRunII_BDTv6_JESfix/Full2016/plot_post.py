# plot configuration
# groupPlot = {}
 
# Groups of samples to improve the plots.
# If not defined, normal plots is used


#groupPlot['DY']  = {  
#                  'nameHR' : "DY",
#                  'isSignal' : 0,
#                  'color': 418,    # kGreen+2
#                  'samples'  : ['DY']
#              }

groupPlot['Fake']  = {  
                  'nameHR' : 'Non-prompt',
                  'isSignal' : 0,
                  'color': 921,    # kGray + 1
                  'samples'  : ['Fake']
              }

#groupPlot['top']  = {  
#                  'nameHR' : 'tW and t#bart',
#                  'isSignal' : 0,
#                  'color': 921,   # kYellow
#                  'samples'  : ['top']
#              }

groupPlot['WW']  = {  
                  'nameHR' : 'WW',
                  'isSignal' : 0,
                  'color': 851, # kAzure -9 
                  'samples'  : ['WW']
              }

groupPlot['VVV']  = {  
                  'nameHR' : 'VVV',
                  'isSignal' : 0,
                  'color': 857, # kAzure -3  
                  'samples'  : ['VVV']
              }


groupPlot['Zg']  = {
                  'nameHR' : 'Zg',
                  'color': 859, # kAzure -1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0,
                  'samples'  : ['Zg']
                  }

groupPlot['ZgS']  = {
                  'nameHR' : "Z#gamma*",
                  'color'    : 409,   # kGreen - 9
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0,
                  'samples'  : ['ZgS']
              }
groupPlot['Wg']  = {
                  'nameHR' : 'Wg',
                  'color': 635,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0,
                  'samples'  : ['Wg']
                  }

groupPlot['WgS']  = {
                  'nameHR' : "W#gamma*",
                  'color'    : 636,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0,
                  'samples'  : ['WgS']
              }
# groupPlot['Vg']  = {
                  # 'nameHR' : 'Vg',
                  # 'color': 859, # kAzure -1  
                  # 'isSignal' : 0,
                  # 'isData'   : 0,
                  # 'scale'    : 1.0,
                  # 'samples'  : ['Vg']
                  # }

# groupPlot['VgS']  = {
                  # 'nameHR' : "V#gamma*",
                  # 'color'    : 409,   # kGreen - 9
                  # 'isSignal' : 0,
                  # 'isData'   : 0,
                  # 'scale'    : 1.0,
                  # 'samples'  : ['VgS']
              # }

groupPlot['ZZ']  = {
                  'nameHR' : "ZZ",
                  'isSignal' : 0,
                  'color'    : 617,   # kViolet + 1  
          #        'samples'  : ['ZZ', 'ggZZ_tt', 'ggZZ_em', 'ggZZ_ee', 'ggZZ_mm']
                  'samples'  : ['ZZ']
              }

groupPlot['WZ']  = {
                  'nameHR' : "WZ",
                  'isSignal' : 0,
                  'color'    : 400,   # Yellow
                  'samples'  : ['WZ']
              }

groupPlot['Higgs']  = {  
                  'nameHR' : 'Higgs',
                  'isSignal' : 1,
                  'color': 632, # kRed 
          'samples'  : ['ZH_hww', 'ggZH_hww', 'WH_hww', 'qqH_hww', 'ggH_hww','WH_htt','ZH_htt','ggH_htt','qqH_htt']
              }
# groupPlot['Higgs']  = {  
                  # 'nameHR' : 'Higgs',
                  # 'isSignal' : 1,
                  # 'color': 632, # kRed 
                  # 'samples'  : ['H_htt', 'WH_hww', 'ZH_hww']
              # }

#plot = {}
               
plot['Fake']  = {  
                  'color': 921,    # kGray + 1
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0                  
              }


plot['VVV']  = {
                  'color': 851, # kAzure -9 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1.0
                  }

plot['WW']  = {
                  'color': 850, # kAzure -10
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1.0
                  }


# plot['Vg']  = { 
                  # 'nameHR' : 'Zg',
                  # 'color': 859, # kAzure -1  
                  # 'isSignal' : 0,
                  # 'isData'   : 0,
                  # 'scale'    : 1.0
                  # }

# plot['VgS'] = { 
                 # 'color'    : 617,   # kViolet + 1  
                 # 'isSignal' : 0,
                 # 'isData'   : 0,
                 # 'scale'    : 1.0
                 # }

plot['Zg']  = {
                  'nameHR' : 'Zg',
                  'color': 859, # kAzure -1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0

                  }

plot['ZgS']  = {
                  'nameHR' : "Z#gamma*",
                  'color'    : 409,   # kGreen - 9
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
              }
plot['Wg']  = {
                  'nameHR' : 'Wg',
                  'color': 635,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['WgS']  = {
                  'nameHR' : "W#gamma*",
                  'color'    : 636,
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
              }
plot['WZ']  = { 
                  'nameHR' : 'WZ',
                  'color': 858, # kAzure -2  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['ZZ']  = { 
                  'nameHR' : 'ZZ',
                  'color': 856, # kAzure -4  
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

# Htautau

# plot['H_htt'] = {
                  # 'nameHR' : 'Htt',
                  # 'color': 632+4, # kRed+4 
                  # 'isSignal' : 1,
                  # 'isData'   : 0,    
                  # 'scale'    : 1
                  # }

# Htautau
plot['ZH_htt'] = {
                  'nameHR' : 'ZHtt',
                  'color': 632+3, # kRed+3 
                  'isSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

plot['WH_htt'] = {
                  'nameHR' : 'WHtt',
                  'color': 632+2, # kRed+2 
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


plot['ggH_htt'] = {
                  'nameHR' : 'ggHtt',
                  'color': 632, # kRed 
                  'isSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

# HWW 
plot['ZH_hww'] = {
                  'nameHR' : 'ZH',
                  'color': 632+3, # kRed+3 
                  'isSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

plot['ggZH_hww'] = {
                  'nameHR' : 'ggZH',
                  'color': 632+4, # kRed+4
                  'isSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }

plot['WH_hww'] = {
                  'nameHR' : 'WH',
                  'color': 632+2, # kRed+2 
                  'isSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }


plot['qqH_hww'] = {
                  'nameHR' : 'qqH',
                  'color': 632+1, # kRed+1 
                  'isSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }


plot['ggH_hww'] = {
                  'nameHR' : 'ggH',
                  'color': 632, # kRed 
                  'isSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }


# data

plot['DATA']  = { 
                  'nameHR' : 'Data',
                  'color': 1 ,  
                  'isSignal' : 0,
                  'isData'   : 1 ,
                  'isBlind'  : 0
                  # 'isBlind'  : 1
              }

# additional options

legend['lumi'] = 'L = 35.87/fb'
legend['sqrt'] = '#sqrt{s} = 13 TeV'
plot['ZgS']['cuts'] = {} 
plot['ZgS']['cuts']['wh3l_13TeV_ossf'] = 0.630926 
plot['VVV']['cuts'] = {} 
plot['VVV']['cuts']['wh3l_13TeV_ossf'] = 1.069267 
plot['ggZH_hww']['cuts'] = {} 
plot['ggZH_hww']['cuts']['wh3l_13TeV_ossf'] = 2.011433 
plot['Zg']['cuts'] = {} 
plot['Zg']['cuts']['wh3l_13TeV_ossf'] = 0.794441 
plot['WH_htt']['cuts'] = {} 
plot['WH_htt']['cuts']['wh3l_13TeV_ossf'] = 1.965561 
plot['WH_hww']['cuts'] = {} 
plot['WH_hww']['cuts']['wh3l_13TeV_ossf'] = 1.944626 
plot['ZZ']['cuts'] = {} 
plot['ZZ']['cuts']['wh3l_13TeV_ossf'] = 1.071823 
plot['Fake']['cuts'] = {} 
plot['Fake']['cuts']['wh3l_13TeV_ossf'] = 0.732153 
plot['ZH_htt']['cuts'] = {} 
plot['ZH_htt']['cuts']['wh3l_13TeV_ossf'] = 1.828392 
plot['WZ']['cuts'] = {} 
plot['WZ']['cuts']['wh3l_13TeV_ossf'] = 1.335235 
plot['ZH_hww']['cuts'] = {} 
plot['ZH_hww']['cuts']['wh3l_13TeV_ossf'] = 1.799339 
plot['ZH_htt']['cuts']['wh3l_zg_13TeV'] = 1.885810 
plot['Zg']['cuts']['wh3l_zg_13TeV'] = 0.680277 
plot['ZgS']['cuts']['wh3l_zg_13TeV'] = 0.668092 
plot['ZZ']['cuts']['wh3l_zg_13TeV'] = 1.046328 
plot['Fake']['cuts']['wh3l_zg_13TeV'] = 0.703724 
plot['VVV']['cuts']['wh3l_13TeV_sssf'] = 1.142401 
plot['ggZH_hww']['cuts']['wh3l_13TeV_sssf'] = 1.939910 
plot['WH_htt']['cuts']['wh3l_13TeV_sssf'] = 1.868102 
plot['WH_hww']['cuts']['wh3l_13TeV_sssf'] = 1.854788 
plot['ZZ']['cuts']['wh3l_13TeV_sssf'] = 0.992661 
plot['Fake']['cuts']['wh3l_13TeV_sssf'] = 0.709263 
plot['ZH_htt']['cuts']['wh3l_13TeV_sssf'] = 1.846055 
plot['WZ']['cuts']['wh3l_13TeV_sssf'] = 0.785641 
plot['ZH_hww']['cuts']['wh3l_13TeV_sssf'] = 1.865649 
plot['ggZH_hww']['cuts']['wh3l_wz_13TeV'] = 1.906347 
plot['VVV']['cuts']['wh3l_wz_13TeV'] = 0.990380 
plot['Zg']['cuts']['wh3l_wz_13TeV'] = 0.765158 
plot['WH_htt']['cuts']['wh3l_wz_13TeV'] = 1.894092 
plot['WH_hww']['cuts']['wh3l_wz_13TeV'] = 1.902740 
plot['ZZ']['cuts']['wh3l_wz_13TeV'] = 1.029112 
plot['Fake']['cuts']['wh3l_wz_13TeV'] = 0.714322 
plot['ZH_htt']['cuts']['wh3l_wz_13TeV'] = 1.822455 
plot['WZ']['cuts']['wh3l_wz_13TeV'] = 1.166936 
plot['ZH_hww']['cuts']['wh3l_wz_13TeV'] = 1.859158 
