# plot configuration



# groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#
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
                  'nameHR' : 'Non-prompt',
                  'isSignal' : 0,
                  'color': 921,    # kGray + 1
                  #'samples'  : ['Fake']
                  'samples'  : ['Fake_mm','Fake_em']
              }

groupPlot['DY']  = {  
                  'nameHR' : "DY",
                  'isSignal' : 0,
                  'color': 418,    # kGreen+2
                  'samples'  : ['DY']
              }

groupPlot['VVV']  = {  
                  'nameHR' : 'VVV',
                  'isSignal' : 0,
                  'color': 857, # kAzure -3  
                  'samples'  : ['VVV']
              }


groupPlot['ZZ']  = {  
                  'nameHR' : "ZZ",
                  'isSignal' : 0,
                  'color'    : 617,   # kViolet + 1  
                  'samples'  : ['ZZ']
              }

groupPlot['WZ']  = {    
                  'nameHR' : "WZ",
                  'isSignal' : 0,
                  'color'    : 619,   # kViolet + 1  
                  'samples'  : ['WZ']
              }

groupPlot['Vg']  = {  
                  'nameHR' : "V#gamma",
                  'isSignal' : 0,
                  'color'    : 810,   # kOrange + 10
                  'samples'  : ['Wg','Zg']
              }

#groupPlot['Zg']  = {
#                  'nameHR' : "Z#gamma",
#                  'isSignal' : 0,
#                  'color'    : 810,   # kOrange + 10
#                  'samples'  : ['Zg']
#              }


groupPlot['VgS']  = {
                  'nameHR' : "V#gamma*",
                  'isSignal' : 0,
                  'color'    : 412,   # kGreen - 9
                  'samples'  : ['ZgS','WgS']
              }

#groupPlot['WgS']  = {
#                  'nameHR' : "W#gamma*",
#                  'isSignal' : 0,
#                  'color'    : 409,   # kGreen - 9
#                  'samples'  : ['WgS']
#              }

groupPlot['Higgs']  = {  
                  'nameHR' : 'Higgs',
                  'isSignal' : 1,
                  'color': 632, # kRed 
		  'samples'  : ['ZH_hww', 'ggZH_hww', 'WH_hww', 'qqH_hww', 'ggH_hww','WH_htt','ZH_htt','ggH_htt','qqH_htt']
              }


#plot = {}

# keys here must match keys in samples.py    
#     
plot['DY']  = {  
                  'color': 418,    # kGreen+2
                  'isSignal' : 0,
                  'isData'   : 0, 
                  'scale'    : 1.0,
              }


plot['Fake_em']  = {  
                  'color': 921,    # kGray + 1
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0                  
              }

plot['Fake_mm']  = { 
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
                  'color': 850, # kAzure -10
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }


plot['Wg']  = { 
                  'color': 859, # kAzure -1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['Zg']  = {
                  'color': 859, # kAzure -1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['ZgS'] = { 
                  'color'    : 617,   # kViolet + 1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['ZZ']  = { 
                  'color': 858, # kAzure -2  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

plot['WZ']  = {
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

plot['WgS']  = {
                  'color': 617, # kViolet + 1
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

#plot['bbH_htt'] = {
#                  'nameHR' : 'bbHtt',
#                  'color': 632-1, # kRed-1 
#                  'isSignal' : 1,
#                  'isData'   : 0,
#                  'scale'    : 1    #
#                  }
#
#plot['ttH_htt'] = {
#                  'nameHR' : 'bbHtt',
#                  'color': 632-2, # kRed-1 
#                  'isSignal' : 1,
#                  'isData'   : 0,
#                  'scale'    : 1    #
#                  }
#
#
'''
plot['ggZH_htt'] = {
                  'nameHR' : 'ggZHtt',
                  'color': 632+4, # kRed+4
                  'isSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                  }
'''
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

#plot['H_hww'] = {
#                  'nameHR' : 'Hww',
#                  'color': 632, # kRed 
#                  'isSignal' : 1,
#                  'isData'   : 0,    
#                  'scale'    : 1    #
#                  }

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

#plot['bbH_hww'] = {
#                  'nameHR' : 'bbH',
#                  'color': 632+5, # kRed+5 
#                  'isSignal' : 1,
#                  'isData'   : 0,
#                  'scale'    : 1    #
#                  }

#plot['ttH_hww'] = {
#                  'nameHR' : 'ttH',
#                  'color': 632+6, # kRed+6
#                  'isSignal' : 1,
#                  'isData'   : 0,
#                  'scale'    : 1    #
#                  }


# data

plot['DATA']  = { 
                  'nameHR' : 'Data',
                  'color': 1 ,  
                  'isSignal' : 0,
                  'isData'   : 1,
                  'isBlind'  : 0
              }




# additional options

legend['lumi'] = 'L = 41.5/fb'
legend['sqrt'] = '#sqrt{s} = 13 TeV'
plot['ggZH_hww']['cuts'] = {} 
plot['ggZH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = 1.536468 
plot['ZZ']['cuts'] = {} 
plot['ZZ']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = 1.067104 
plot['VVV']['cuts'] = {} 
plot['VVV']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = 1.019388 
plot['ZgS']['cuts'] = {} 
plot['ZgS']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = 0.906711 
plot['WH_htt']['cuts'] = {} 
plot['WH_htt']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = 1.871851 
plot['WH_hww']['cuts'] = {} 
plot['WH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = 1.932374 
plot['WgS']['cuts'] = {} 
plot['WgS']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = 0.945661 
plot['Fake_mm']['cuts'] = {} 
plot['Fake_mm']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = 0.708232 
plot['ZH_htt']['cuts'] = {} 
plot['ZH_htt']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = 1.788981 
plot['WZ']['cuts'] = {} 
plot['WZ']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = 0.926449 
plot['ZH_hww']['cuts'] = {} 
plot['ZH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = 1.891334 
plot['Wg']['cuts'] = {} 
plot['Wg']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 0.771755 
plot['ggH_htt']['cuts'] = {} 
plot['ggH_htt']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 0.996416 
plot['ggWW']['cuts'] = {} 
plot['ggWW']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.060988 
plot['ZgS']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.027273 
plot['WWewk']['cuts'] = {} 
plot['WWewk']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.008759 
plot['ZZ']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.047252 
plot['qqH_hww']['cuts'] = {} 
plot['qqH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 0.853576 
plot['top']['cuts'] = {} 
plot['top']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 0.954551 
plot['VVV']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 0.932808 
plot['ggZH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.906721 
plot['Zg']['cuts'] = {} 
plot['Zg']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.504860 
plot['WH_htt']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.875085 
plot['Fake_em']['cuts'] = {} 
plot['Fake_em']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 0.873545 
plot['WW']['cuts'] = {} 
plot['WW']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.560746 
plot['WH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.987308 
plot['WgS']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 0.935721 
plot['ZH_htt']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.973687 
plot['ggH_hww']['cuts'] = {} 
plot['ggH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.030832 
plot['WZ']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 0.936079 
plot['ZH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.859400 
plot['Wg']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 0.553996 
plot['ggWW']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 1.015681 
plot['ZgS']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 0.538463 
plot['WWewk']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 1.003965 
plot['ZZ']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 1.209617 
plot['top']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 1.037906 
plot['VVV']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 0.986268 
plot['ggZH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 2.020514 
plot['Zg']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 2.185497 
plot['WH_htt']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 2.054866 
plot['Fake_em']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 0.875067 
plot['WW']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 1.003450 
plot['WH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 1.771116 
plot['WgS']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 1.116899 
plot['ZH_htt']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 2.103211 
plot['WZ']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 1.297241 
plot['ZH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 2.094894 
plot['ZZ']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_2j'] = 1.039467 
plot['VVV']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_2j'] = 1.087122 
plot['ggZH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_2j'] = 1.401445 
plot['WH_htt']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_2j'] = 1.961327 
plot['WH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_2j'] = 1.891283 
plot['WgS']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_2j'] = 1.072776 
plot['Fake_mm']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_2j'] = 0.684523 
plot['ZH_htt']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_2j'] = 2.247668 
plot['WZ']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_2j'] = 1.315448 
plot['ZH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_2j'] = 2.195244 
