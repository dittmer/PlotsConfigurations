# variables

#variables = {}
    
#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow


variables['BDT'] = {
     'name': 'hww_ZH_BDT(Entry$,0)',
     'range' : ([-0.50,-0.25,-0.15,0.,0.15,0.25,0.35,0.50,0.80],),
     'xaxis' : 'MVA discriminant ZH',
     'fold' : 3,
     'linesToAdd' : ['.L /afs/cern.ch/work/k/kaura/NewLatino_v6/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/ZH4l/nano_config/Full2016/hww_ZH_BDT.C+']
}  #change the path of macro

