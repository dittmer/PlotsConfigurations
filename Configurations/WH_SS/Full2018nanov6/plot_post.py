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

legend['lumi'] = 'L = 59.74/fb'
legend['sqrt'] = '#sqrt{s} = 13 TeV'
plot['ZZ']['cuts'] = {} 
plot['ZZ']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = 1.109526 
plot['VVV']['cuts'] = {} 
plot['VVV']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = 0.982669 
plot['top']['cuts'] = {} 
plot['top']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = 1.104237 
plot['ggZH_hww']['cuts'] = {} 
plot['ggZH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = 2.005411 
plot['WH_htt']['cuts'] = {} 
plot['WH_htt']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = 1.910640 
plot['WH_hww']['cuts'] = {} 
plot['WH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = 1.930684 
plot['WgS']['cuts'] = {} 
plot['WgS']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = 0.959174 
plot['Fake_mm']['cuts'] = {} 
plot['Fake_mm']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = 0.530780 
plot['ZH_htt']['cuts'] = {} 
plot['ZH_htt']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = 2.031620 
plot['WZ']['cuts'] = {} 
plot['WZ']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = 0.955819 
plot['ZH_hww']['cuts'] = {} 
plot['ZH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_1j'] = 1.683910 
plot['Wg']['cuts'] = {} 
plot['Wg']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 0.980289 
plot['ggH_htt']['cuts'] = {} 
plot['ggH_htt']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 0.843159 
plot['ggWW']['cuts'] = {} 
plot['ggWW']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.356440 
plot['ZgS']['cuts'] = {} 
plot['ZgS']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.022938 
plot['WWewk']['cuts'] = {} 
plot['WWewk']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.004082 
plot['ZZ']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.062201 
plot['qqH_hww']['cuts'] = {} 
plot['qqH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.009114 
plot['top']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 0.987496 
plot['VVV']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 0.934823 
plot['ggZH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.963692 
plot['Zg']['cuts'] = {} 
plot['Zg']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.015286 
plot['WH_htt']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.927263 
plot['Fake_em']['cuts'] = {} 
plot['Fake_em']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 0.802038 
plot['WW']['cuts'] = {} 
plot['WW']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.075830 
plot['WH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.934156 
plot['WgS']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 0.889324 
plot['ZH_htt']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.885308 
plot['ggH_hww']['cuts'] = {} 
plot['ggH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 0.961038 
plot['WZ']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 0.940623 
plot['ZH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_1j'] = 1.945348 
plot['ggH_htt']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 1.045120 
plot['ggWW']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 1.019821 
plot['ZgS']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 0.970884 
plot['ZZ']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 0.995973 
plot['top']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 1.024818 
plot['VVV']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 0.941396 
plot['ggZH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 1.879144 
plot['Zg']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 1.166832 
plot['WH_htt']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 1.767613 
plot['Fake_em']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 0.695783 
plot['WW']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 0.709283 
plot['WH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 1.774357 
plot['WgS']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 0.880194 
plot['ZH_htt']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 1.772452 
plot['WZ']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 1.131596 
plot['ZH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_eu_2j'] = 1.538528 
plot['ZZ']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_2j'] = 1.100468 
plot['VVV']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_2j'] = 0.916561 
plot['ggZH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_2j'] = 1.539109 
plot['WH_htt']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_2j'] = 1.762801 
plot['WH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_2j'] = 1.777673 
plot['WgS']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_2j'] = 0.937048 
plot['Fake_mm']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_2j'] = 0.448579 
plot['ZH_htt']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_2j'] = 1.854204 
plot['WZ']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_2j'] = 1.147403 
plot['ZH_hww']['cuts']['hww2l2v_13TeV_of2j_WH_SS_uu_2j'] = 1.859243 
