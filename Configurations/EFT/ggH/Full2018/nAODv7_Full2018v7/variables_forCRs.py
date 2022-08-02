# variables

#variables = {}
    
variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                        }

variables['mllSR'] = { 'name' : 'mll',
                     'range': (25,0,250),
                     'xaxis': 'm_{ll}',
                     'fold' : 3
                }

variables['mllDYCR'] = { 'name' : 'mll',
                     'range': (25,0,100),
                     'xaxis': 'm_{ll}',
                     'fold' : 3
                }
variables['mllTopCR'] = { 'name' : 'mll',
                     'range': (25,0,250),
                     'xaxis': 'm_{ll}',
                     'fold' : 3
                }

variables['mthSR'] = { 'name' : 'mth',
                     'range': (25,50,150),
                     'xaxis': 'm_{T}^{H}',
                     'fold' : 3
                }

variables['mthDYCR'] = { 'name' : 'mth',
                     'range': (25,0,100),
                     'xaxis': 'm_{T}^{H}',
                     'fold' : 3
                }

variables['mthTopCR'] = { 'name' : 'mth',
                     'range': (25,0,250),
                     'xaxis': 'm_{T}^{H}',
                     'fold' : 3
                }

variables['mllVSmthOrig'] = {   'name': 'mll:mth',
                           'range': ([60,70,80,90,100,110,120,160,200,240,280],[0,26,41,56,71,85,100,120,140,160,180,200],),
                           'xaxis': 'm_{ll} : m_{T}^{H}',
                           'fold': 3
                       }
variables['mllVSmth'] = {   'name': 'mll:mth',
                           'range': ([60,70,80,90,100,110,125],[12,25,40,55,70,100,120,140,160,180,200],),
                           'xaxis': 'm_{ll} : m_{T}^{H}',
                           'fold': 3
                       }

variables['dphill']  = {  'name': 'dphill',
                        'range' : (20,0.0,3.2),
                        'xaxis' : '#Delta#phi_{ll}',
                        'fold'  : 3
                        }

##### objects #######

variables['eta1']  = {  'name': 'Lepton_eta[0]',
                        'range' : (20,-3,3),
                        'xaxis' : '#eta 1st lep',
                        'fold'  : 3
                        }
variables['eta2']  = {  'name': 'Lepton_eta[1]',
                        'range' : (20,-3,3),
                        'xaxis' : '#eta 2nd lep',
                        'fold'  : 3
                        }
variables['phi1']  = {  'name': 'Lepton_phi[0]',
                        'range' : (20,-3.2,3.2),
                        'xaxis' : '#phi 1st lep',
                        'fold'  : 3
                        }
variables['phi2']  = {  'name': 'Lepton_phi[1]',
                        'range' : (20,-3.2,3.2),
                        'xaxis' : '#phi 2nd lep',
                        'fold'  : 3
                        }
variables['puppimetDYCR']  = {
                        'name': 'PuppiMET_pt',
                        'range' : (20,0,100),
                        'xaxis' : 'puppimet [GeV]',
                        'fold'  : 3
                        }
variables['puppimetTopCR']  = {
                        'name': 'PuppiMET_pt',
                        'range' : (20,0,200),
                        'xaxis' : 'puppimet [GeV]',
                        'fold'  : 3
                        }

variables['njet']  = {
                        'name': 'Sum$(CleanJet_pt>30)',
                        'range' : (5,0,5),
                        'xaxis' : 'Number of jets',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }
variables['jetpt1']  = {
                        'name': '(Sum$(CleanJet_pt>30)>0)*(Alt$(CleanJet_pt[0], 0)) - (Sum$(CleanJet_pt>30)==0)*99',
                        'range' : (20,0,200),
                        'xaxis' : 'p_{T} 1st jet',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }
variables['jeteta1']  = {  'name': '(Sum$(CleanJet_pt>30)>0)*(Alt$(CleanJet_eta[0], 0)) - (Sum$(CleanJet_pt>30)==0)*99',
                        'range' : (20,-5.0,5.0),
                        'xaxis' : '#eta 1st jet',
                        'fold'  : 0
                        }
