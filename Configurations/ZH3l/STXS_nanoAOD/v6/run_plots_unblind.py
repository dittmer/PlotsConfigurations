import os

plotOnly = False
postfit = True

options = { 
    'ZH3l' : {
        '2016' : {
            'config' : '/afs/cern.ch/user/d/dittmer/private/hww2018/CMSSW_9_4_12/src/PlotsConfigurations/Configurations/ZH3l/STXS_nanoAOD/v6/Full2016nano_STXS_1p1/',
            'cuts': {
                'zh3l_SR_1j_ptv_lt150': {'variable': 'mTlmetj',  'combineCut': 'ch3_zh3l_2016_SR1j_ptv_lt150', 'append': ' --scaleToPlot=2.0 --minLogCratio=0.05'},
                'zh3l_SR_1j_ptv_gt150': {'variable': 'mTlmetj',  'combineCut': 'ch3_zh3l_2016_SR1j_ptv_gt150', 'append': ' --scaleToPlot=2.0 --minLogCratio=0.05'},
                'zh3l_SR_2j_ptv_lt150': {'variable': 'mTlmetjj', 'combineCut': 'ch3_zh3l_2016_SR2j_ptv_lt150', 'append': ' --scaleToPlot=2.0 --minLogCratio=0.05'},
                'zh3l_SR_2j_ptv_gt150': {'variable': 'mTlmetjj', 'combineCut': 'ch3_zh3l_2016_SR2j_ptv_gt150', 'append': ' --scaleToPlot=2.0 --minLogCratio=0.05'}
            }
        },
        '2017' : {
            'config' : '/afs/cern.ch/user/d/dittmer/private/hww2018/CMSSW_9_4_12/src/PlotsConfigurations/Configurations/ZH3l/STXS_nanoAOD/v6/Full2017nano_STXS_1p1/',
            'cuts': {
                'zh3l_SR_1j_ptv_lt150': {'variable': 'mTlmetj',  'combineCut': 'ch3_zh3l_2017_SR1j_ptv_lt150', 'append': ' --scaleToPlot=2.0 --minLogCratio=0.05'},
                'zh3l_SR_1j_ptv_gt150': {'variable': 'mTlmetj',  'combineCut': 'ch3_zh3l_2017_SR1j_ptv_gt150', 'append': ' --scaleToPlot=2.0 --minLogCratio=0.05'},
                'zh3l_SR_2j_ptv_lt150': {'variable': 'mTlmetjj', 'combineCut': 'ch3_zh3l_2017_SR2j_ptv_lt150', 'append': ' --scaleToPlot=2.0 --minLogCratio=0.05'},
                'zh3l_SR_2j_ptv_gt150': {'variable': 'mTlmetjj', 'combineCut': 'ch3_zh3l_2017_SR2j_ptv_gt150', 'append': ' --scaleToPlot=2.0 --minLogCratio=0.05'}
            }
        },
        '2018' : {
            'config' : '/afs/cern.ch/user/d/dittmer/private/hww2018/CMSSW_9_4_12/src/PlotsConfigurations/Configurations/ZH3l/STXS_nanoAOD/v6/Full2018nano_STXS_1p1/',
            'cuts': {
                'zh3l_SR_1j_ptv_lt150': {'variable': 'mTlmetj',  'combineCut': 'ch3_zh3l_2018_SR1j_ptv_lt150', 'append': ' --scaleToPlot=2.0 --minLogCratio=0.05'},
                'zh3l_SR_1j_ptv_gt150': {'variable': 'mTlmetj',  'combineCut': 'ch3_zh3l_2018_SR1j_ptv_gt150', 'append': ' --scaleToPlot=2.0 --minLogCratio=0.05'},
                'zh3l_SR_2j_ptv_lt150': {'variable': 'mTlmetjj', 'combineCut': 'ch3_zh3l_2018_SR2j_ptv_lt150', 'append': ' --scaleToPlot=2.0 --minLogCratio=0.05'},
                'zh3l_SR_2j_ptv_gt150': {'variable': 'mTlmetjj', 'combineCut': 'ch3_zh3l_2018_SR2j_ptv_gt150', 'append': ' --scaleToPlot=2.0 --minLogCratio=0.05'}
            }
        }
    },
    'ZH4l' : {
        '2016' : {
            'config' : '/afs/cern.ch/user/d/dittmer/private/hww2018/CMSSW_9_4_12/src/PlotsConfigurations/Configurations/ZH4l/STXS_nanoAOD/v6/Full2016nano_STXS_1p1/',
            'cuts': {
                'zh4l_XSF_13TeV_ptv_lt150' : {'variable' : 'class0_XSF', 'combineCut': 'ch4_zh4l_2016_XSF_ptv_lt150', 'append': ' --scaleToPlot=2.0 --maxLogCratio=50'},
                'zh4l_XSF_13TeV_ptv_gt150' : {'variable' : 'class0_XSF', 'combineCut': 'ch4_zh4l_2016_XSF_ptv_gt150', 'append': ' --scaleToPlot=2.0 --maxLogCratio=50'},
                'zh4l_XDF_13TeV_ptv_lt150' : {'variable' : 'class1_XDF', 'combineCut': 'ch4_zh4l_2016_XDF_ptv_lt150', 'append': ' --scaleToPlot=2.0 --maxLogCratio=50'},
                'zh4l_XDF_13TeV_ptv_gt150' : {'variable' : 'class1_XDF', 'combineCut': 'ch4_zh4l_2016_XDF_ptv_gt150', 'append': ' --scaleToPlot=2.0 --maxLogCratio=50'}
            }
        },
        '2017' : {
            'config' : '/afs/cern.ch/user/d/dittmer/private/hww2018/CMSSW_9_4_12/src/PlotsConfigurations/Configurations/ZH4l/STXS_nanoAOD/v6/Full2017nano_STXS_1p1/',
            'cuts': {
                'zh4l_XSF_13TeV_ptv_lt150' : {'variable' : 'class0_XSF', 'combineCut': 'ch4_zh4l_2017_XSF_ptv_lt150', 'append': ' --scaleToPlot=2.0 --maxLogCratio=50'},
                'zh4l_XSF_13TeV_ptv_gt150' : {'variable' : 'class0_XSF', 'combineCut': 'ch4_zh4l_2017_XSF_ptv_gt150', 'append': ' --scaleToPlot=2.0 --maxLogCratio=50'},
                'zh4l_XDF_13TeV_ptv_lt150' : {'variable' : 'class1_XDF', 'combineCut': 'ch4_zh4l_2017_XDF_ptv_lt150', 'append': ' --scaleToPlot=2.0 --maxLogCratio=50'},
                'zh4l_XDF_13TeV_ptv_gt150' : {'variable' : 'class1_XDF', 'combineCut': 'ch4_zh4l_2017_XDF_ptv_gt150', 'append': ' --scaleToPlot=2.0 --maxLogCratio=50'}
            }
        },
        '2018' : {
            'config' : '/afs/cern.ch/user/d/dittmer/private/hww2018/CMSSW_9_4_12/src/PlotsConfigurations/Configurations/ZH4l/STXS_nanoAOD/v6/Full2018nano_STXS_1p1/',
            'cuts': {
                'zh4l_XSF_13TeV_ptv_lt150' : {'variable' : 'class0_XSF', 'combineCut': 'ch4_zh4l_2018_XSF_ptv_lt150', 'append': ' --scaleToPlot=2.0 --maxLogCratio=50'},
                'zh4l_XSF_13TeV_ptv_gt150' : {'variable' : 'class0_XSF', 'combineCut': 'ch4_zh4l_2018_XSF_ptv_gt150', 'append': ' --scaleToPlot=2.0 --maxLogCratio=50'},
                'zh4l_XDF_13TeV_ptv_lt150' : {'variable' : 'class1_XDF', 'combineCut': 'ch4_zh4l_2018_XDF_ptv_lt150', 'append': ' --scaleToPlot=2.0 --maxLogCratio=50'},
                'zh4l_XDF_13TeV_ptv_gt150' : {'variable' : 'class1_XDF', 'combineCut': 'ch4_zh4l_2018_XDF_ptv_gt150', 'append': ' --scaleToPlot=2.0 --maxLogCratio=50'}
            }
        }
    }
}

thisdir = '/afs/cern.ch/user/d/dittmer/private/hww2018/CMSSW_9_4_12/src/PlotsConfigurations/Configurations/VH_STXS/'
outputFile = 'output_postfit.root' if postfit else 'output.root'
version = 'postfit' if postfit else 'prefit'
kind = 's' if postfit else 'p'

for channel in options.keys():
    for year in options[channel].keys():
        if not os.path.exists(channel+'/'+year):
            os.makedirs(channel+'/'+year)
        print 'Moving to '+options[channel][year]['config']
        os.chdir(options[channel][year]['config'])
        if not plotOnly:
            for cut in options[channel][year]['cuts']:
                variable = options[channel][year]['cuts'][cut]['variable']
                combineCut = options[channel][year]['cuts'][cut]['combineCut']
                command = 'mkPostFitPlot.py --inputFileCombine=/afs/cern.ch/work/d/dittmer/private/hww2018/hig-19-017/VHlepSTXS/fitDiagnosticsVH_obs.root --variable=%s --cut=%s --cutNameInOriginal=%s --inputFile=/afs/cern.ch/work/d/dittmer/private/hww2018/hig-19-017/VHlepSTXS/%s/%s/%s/%s/shapes/histos_%s.root --kind=%s --pycfg=configuration.py --outputFile=%s'%(variable,combineCut,cut,channel,year,cut,variable,cut,kind,outputFile)
                os.system(command)
            os.system('mv '+outputFile+' '+thisdir+'/'+channel+'/'+year)
        for cut in options[channel][year]['cuts']:
            #Output file has been produced, now do plotting
            append = options[channel][year]['cuts'][cut]['append']
            command = 'mkPlot.py --inputFile=%s/%s/%s/%s --showIntegralLegend=1 --outputDirPlots=plots_unblind_%s --nuisancesFile=%snuisances_dummy.py --onlyPlot=cratio --onlyCut='%(thisdir,channel,year,outputFile,version,thisdir)+cut+append
            os.system(command)
        os.system('rm -r '+thisdir+'/'+channel+'/'+year+'/plots_unblind_'+version)
        os.system('mv plots_unblind_'+version+' '+thisdir+'/'+channel+'/'+year)
        os.chdir(thisdir)

