# plot configuration



# groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#
'''
groupPlot['top']  = {  
                  'nameHR' : 'tW and t#bar{t}',
                  'isSignal' : 0,
                  'color': 401,   # kYellow
                  'samples'  : ['top']
              }
'''
groupPlot['ttV']  = {  
                  'nameHR' : 'ttV',
                  'isSignal' : 0,
                  'color': 418,    # kGreen+3
                  'samples'  : ['ttW','ttZ']
              }
'''
groupPlot['WW']  = {  
                  'nameHR' : 'WW',
                  'isSignal' : 0,
                  'color': 431, # kAzure -9 
                  'samples'  : ['WW','WWewk']
              }

groupPlot['DY']  = {  
                  'nameHR' : "DY",
                  'isSignal' : 0,
                  'color': 635,    # kGreen+2
                  'samples'  : ['DY']
              }
'''


groupPlot['VVV']  = {  
                  'nameHR' : 'VVV',
                  'isSignal' : 0,
                  'color': 618, # kAzure -3  
                  'samples'  : ['VVV','WWW']
              }

'''
groupPlot['VZ']  = {  
                  'nameHR' : "VZ",
                  'isSignal' : 0,
                  'color'    :603,   # kViolet + 1  
                  'samples'  : ['VZ', 'WZ']
              }
'''
groupPlot['ZZ']  = {
                  'nameHR' : "ZZ",
                  'isSignal' : 0,
                  'color'    : 857,   # kViolet + 1  
                  'samples'  : ['ZZ']
              }
'''
groupPlot['ggZZ']  = {
                  'nameHR' : "ggZZ",
                  'isSignal' : 0,
                  'color'    : 635,     
                  'samples'  : ['ggZZ']
              }
'''
'''
groupPlot['Vg']  = {  
                  'nameHR' : "V#gamma",
                  'isSignal' : 0,
                  'color'    : 922,   # kOrange + 10
                  'samples'  : ['Vg', 'Wg']
              }
'''


groupPlot['ZH4l']  = {  
                  'nameHR' : 'Higgs',
                  'isSignal' : 1,
                  'color': 632, # kRed 
		  'samples'  : ['ZH_hww','ggZH_hww','WH_hww','qqH_hww','ggH_hww','ZH_htt', 'WH_htt', 'qqH_htt', 'ggH_htt']
              }





#plot = {}

# keys here must match keys in samples.py    
#  
'''                  
plot['DY']  = {  
                  'color': 418,    # kGreen+2
                  'isSignal' : 0,
                  'isData'   : 0, 
                  'scale'    : 1.0,
                  #'cuts'  : {
                       #'hww2l2v_13TeV_of0j'      : 0.95 ,
                       #'hww2l2v_13TeV_top_of0j'  : 0.95 , 
                       #'hww2l2v_13TeV_dytt_of0j' : 0.95 ,
                       #'hww2l2v_13TeV_em_0j'     : 0.95 , 
                       #'hww2l2v_13TeV_me_0j'     : 0.95 , 
                       ##
                       #'hww2l2v_13TeV_of1j'      : 1.08 ,
                       #'hww2l2v_13TeV_top_of1j'  : 1.08 , 
                       #'hww2l2v_13TeV_dytt_of1j' : 1.08 ,
                       #'hww2l2v_13TeV_em_1j'     : 1.08 , 
                       #'hww2l2v_13TeV_me_1j'     : 1.08 , 
                        #},

              }
'''
plot['ttZ']  = {
                  'color': 419,    # kGreen+3
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
                  }

plot['ttW']  = {
                  'color': 419,    # kGreen+3
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
                  }

              
'''           
plot['top'] = {   
                  'nameHR' : 'tW and t#bar{t}',
                  'color': 401,   # kYellow
                  'isSignal' : 0,
                  'isData'   : 0, 
                  'scale'    : 1.0,
                  #'cuts'  : {
                       #'hww2l2v_13TeV_of0j'      : 0.94 ,
                       #'hww2l2v_13TeV_top_of0j'  : 0.94 , 
                       #'hww2l2v_13TeV_dytt_of0j' : 0.94 ,
                       #'hww2l2v_13TeV_em_0j'     : 0.94 , 
                       #'hww2l2v_13TeV_me_0j'     : 0.94 , 
                       ##
                       #'hww2l2v_13TeV_of1j'      : 0.86 ,
                       #'hww2l2v_13TeV_top_of1j'  : 0.86 , 
                       #'hww2l2v_13TeV_dytt_of1j' : 0.86 ,
                       #'hww2l2v_13TeV_em_1j'     : 0.86 , 
                       #'hww2l2v_13TeV_me_1j'     : 0.86 , 
                        #},
                  }
'''
'''
plot['WW']  = {
                  'color': 419, # kAzure -9 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
                  }
'''
plot['ggWW']  = {
                  'color': 851, # kAzure -10
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

'''
plot['Vg']  = { 
                  'color': 922, # kAzure -1  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

#plot['VgS'] = { 
#                  'color'    : 617,   # kViolet + 1  
#                  'isSignal' : 0,
#                  'isData'   : 0,
#                  'scale'    : 1.0
#                  }
#
plot['VZ']  = { 
                  'color': 612, # kAzure -2  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }
'''
plot['ZZ']  = {
                  'color': 857, # kAzure -2  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.11
                  }
'''
plot['ggZZ']  = {
                  'color':  635, # kAzure -2  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

'''
plot['VVV']  = { 
                  'color': 618, # kAzure -3  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }

# Htautau

#plot['H_htt'] = {
#                  'nameHR' : 'Htt',
#                  'color': 632+4, # kRed+4 
#                  'isSignal' : 1,
#                  'isData'   : 0,    
#                  'scale'    : 1    #
#                  }

#
plot['ZH_htt'] = {
                  'nameHR' : 'ZHtt',
                  'color': 632+3, # kRed+3 
                  'isSignal' : 1,
                  'isData'   : 0,    
                  'scale'    : 1    #
                 }
##
###plot['bbH_htt'] = {
###                  'nameHR' : 'bbHtt',
###                  'color': 632-1, # kRed-1 
###                  'isSignal' : 1,
###                  'isData'   : 0,
###                  'scale'    : 1    #
###                  }
###
###plot['ttH_htt'] = {
###                  'nameHR' : 'bbHtt',
###                  'color': 632-2, # kRed-1 
###                  'isSignal' : 1,
###                  'isData'   : 0,
###                  'scale'    : 1    #
###                  }
###
###
#plot['ggZH_htt'] = {
#                  'nameHR' : 'ggZHtt',
#                  'color': 632+4, # kRed+4
#                  'isSignal' : 1,
#                  'isData'   : 0,    
#                  'scale'    : 1    #
#                  }
###
plot['WH_htt'] = {
                  'nameHR' : 'WHtt',
                  'color': 632+2, # kRed+2 
                 'isSignal' : 1,
                 'isData'   : 0,    
                  'scale'    : 1    #
                  }

###
plot['qqH_htt'] = {
                  'nameHR' : 'qqHtt',
                  'color': 632+1, # kRed+1 
                  'isSignal' : 1,
                 'isData'   : 0,    
                  'scale'    : 1    #
                  }
##
###
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




plot['ttZ']['cuts'] = {} 
plot['ttZ']['cuts']['zh4l_ZZ_13TeV'] = 0.880052 
plot['VVV']['cuts'] = {} 
plot['VVV']['cuts']['zh4l_ZZ_13TeV'] = 0.975472 
plot['ggZH_hww']['cuts'] = {} 
plot['ggZH_hww']['cuts']['zh4l_ZZ_13TeV'] = 1.743488 
plot['ZZ']['cuts'] = {} 
plot['ZZ']['cuts']['zh4l_ZZ_13TeV'] = 1.094544 
plot['ZH_htt']['cuts'] = {} 
plot['ZH_htt']['cuts']['zh4l_ZZ_13TeV'] = 1.806566 
plot['ZH_hww']['cuts'] = {} 
plot['ZH_hww']['cuts']['zh4l_ZZ_13TeV'] = 1.799761 
plot['ttZ']['cuts']['zh4l_XDF_13TeV'] = 1.022187 
plot['VVV']['cuts']['zh4l_XDF_13TeV'] = 1.005436 
plot['ggZH_hww']['cuts']['zh4l_XDF_13TeV'] = 1.887008 
plot['ZZ']['cuts']['zh4l_XDF_13TeV'] = 1.112607 
plot['ZH_htt']['cuts']['zh4l_XDF_13TeV'] = 1.874365 
plot['ZH_hww']['cuts']['zh4l_XDF_13TeV'] = 1.842777 
plot['ttZ']['cuts']['zh4l_XSF_13TeV'] = 0.986580 
plot['VVV']['cuts']['zh4l_XSF_13TeV'] = 0.974604 
plot['ggZH_hww']['cuts']['zh4l_XSF_13TeV'] = 1.862341 
plot['ZZ']['cuts']['zh4l_XSF_13TeV'] = 1.137039 
plot['ZH_htt']['cuts']['zh4l_XSF_13TeV'] = 1.868498 
plot['ZH_hww']['cuts']['zh4l_XSF_13TeV'] = 1.804618 
