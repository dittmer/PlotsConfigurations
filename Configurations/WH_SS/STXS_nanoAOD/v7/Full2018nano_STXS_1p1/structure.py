# structure configuration for datacard
# keys here must match keys in samples.py    
structure ={}

# keys here must match keys in samples.py 
for iproc in samples.keys():
    structure[iproc] = {
        'isSignal' : 1 if any(substring in iproc for substring in ['H_hww','H_htt']) else 0,
        'isData'   : 1 if iproc == 'DATA' else 0,
    }

structure['Wg']['removeFromCuts']      = ['hww2l2v_13TeV_of2j_WH_SS_uu_1j_ptv_gt150','hww2l2v_13TeV_of2j_WH_SS_uu_2j_ptv_gt150','hww2l2v_13TeV_of2j_WH_SS_uu_2j_ptv_lt150',
                                          'hww2l2v_13TeV_of2j_WH_SS_uu_1j_ptv_lt150']
structure['WW']['removeFromCuts']      = ['hww2l2v_13TeV_of2j_WH_SS_uu_2j_ptv_gt150','hww2l2v_13TeV_of2j_WH_SS_uu_2j_ptv_lt150']
structure['Zg']['removeFromCuts']      = ['hww2l2v_13TeV_of2j_WH_SS_uu_1j_ptv_gt150','hww2l2v_13TeV_of2j_WH_SS_uu_2j_ptv_gt150','hww2l2v_13TeV_of2j_WH_SS_eu_1j_ptv_gt150',
                                          'hww2l2v_13TeV_of2j_WH_SS_eu_2j_ptv_gt150']
structure['WWewk']['removeFromCuts']   = ['hww2l2v_13TeV_of2j_WH_SS_uu_1j_ptv_gt150','hww2l2v_13TeV_of2j_WH_SS_uu_2j_ptv_gt150','hww2l2v_13TeV_of2j_WH_SS_uu_2j_ptv_lt150',
                                          'hww2l2v_13TeV_of2j_WH_SS_uu_1j_ptv_lt150','hww2l2v_13TeV_of2j_WH_SS_eu_2j_ptv_gt150','hww2l2v_13TeV_of2j_WH_SS_eu_2j_ptv_lt150',
                                          'hww2l2v_13TeV_of2j_WH_SS_eu_1j_ptv_lt150']
structure['Fake_mm']['removeFromCuts'] = ['hww2l2v_13TeV_of2j_WH_SS_eu_1j_ptv_gt150','hww2l2v_13TeV_of2j_WH_SS_eu_2j_ptv_gt150','hww2l2v_13TeV_of2j_WH_SS_eu_2j_ptv_lt150',
                                          'hww2l2v_13TeV_of2j_WH_SS_eu_1j_ptv_lt150']
structure['top']['removeFromCuts']     = ['hww2l2v_13TeV_of2j_WH_SS_uu_1j_ptv_gt150','hww2l2v_13TeV_of2j_WH_SS_uu_2j_ptv_gt150','hww2l2v_13TeV_of2j_WH_SS_uu_2j_ptv_lt150']
structure['ZgS']['removeFromCuts']     = ['hww2l2v_13TeV_of2j_WH_SS_uu_1j_ptv_gt150','hww2l2v_13TeV_of2j_WH_SS_uu_2j_ptv_gt150']
structure['Fake_em']['removeFromCuts'] = ['hww2l2v_13TeV_of2j_WH_SS_uu_1j_ptv_gt150','hww2l2v_13TeV_of2j_WH_SS_uu_2j_ptv_gt150','hww2l2v_13TeV_of2j_WH_SS_uu_2j_ptv_lt150',
                                          'hww2l2v_13TeV_of2j_WH_SS_uu_1j_ptv_lt150']
structure['ggWW']['removeFromCuts']    = ['hww2l2v_13TeV_of2j_WH_SS_uu_1j_ptv_gt150','hww2l2v_13TeV_of2j_WH_SS_uu_2j_ptv_gt150','hww2l2v_13TeV_of2j_WH_SS_uu_2j_ptv_lt150',
                                          'hww2l2v_13TeV_of2j_WH_SS_uu_1j_ptv_lt150']
structure['DY']['removeFromCuts']      = ['hww2l2v_13TeV_of2j_WH_SS_uu_1j_ptv_gt150','hww2l2v_13TeV_of2j_WH_SS_uu_2j_ptv_gt150','hww2l2v_13TeV_of2j_WH_SS_uu_2j_ptv_lt150',
                                          'hww2l2v_13TeV_of2j_WH_SS_uu_1j_ptv_lt150','hww2l2v_13TeV_of2j_WH_SS_eu_1j_ptv_gt150','hww2l2v_13TeV_of2j_WH_SS_eu_2j_ptv_gt150',
                                          'hww2l2v_13TeV_of2j_WH_SS_eu_2j_ptv_lt150']


