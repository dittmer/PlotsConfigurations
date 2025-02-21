# cuts

supercut = ' Lepton_pt[0]>25 \
            && Lepton_pt[1]>15 \
            && Lepton_pt[2]>10 \
            && Lepton_pt[3]>10 \
            && (nLepton>=4 && Alt$(Lepton_pt[4],0)<10) \
            && chllll_zh4l == 0 \
            && z0Mass_zh4l_test[0]>12 \
            && bVeto \
                  '

#cuts['zh4l_preselection_13TeV'] = '((flagZ1SF_zh4l==1)&&(mllll_zh4l > 140)) || (flagZ1SF_zh4l==0)'

                          
cuts['zh4l_XSF_13TeV']  = {
    'expr' : 'flagZ1SF_zh4l==1 && mllll_zh4l_test[0] > 140 && z1Mass_zh4l_test[0] < 60 && z1Mass_zh4l_test[0] > 10 && abs(z0Mass_zh4l_test[0]-91.1876)< 15 && PuppiMET_pt > 35',
    'categories' : {
        'ptv_lt150' : 'ZH4l_pTZ[0] < 150',
        'ptv_gt150' : 'ZH4l_pTZ[0] > 150',
    }
}

cuts['zh4l_XDF_13TeV']  = {
    'expr' : 'flagZ1SF_zh4l==0 && z1Mass_zh4l_test[0] < 70 && z1Mass_zh4l_test[0] >10 && PuppiMET_pt > 20 && abs(z0Mass_zh4l_test[0]-91.1876) < 15',
    'categories' : {
        'ptv_lt150' : 'ZH4l_pTZ[0] < 150',
        'ptv_gt150' : 'ZH4l_pTZ[0] > 150',
    }
}
    
cuts['zh4l_ZZ_13TeV']  = ' z1Mass_zh4l_test[0] < 105 && z1Mass_zh4l_test[0] >75 \
                           && PuppiMET_pt < 35 \
                           && fabs(z0Mass_zh4l_test[0]-91.1876)< 15\
                           '

cuts['zh4l_ZZ_MET_13TeV']  = ' z1Mass_zh4l_test[0] < 105 && z1Mass_zh4l_test[0] >75 \
                           && PuppiMET_pt > 35 \
                           && fabs(z0Mass_zh4l_test[0]-91.1876)< 15\
                           '

