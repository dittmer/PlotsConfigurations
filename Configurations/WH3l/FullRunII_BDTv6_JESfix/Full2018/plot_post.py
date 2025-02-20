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
                  'samples'  : ['ZH_hww', 'ggZH_hww', 'WH_hww', 'qqH_hww', 'ggH_hww' ,'ttH_hww','WH_htt','ZH_htt','ggH_htt','qqH_htt']
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

plot['ttH_hww'] = {
                  'nameHR' : 'ttH',
                  'color': 632, # kRed 
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


# Htautau

# plot['H_htt'] = {
                  # 'nameHR' : 'Htt',
                  # 'color': 632+4, # kRed+4 
                  # 'isSignal' : 1,
                  # 'isData'   : 0,    
                  # 'scale'    : 1
                  # }

# HWW 

# plot['ZH_hww'] = {
                  # 'nameHR' : 'ZH',
                  # 'color': 632+3, # kRed+3 
                  # 'isSignal' : 1,
                  # 'isData'   : 0,    
                  # 'scale'    : 1
                  # }

##plot['ggZH_hww'] = {
#                  'nameHR' : 'ggZH',
#                  'color': 632+4, # kRed+4
#                  'isSignal' : 1,
#                  'isData'   : 0,    
#                  'scale'    : 1
#                  }

# plot['WH_hww'] = {
                  # 'nameHR' : 'WH',
                  # 'color': 632+2, # kRed+2 
                  # 'isSignal' : 1,
                  # 'isData'   : 0,    
                  # 'scale'    : 1
                  # }

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

legend['lumi'] = 'L = 59.74/fb'
legend['sqrt'] = '#sqrt{s} = 13 TeV'
plot['ZgS']['cuts'] = {} 
plot['ZgS']['cuts']['wh3l_13TeV_ossf'] = 0.673987 
plot['VVV']['cuts'] = {} 
plot['VVV']['cuts']['wh3l_13TeV_ossf'] = 0.906140 
plot['ggZH_hww']['cuts'] = {} 
plot['ggZH_hww']['cuts']['wh3l_13TeV_ossf'] = 1.719661 
plot['Zg']['cuts'] = {} 
plot['Zg']['cuts']['wh3l_13TeV_ossf'] = 0.603340 
plot['WH_htt']['cuts'] = {} 
plot['WH_htt']['cuts']['wh3l_13TeV_ossf'] = 1.816415 
plot['WW']['cuts'] = {} 
plot['WW']['cuts']['wh3l_13TeV_ossf'] = 1.030258 
plot['WH_hww']['cuts'] = {} 
plot['WH_hww']['cuts']['wh3l_13TeV_ossf'] = 1.832968 
plot['ZZ']['cuts'] = {} 
plot['ZZ']['cuts']['wh3l_13TeV_ossf'] = 0.997006 
plot['Fake']['cuts'] = {} 
plot['Fake']['cuts']['wh3l_13TeV_ossf'] = 0.607466 
plot['ttH_hww']['cuts'] = {} 
plot['ttH_hww']['cuts']['wh3l_13TeV_ossf'] = 0.880427 
plot['ZH_htt']['cuts'] = {} 
plot['ZH_htt']['cuts']['wh3l_13TeV_ossf'] = 1.830405 
plot['WZ']['cuts'] = {} 
plot['WZ']['cuts']['wh3l_13TeV_ossf'] = 1.120365 
plot['ZH_hww']['cuts'] = {} 
plot['ZH_hww']['cuts']['wh3l_13TeV_ossf'] = 1.832551 
plot['ZgS']['cuts']['wh3l_zg_13TeV'] = 0.745538 
plot['VVV']['cuts']['wh3l_zg_13TeV'] = 0.969587 
plot['Zg']['cuts']['wh3l_zg_13TeV'] = 0.694859 
plot['WH_htt']['cuts']['wh3l_zg_13TeV'] = 1.828585 
plot['WH_hww']['cuts']['wh3l_zg_13TeV'] = 2.077893 
plot['ZZ']['cuts']['wh3l_zg_13TeV'] = 1.002825 
plot['Fake']['cuts']['wh3l_zg_13TeV'] = 0.812935 
plot['ZH_htt']['cuts']['wh3l_zg_13TeV'] = 1.807816 
plot['WZ']['cuts']['wh3l_zg_13TeV'] = 1.179254 
plot['VVV']['cuts']['wh3l_13TeV_sssf'] = 0.964405 
plot['ggZH_hww']['cuts']['wh3l_13TeV_sssf'] = 1.782593 
plot['WH_htt']['cuts']['wh3l_13TeV_sssf'] = 1.805193 
plot['WH_hww']['cuts']['wh3l_13TeV_sssf'] = 1.769668 
plot['ZZ']['cuts']['wh3l_13TeV_sssf'] = 0.948249 
plot['Fake']['cuts']['wh3l_13TeV_sssf'] = 0.582484 
plot['ttH_hww']['cuts']['wh3l_13TeV_sssf'] = 0.770487 
plot['ZH_htt']['cuts']['wh3l_13TeV_sssf'] = 1.786489 
plot['WZ']['cuts']['wh3l_13TeV_sssf'] = 1.115092 
plot['ZH_hww']['cuts']['wh3l_13TeV_sssf'] = 1.933594 
plot['ZgS']['cuts']['wh3l_wz_13TeV'] = 0.611839 
plot['VVV']['cuts']['wh3l_wz_13TeV'] = 1.035287 
plot['ggZH_hww']['cuts']['wh3l_wz_13TeV'] = 1.837909 
plot['Zg']['cuts']['wh3l_wz_13TeV'] = 0.744398 
plot['WH_htt']['cuts']['wh3l_wz_13TeV'] = 1.797929 
plot['WH_hww']['cuts']['wh3l_wz_13TeV'] = 1.846773 
plot['ZZ']['cuts']['wh3l_wz_13TeV'] = 1.002901 
plot['Fake']['cuts']['wh3l_wz_13TeV'] = 0.673570 
plot['ttH_hww']['cuts']['wh3l_wz_13TeV'] = 1.038351 
plot['ZH_htt']['cuts']['wh3l_wz_13TeV'] = 1.770594 
plot['WZ']['cuts']['wh3l_wz_13TeV'] = 1.125956 
plot['ZH_hww']['cuts']['wh3l_wz_13TeV'] = 1.753284 
