
### Run2 combination
# b-only fit
mkPostFitPlot.py --inputFileCombine ../../FullRun2_v7/darkHiggs_HT/datacards_combi/Run2_Comb/CFineEnd_mix_10_20/fitDiagnostics_postfit.root --outputFile darkHiggs_HT_postfit_b_lim/postfit_darkHiggs_HT_lim_2017v7.root --variable BDT_CFineEnd10 --cut Year2017_SB --cutNameInOriginal InCh_SB --inputFile darkHiggs_HT_root_lim/plots_darkHiggs_HT_lim_2017v7_nuisNorm_rename.root --kind b --structureFile structure.py -S samples.py --getSignalFromPrefit 1
mkPostFitPlot.py --inputFileCombine ../../FullRun2_v7/darkHiggs_HT/datacards_combi/Run2_Comb/CFineEnd_mix_10_20/fitDiagnostics_postfit.root --outputFile darkHiggs_HT_postfit_b_lim/postfit_darkHiggs_HT_lim_2017v7.root --variable BDT_CFineEnd10 --cut Year2017_TCR --cutNameInOriginal InCh_TCR --inputFile darkHiggs_HT_root_lim/plots_darkHiggs_HT_lim_2017v7_nuisNorm_rename.root --kind b --structureFile structure.py -S samples.py --getSignalFromPrefit 1
mkPostFitPlot.py --inputFileCombine ../../FullRun2_v7/darkHiggs_HT/datacards_combi/Run2_Comb/CFineEnd_mix_10_20/fitDiagnostics_postfit.root --outputFile darkHiggs_HT_postfit_b_lim/postfit_darkHiggs_HT_lim_2017v7.root --variable BDT_CFineEnd20 --cut Year2017_SR --cutNameInOriginal InCh_SR --inputFile darkHiggs_HT_root_lim/plots_darkHiggs_HT_lim_2017v7_nuisNorm_rename.root --kind b --structureFile structure.py -S samples.py --getSignalFromPrefit 1

mkPlot.py --pycfg=conf_postfit.py --inputFile darkHiggs_HT_postfit_b_lim/postfit_darkHiggs_HT_lim_2017v7.root --showIntegralLegend=1 --scaleToPlot=3000 --logOnly --outputDirPlots darkHiggs_HT_postfit_b_lim --postFit y

# s+b fit
mkPostFitPlot.py --inputFileCombine ../../FullRun2_v7/darkHiggs_HT/datacards_combi/Run2_Comb/CFineEnd_mix_10_20/fitDiagnostics_postfit.root --outputFile darkHiggs_HT_postfit_s_lim/postfit_darkHiggs_HT_lim_2017v7.root --variable BDT_CFineEnd10 --cut Year2017_SB --cutNameInOriginal InCh_SB --inputFile darkHiggs_HT_root_lim/plots_darkHiggs_HT_lim_2017v7_nuisNorm_rename.root --kind s --structureFile structure.py -S samples.py --getSignalFromPrefit 1
mkPostFitPlot.py --inputFileCombine ../../FullRun2_v7/darkHiggs_HT/datacards_combi/Run2_Comb/CFineEnd_mix_10_20/fitDiagnostics_postfit.root --outputFile darkHiggs_HT_postfit_s_lim/postfit_darkHiggs_HT_lim_2017v7.root --variable BDT_CFineEnd10 --cut Year2017_TCR --cutNameInOriginal InCh_TCR --inputFile darkHiggs_HT_root_lim/plots_darkHiggs_HT_lim_2017v7_nuisNorm_rename.root --kind s --structureFile structure.py -S samples.py --getSignalFromPrefit 1
mkPostFitPlot.py --inputFileCombine ../../FullRun2_v7/darkHiggs_HT/datacards_combi/Run2_Comb/CFineEnd_mix_10_20/fitDiagnostics_postfit.root --outputFile darkHiggs_HT_postfit_s_lim/postfit_darkHiggs_HT_lim_2017v7.root --variable BDT_CFineEnd20 --cut Year2017_SR --cutNameInOriginal InCh_SR --inputFile darkHiggs_HT_root_lim/plots_darkHiggs_HT_lim_2017v7_nuisNorm_rename.root --kind s --structureFile structure.py -S samples.py --getSignalFromPrefit 1

mkPlot.py --pycfg=conf_postfit.py --inputFile darkHiggs_HT_postfit_s_lim/postfit_darkHiggs_HT_lim_2017v7.root --showIntegralLegend=1 --scaleToPlot=3000 --logOnly --outputDirPlots darkHiggs_HT_postfit_s_lim --postFit y
