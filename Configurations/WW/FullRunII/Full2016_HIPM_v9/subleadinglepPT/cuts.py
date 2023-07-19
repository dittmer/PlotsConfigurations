# cuts
supercut = '   mll>12 \
            && Lepton_pt[0]>25 \
            && Lepton_pt[1]>20 \
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && ptll>30 \
            && PuppiMET_pt > 20 \
            && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) \
            && mll > 20 \
           '
catCR = {
    '0j' : 'nGoodCleanJet == 0',
    '1j' : 'nGoodCleanJet == 1',
    '2j' : 'nGoodCleanJet >= 2',
}

catSR = {
    'B0'  : 'Lepton_pt[1] > 20       && Lepton_pt[1] <= 30',
    'B1'  : 'Lepton_pt[1] > 30       && Lepton_pt[1] <= 35',
    'B2'  : 'Lepton_pt[1] > 35       && Lepton_pt[1] <= 40',
    'B3'  : 'Lepton_pt[1] > 40       && Lepton_pt[1] <= 45',
    'B4'  : 'Lepton_pt[1] > 45       && Lepton_pt[1] <= 50',
    'B5'  : 'Lepton_pt[1] > 50       && Lepton_pt[1] <= 60',
    'B6'  : 'Lepton_pt[1] > 60',
}

##  signal regions
cuts['ww2l2v_13TeV_sr']  = {
    'expr' : 'sr',
    'categories' : dict((iCR+'_'+iSR,catCR[iCR]+' && '+catSR[iSR]) for iCR in catCR.keys() for iSR in catSR.keys()) 
}

# Top control region
cuts['ww2l2v_13TeV_top']  = {
    'expr' : 'topcr',
    'categories' : catCR
}
