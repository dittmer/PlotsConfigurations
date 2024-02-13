# variables

#variables = {}

# 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
    
variables['events'] = {
    'name'  : '1',      
    'range' : (1,0,2),  
    'xaxis' : 'events', 
    'fold'  : 3
}

# 1 jet binning
variables['mlljj20_whss_1j_bin'] = {
    'name'  : 'mlljj20_whss',
    'range' : ([60.,70.,80.,90.,100.,110.,120.,130.,140.,150.,160.,170.,180.,190.,200.,250.,300.],),
    'xaxis' : 'mlljj20_whss [GeV]',
    'fold'  : 3
}

# 2 jets binning
variables['mlljj20_whss_2j_bin'] = {
    'name'  : 'mlljj20_whss',
    'range' : ([60.,120.,130.,140.,150.,160.,170.,180.,190.,200.,250.,300.],),
    'xaxis' : 'mlljj20_whss [GeV]',
    'fold'  : 3
}

########################################################
# Default BDT training but with TopSemileptonic as fakes
########################################################

variables['BDTG6_TT'] = {
    'name'     : 'BDT_WHSS_TopSemileptonic_v9',     
    'range'    : (40,-1,1),   
    'doWeight' : 1,
    'binX'     : 1,
    'binY'     : 40,
    'xaxis'    : 'BDT discriminant',
    'yaxis'    : 'Events',
    'fold'     : 3
}

variables['BDTG6_TT_100_bins'] = {
    'name'  : 'BDT_WHSS_TopSemileptonic_v9',     
    'range' : (100,-1,1),   
    'xaxis' : 'BDT discriminant',
    'fold'  : 3
}

##########################################################
# BDT training with TopSemileptonic as fakes and weights
##########################################################

variables['BDTG5_TT_weight'] = {
    'name'     : 'BDT_WHSS_TopSemileptonic_weight_v9',     
    'range'    : (40,-1,1),   
    'doWeight' : 1,
    'binX'     : 1,
    'binY'     : 40,
    'xaxis'    : 'BDT discriminant',
    'yaxis'    : 'Events',
    'fold'     : 3
}

variables['BDTG5_TT_weight_100_bins'] = {
    'name'  : 'BDT_WHSS_TopSemileptonic_weight_v9',
    'range' : (100,-1,1),   
    'xaxis' : 'BDT discriminant',
    'fold'  : 3
}

########################################################
# BDT training with TopSemileptonic as fakes and weights
# Training using the 4 eras of Run 2 merged
########################################################

variables['BDTG5_TT_weight_FullRun2'] = {
    'name'     : 'BDT_WHSS_TopSemileptonic_weight_FullRun2_v9',
    'range'    : (40,-1,1),   
    'doWeight' : 1,
    'binX'     : 1,
    'binY'     : 40,
    'xaxis'    : 'BDT discriminant',
    'fold'     : 3
}

variables['BDTG5_TT_weight_FullRun2_100_bins'] = {
    'name'  : 'BDT_WHSS_TopSemileptonic_weight_FullRun2_v9',
    'range' : (100,-1,1),   
    'xaxis' : 'BDT discriminant',
    'fold'  : 3
}

###################
# Control variables
###################

variables['puppimet'] = {
    'name'  : 'PuppiMET_pt',    
    'range' : (20,0,200),
    'xaxis' : 'PUPPI met [GeV]',
    'fold'  : 3
}

variables['mll'] = {
    'name'  : 'mll',
    'range' : (20, 40,120),
    'xaxis' : 'm_{ll} [GeV]',
    'fold'  : 0
}

variables['ptll'] = {
    'name'  : 'ptll',     
    'range' : (40, 0,200),   
    'xaxis' : 'p_{T}^{ll} [GeV]',
    'fold'  : 0
}

variables['pt1'] = {
    'name'  : 'Lepton_pt[0]',     
    'range' : (30,0,150),   
    'xaxis' : 'p_{T} 1st lep',
    'fold'  : 0                         
}

variables['pt2'] = {
    'name'  : 'Lepton_pt[1]',     
    'range' : (20,0,100),   
    'xaxis' : 'p_{T} 2nd lep',
    'fold'  : 3                         
}

variables['mlljj20_whss_bin2'] = {
    'name'  : 'mlljj20_whss',
    'range' : ([60.,100.,110.,120.,130.,140.,150.,160.,170.,180.,190.,200.,250.,300.],),
    'xaxis' : 'mlljj20_whss [GeV]',
    'fold'  : 3
}

variables['detall']  = {  
    'name'  : 'abs(Lepton_eta[0] - Lepton_eta[1])',
    'range' : (20,0.,10.),
    'xaxis' : 'detall',
    'fold'  : 3
}

variables['mth']  = {  
    'name'  : 'mth',
    'range' : (40,0,200),
    'xaxis' : 'm_{T}^{H} [GeV]',
    'fold'  : 0
}

variables['dphill']  = {  
    'name'  : 'abs(dphill)',     
    'range' : (20,0,3.14),   
    'xaxis' : '#Delta#phi_{ll}',
    'fold'  : 3
}

variables['eta1']  = {
    'name'  : 'Lepton_eta[0]',     
    'range' : (40,-3,3),   
    'xaxis' : '#eta 1st lep',
    'fold'  : 3                         
}

variables['eta2']  = {
    'name'  : 'Lepton_eta[1]',     
    'range' : (40,-3,3),   
    'xaxis' : '#eta 2nd lep',
    'fold'  : 3                         
}

variables['jetpt1']  = {
    'name'  : 'CleanJet_pt[0]*(CleanJet_pt[0]>30)',     
    'range' : (40,0,200),   
    'xaxis' : 'p_{T} 1st jet',
    'fold'  : 2   
}

variables['jetpt2'] = {
    'name'  : 'CleanJet_pt[1]*(CleanJet_pt[1]>30)',     
    'range' : (40,0,200),   
    'xaxis' : 'p_{T} 2nd jet',
    'fold'  : 0
}

variables['mjj'] = {
    'name'  : 'mjj*(CleanJet_pt[1]>30)',
    'range' : (50,0,400),
    'xaxis' : 'm_{jj} [GeV]',
    'fold'  : 3
}

variables['mtw1'] = {
    'name'  : 'mtw1',
    'range' : (40,0,200),
    'xaxis' : 'm_{T}^{W_{1}} [GeV]',
    'fold'  : 3
}

variables['mtw2'] = {
    'name'  : 'mtw2',
    'range' : (40,0,200),
    'xaxis' : 'm_{T}^{W_{2}} [GeV]',
    'fold'  : 3
}

variables['dphilljet'] = {
    'name'  : 'dphilljet',
    'range' : (20,0,3.2),
    'xaxis' : 'dphilljet',
    'fold'  : 3
}

variables['dphilljetjet'] = {
    'name'  : 'dphilljetjet*(CleanJet_pt[1]>30)',
    'range' : (20,0,3.2),
    'xaxis' : 'dphilljetjet',
    'fold'  : 3
}

variables['dphilmet'] = {
    'name'  : 'dphilmet',
    'range' : (20,0,3.2),
    'xaxis' : 'dphilmet',
    'fold'  : 3
}

variables['dphilmet2'] = {
    'name'  : 'dphilmet2',
    'range' : (20,0,3.2),
    'xaxis' : 'dphilmet2',
    'fold'  : 3
}

variables['dphillmet'] = {
    'name'  : 'dphillmet',
    'range' : (20,0,3.2),
    'xaxis' : 'dphillmet',
    'fold'  : 3
}

variables['dphilep1jet1'] = {
    'name'  : 'dphilep1jet1',
    'range' : (20,0,3.2),
    'xaxis' : 'dphilep1jet1',
    'fold'  : 3
}

variables['dphilep1jet2'] = {
    'name'  : 'dphilep1jet2*(CleanJet_pt[1]>30)',
    'range' : (20,0,3.2),
    'xaxis' : 'dphilep1jet2',
    'fold'  : 3
}

variables['dphilep2jet1'] = {
    'name'  : 'dphilep2jet1',
    'range' : (20,0,3.2),
    'xaxis' : 'dphilep2jet1',
    'fold'  : 3
}

variables['dphilep2jet2'] = {
    'name'  : 'dphilep2jet2*(CleanJet_pt[1]>30)',
    'range' : (20,0,3.2),
    'xaxis' : 'dphilep1jet2',
    'fold'  : 3
}

variables['dphijjmet'] = {
    'name'  : 'dphijjmet',
    'range' : (20,0,3.2),
    'xaxis' : 'dphijjmet',
    'fold'  : 3
}

variables['ht'] = {
    'name'  : 'ht',
    'range' : (40,0,200),
    'xaxis' : 'ht [GeV]',
    'fold'  : 3
}

variables['dphijj'] = {
    'name'  : 'dphijj',
    'range' : (20,0,3.2),
    'xaxis' : 'dphijj',
    'fold'  : 3
}

variables['dphijet1met'] = {
    'name'  : 'dphijet1met',
    'range' : (20,0,3.2),
    'xaxis' : 'dphijet1met',
    'fold'  : 3
}

variables['DeepCSV_jet1'] = {
    'name'  : 'Alt$(Jet_btagDeepB[CleanJet_jetIdx[0]],-2)',
    'range' : (50,0.0,1.0),
    'xaxis' : 'Leading jet DeepCSV',
    'fold'  : 3
}

variables['DeepCSV_jet2'] = {
    'name'  : 'Alt$(Jet_btagDeepB[CleanJet_jetIdx[1]],-2)',
    'range' : (50,0.0,1.0),
    'xaxis' : 'Sub-leading jet DeepCSV',
    'fold'  : 3
}


# #############################
# # 1 jet specific BDT training
# #############################

# variables['BDTG6_1j'] = {
#     'name'     : 'BDT_WHSS_1j_v9',     
#     'range'    : (40,-1,1),   
#     'doWeight' : 1,
#     'binX'     : 1,
#     'binY'     : 40,
#     'xaxis'    : 'BDT discriminant',
#     'yaxis'    : 'Events',
#     'fold'     : 3
# }

# variables['BDTG6_1j_more'] = {
#     'name'  : 'BDT_WHSS_1j_v9',     
#     'range' : (1000,-1,1),   
#     'xaxis' : 'BDT discriminant',
#     'fold'  : 3
# }

# ##############################
# # 2 jets specific BDT training
# ##############################

# variables['BDTG5_2j'] = {
#     'name'     : 'BDT_WHSS_2j_v9',
#     'range'    : (40,-1,1),   
#     'doWeight' : 1,
#     'binX'     : 1,
#     'binY'     : 40,
#     'xaxis'    : 'BDT discriminant',
#     'yaxis'    : 'Events',
#     'fold'     : 3
# }

# variables['BDTG5_2j_more'] = {
#     'name'  : 'BDT_WHSS_2j_v9',     
#     'range' : (1000,-1,1),   
#     'xaxis' : 'BDT discriminant',
#     'fold'  : 3
# }

# ######################################
# # Default BDT training in AN-22-120_v1
# ######################################

# variables['BDTG6'] = {
#     'name'     : 'BDT_WHSS_v9',     
#     'range'    : (40,-1,1),   
#     'doWeight' : 1,
#     'binX'     : 1,
#     'binY'     : 40,
#     'xaxis'    : 'BDT discriminant',
#     'yaxis'    : 'Events',
#     'fold'     : 3
# }

# variables['BDTG6_more'] = {
#     'name'  : 'BDT_WHSS_v9',     
#     'range' : (1000,-1,1),   
#     'xaxis' : 'BDT discriminant',
#     'fold'  : 3
# }

# ########################################################
# # Default BDT training but with TopSemileptonic as fakes
# # Properly applying events weights
# ########################################################

# variables['BDTG6_TT_XSweight'] = {
#     'name'     : 'BDT_WHSS_TopSemileptonic_XSweight_v9',
#     'range'    : (40,-1,1),   
#     'doWeight' : 1,
#     'binX'     : 1,
#     'binY'     : 40,
#     'xaxis'    : 'BDT discriminant',
#     'yaxis'    : 'Events',
#     'fold'     : 3
# }

# variables['BDTG6_TT_XSweight_more'] = {
#     'name'  : 'BDT_WHSS_TopSemileptonic_XSweight_v9',
#     'range' : (1000,-1,1),   
#     'xaxis' : 'BDT discriminant',
#     'fold'  : 3
# }

# ########################################################
# # Default BDT training but with TopSemileptonic as fakes
# # Properly applying events weights
# ########################################################

# variables['BDTG5_TT_weight'] = {
#     'name'     : 'BDT_WHSS_TopSemileptonic_weight_v9',
#     'range'    : (40,-1,1),   
#     'doWeight' : 1,
#     'binX'     : 1,
#     'binY'     : 40,
#     'xaxis'    : 'BDT discriminant',
#     'yaxis'    : 'Events',
#     'fold'     : 3
# }

# variables['BDTG5_TT_weight_more'] = {
#     'name'  : 'BDT_WHSS_TopSemileptonic_weight_v9',
#     'range' : (1000,-1,1),   
#     'xaxis' : 'BDT discriminant',
#     'fold'  : 3
# }

# ##############################################################
# # BDT training with TopSemileptonic as fakes - specific for 1j
# ##############################################################

# variables['BDTG2_TT_1j'] = {
#     'name'     : 'BDT_WHSS_TopSemileptonic_1j_v9',     
#     'range'    : (40,-1,1),   
#     'doWeight' : 1,
#     'binX'     : 1,
#     'binY'     : 40,
#     'xaxis'    : 'BDT discriminant',
#     'yaxis'    : 'Events',
#     'fold'     : 3
# }

# variables['BDTG2_TT_1j_more'] = {
#     'name'  : 'BDT_WHSS_TopSemileptonic_1j_v9',     
#     'range' : (1000,-1,1),   
#     'xaxis' : 'BDT discriminant',
#     'fold'  : 3
# }

# ##############################################################
# # BDT training with TopSemileptonic as fakes - specific for 2j
# ##############################################################

# variables['BDTG5_TT_2j'] = {
#     'name'     : 'BDT_WHSS_TopSemileptonic_2j_v9',     
#     'range'    : (40,-1,1),   
#     'doWeight' : 1,
#     'binX'     : 1,
#     'binY'     : 40,
#     'xaxis'    : 'BDT discriminant',
#     'yaxis'    : 'Events',
#     'fold'     : 3
# }

# variables['BDTG5_TT_2j_more'] = {
#     'name'  : 'BDT_WHSS_TopSemileptonic_2j_v9',     
#     'range' : (1000,-1,1),   
#     'xaxis' : 'BDT discriminant',
#     'fold'  : 3
# }

# # BDT binnings
# ##############

# variables['BDTG5_TT_2j_binning_0_0'] = {
#     'name'  : 'BDT_WHSS_TopSemileptonic_2j_v9',
#     'range' : ([-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 1.0],),
#     'xaxis' : 'BDT discriminant',
#     'fold'  : 3
# }

# variables['BDTG5_TT_2j_binning_0_1'] = { 
#     'name'  : 'BDT_WHSS_TopSemileptonic_2j_v9',
#     'range' : ([-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.1, 1.0],),
#     'xaxis' : 'BDT discriminant',
#     'fold'  : 3
# }

# variables['BDTG5_TT_2j_binning_0_2'] = {
#     'name'  : 'BDT_WHSS_TopSemileptonic_2j_v9',
#     'range' : ([-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.1, 0.2, 1.0],),
#     'xaxis' : 'BDT discriminant',
#     'fold'  : 3
# }

# variables['BDTG5_TT_2j_binning_0_3'] = {
#     'name'  : 'BDT_WHSS_TopSemileptonic_2j_v9',
#     'range' : ([-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.1, 0.2, 0.3, 1.0],),
#     'xaxis' : 'BDT discriminant',
#     'fold'  : 3
# }

# variables['BDTG5_TT_2j_binning_0_4'] = {
#     'name'  : 'BDT_WHSS_TopSemileptonic_2j_v9',
#     'range' : ([-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.1, 0.2, 0.3, 0.4, 1.0],),
#     'xaxis' : 'BDT discriminant',
#     'fold'  : 3
# }

# variables['BDTG5_TT_2j_binning_0_45'] = {
#     'name'  : 'BDT_WHSS_TopSemileptonic_2j_v9',
#     'range' : ([-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.1, 0.2, 0.3, 0.4, 0.45, 1.0],),
#     'xaxis' : 'BDT discriminant',
#     'fold'  : 3
# }

# variables['BDTG5_TT_2j_binning_0_5'] = {
#     'name'  : 'BDT_WHSS_TopSemileptonic_2j_v9',
#     'range' : ([-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 1.0],),
#     'xaxis' : 'BDT discriminant',
#     'fold'  : 3
# }

# variables['BDTG5_TT_2j_binning_0_55'] = {
#     'name'  : 'BDT_WHSS_TopSemileptonic_2j_v9',
#     'range' : ([-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.55, 1.0],),
#     'xaxis' : 'BDT discriminant',
#     'fold'  : 3
# }

# variables['BDTG5_TT_2j_binning_0_6'] = {
#     'name'  : 'BDT_WHSS_TopSemileptonic_2j_v9',
#     'range' : ([-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 1.0],),
#     'xaxis' : 'BDT discriminant',
#     'fold'  : 3
# }

# variables['BDTG5_TT_2j_binning_0_65'] = {
#     'name'  : 'BDT_WHSS_TopSemileptonic_2j_v9',
#     'range' : ([-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.65, 1.0],),
#     'xaxis' : 'BDT discriminant',
#     'fold'  : 3
# }

# variables['BDTG5_TT_2j_binning_0_7'] = {
#     'name'  : 'BDT_WHSS_TopSemileptonic_2j_v9',
#     'range' : ([-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 1.0],),
#     'xaxis' : 'BDT discriminant',
#     'fold'  : 3
# }

# variables['BDTG5_TT_2j_binning_0_75'] = {
#     'name'  : 'BDT_WHSS_TopSemileptonic_2j_v9',
#     'range' : ([-1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.75, 1.0],),
#     'xaxis' : 'BDT discriminant',
#     'fold'  : 3
# }


