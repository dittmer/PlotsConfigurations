#!/bin/bash

pushd $COMBINE_SOURCE_DIR #Set to your combine home directory, e.g. the CMSSW/src directory where combine lives
eval `scramv1 runtime -sh`
popd

############## WHSS 2l
combineCards.py eu_1j=Full2016nanov6/datacardsWHSS2016_final_v1_ttHMVASF/hww2l2v_13TeV_of2j_WH_SS_eu_1j/mlljj20_whss/datacard.txt.pruned.txt  \
                eu_2j=Full2016nanov6/datacardsWHSS2016_final_v1_ttHMVASF/hww2l2v_13TeV_of2j_WH_SS_eu_2j/mlljj20_whss_bin3/datacard.txt.pruned.txt  \
                uu_1j=Full2016nanov6/datacardsWHSS2016_final_v1_ttHMVASF/hww2l2v_13TeV_of2j_WH_SS_uu_1j/mlljj20_whss/datacard.txt.pruned.txt  \
                uu_2j=Full2016nanov6/datacardsWHSS2016_final_v1_ttHMVASF/hww2l2v_13TeV_of2j_WH_SS_uu_2j/mlljj20_whss_bin3/datacard.txt.pruned.txt  \
                WZ_1j=/afs/cern.ch/work/d/dittmer/private/hww2018/hig-19-017/VHlep/ZH3l/2016/zh3l_WZ_CR_1j/events/datacard.txt.pruned.txt \
                WZ_2j=/afs/cern.ch/work/d/dittmer/private/hww2018/hig-19-017/VHlep/ZH3l/2016/zh3l_WZ_CR_2j/events/datacard.txt.pruned.txt \
                > Full2016_whss.txt

combineCards.py eu_1j=Full2017nanov6/datacardsWHSS2017_final_v2_ttHMVASF/hww2l2v_13TeV_of2j_WH_SS_eu_1j/mlljj20_whss/datacard.txt.pruned.txt  \
                eu_2j=Full2017nanov6/datacardsWHSS2017_final_v2_ttHMVASF/hww2l2v_13TeV_of2j_WH_SS_eu_2j/mlljj20_whss_bin3/datacard.txt.pruned.txt  \
                uu_1j=Full2017nanov6/datacardsWHSS2017_final_v2_ttHMVASF/hww2l2v_13TeV_of2j_WH_SS_uu_1j/mlljj20_whss/datacard.txt.pruned.txt  \
                uu_2j=Full2017nanov6/datacardsWHSS2017_final_v2_ttHMVASF/hww2l2v_13TeV_of2j_WH_SS_uu_2j/mlljj20_whss_bin3/datacard.txt.pruned.txt  \
                WZ_1j=/afs/cern.ch/work/d/dittmer/private/hww2018/hig-19-017/VHlep/ZH3l/2017/zh3l_WZ_CR_1j/events/datacard.txt.pruned.txt \
                WZ_2j=/afs/cern.ch/work/d/dittmer/private/hww2018/hig-19-017/VHlep/ZH3l/2017/zh3l_WZ_CR_2j/events/datacard.txt.pruned.txt \
                > Full2017_whss.txt

combineCards.py eu_1j=Full2018nanov6/datacardsWHSS2018_final_ttHMVASF/hww2l2v_13TeV_of2j_WH_SS_eu_1j/mlljj20_whss/datacard.txt.pruned.txt  \
                eu_2j=Full2018nanov6/datacardsWHSS2018_final_ttHMVASF/hww2l2v_13TeV_of2j_WH_SS_eu_2j/mlljj20_whss_bin3/datacard.txt.pruned.txt  \
                uu_1j=Full2018nanov6/datacardsWHSS2018_final_ttHMVASF/hww2l2v_13TeV_of2j_WH_SS_uu_1j/mlljj20_whss/datacard.txt.pruned.txt  \
                uu_2j=Full2018nanov6/datacardsWHSS2018_final_ttHMVASF/hww2l2v_13TeV_of2j_WH_SS_uu_2j/mlljj20_whss_bin3/datacard.txt.pruned.txt  \
                WZ_1j=/afs/cern.ch/work/d/dittmer/private/hww2018/hig-19-017/VHlep/ZH3l/2018/zh3l_WZ_CR_1j/events/datacard.txt.pruned.txt \
                WZ_2j=/afs/cern.ch/work/d/dittmer/private/hww2018/hig-19-017/VHlep/ZH3l/2018/zh3l_WZ_CR_2j/events/datacard.txt.pruned.txt \
                > Full2018_whss.txt

combineCards.py whss_2016=Full2016_whss.txt \
                whss_2017=Full2017_whss.txt \
                whss_2018=Full2018_whss.txt \
                > FullRunII_WHSS.txt

combineCards.py eu_1j=Full2016nanov6/datacardsWHSS2016_final_v1_ttHMVASF_test/hww2l2v_13TeV_of2j_WH_SS_eu_1j/mlljj20_whss/datacard.txt.pruned.txt  \
                eu_2j=Full2016nanov6/datacardsWHSS2016_final_v1_ttHMVASF_test/hww2l2v_13TeV_of2j_WH_SS_eu_2j/mlljj20_whss_bin3/datacard.txt.pruned.txt  \
                uu_1j=Full2016nanov6/datacardsWHSS2016_final_v1_ttHMVASF_test/hww2l2v_13TeV_of2j_WH_SS_uu_1j/mlljj20_whss/datacard.txt.pruned.txt  \
                uu_2j=Full2016nanov6/datacardsWHSS2016_final_v1_ttHMVASF_test/hww2l2v_13TeV_of2j_WH_SS_uu_2j/mlljj20_whss_bin3/datacard.txt.pruned.txt  \
                WZ_1j=/afs/cern.ch/work/d/dittmer/private/hww2018/hig-19-017/VHlep/ZH3l/2016/zh3l_WZ_CR_1j/events/datacard.txt.pruned.txt \
                WZ_2j=/afs/cern.ch/work/d/dittmer/private/hww2018/hig-19-017/VHlep/ZH3l/2016/zh3l_WZ_CR_2j/events/datacard.txt.pruned.txt \
                > Full2016_whss_test.txt

combineCards.py eu_1j=Full2017nanov6/datacardsWHSS2017_final_v2_ttHMVASF_test/hww2l2v_13TeV_of2j_WH_SS_eu_1j/mlljj20_whss/datacard.txt.pruned.txt  \
                eu_2j=Full2017nanov6/datacardsWHSS2017_final_v2_ttHMVASF_test/hww2l2v_13TeV_of2j_WH_SS_eu_2j/mlljj20_whss_bin3/datacard.txt.pruned.txt  \
                uu_1j=Full2017nanov6/datacardsWHSS2017_final_v2_ttHMVASF_test/hww2l2v_13TeV_of2j_WH_SS_uu_1j/mlljj20_whss/datacard.txt.pruned.txt  \
                uu_2j=Full2017nanov6/datacardsWHSS2017_final_v2_ttHMVASF_test/hww2l2v_13TeV_of2j_WH_SS_uu_2j/mlljj20_whss_bin3/datacard.txt.pruned.txt  \
                WZ_1j=/afs/cern.ch/work/d/dittmer/private/hww2018/hig-19-017/VHlep/ZH3l/2017/zh3l_WZ_CR_1j/events/datacard.txt.pruned.txt \
                WZ_2j=/afs/cern.ch/work/d/dittmer/private/hww2018/hig-19-017/VHlep/ZH3l/2017/zh3l_WZ_CR_2j/events/datacard.txt.pruned.txt \
                > Full2017_whss_test.txt

combineCards.py eu_1j=Full2018nanov6/datacardsWHSS2018_final_ttHMVASF_test/hww2l2v_13TeV_of2j_WH_SS_eu_1j/mlljj20_whss/datacard.txt.pruned.txt  \
                eu_2j=Full2018nanov6/datacardsWHSS2018_final_ttHMVASF_test/hww2l2v_13TeV_of2j_WH_SS_eu_2j/mlljj20_whss_bin3/datacard.txt.pruned.txt  \
                uu_1j=Full2018nanov6/datacardsWHSS2018_final_ttHMVASF_test/hww2l2v_13TeV_of2j_WH_SS_uu_1j/mlljj20_whss/datacard.txt.pruned.txt  \
                uu_2j=Full2018nanov6/datacardsWHSS2018_final_ttHMVASF_test/hww2l2v_13TeV_of2j_WH_SS_uu_2j/mlljj20_whss_bin3/datacard.txt.pruned.txt  \
                WZ_1j=/afs/cern.ch/work/d/dittmer/private/hww2018/hig-19-017/VHlep/ZH3l/2018/zh3l_WZ_CR_1j/events/datacard.txt.pruned.txt \
                WZ_2j=/afs/cern.ch/work/d/dittmer/private/hww2018/hig-19-017/VHlep/ZH3l/2018/zh3l_WZ_CR_2j/events/datacard.txt.pruned.txt \
                > Full2018_whss_test.txt

combineCards.py whss_2016=Full2016_whss_test.txt \
                whss_2017=Full2017_whss_test.txt \
                whss_2018=Full2018_whss_test.txt \
                > FullRunII_WHSS_test.txt

cards='Full2016_whss.txt Full2017_whss.txt Full2018_whss.txt FullRunII_WHSS.txt Full2016_whss_test.txt Full2017_whss_test.txt Full2018_whss_test.txt'
for card in $cards
do
    echo "nuisance edit rename Zg * QCDscale_VV QCDscale_Vg" >> $card
    echo "nuisance edit rename ZgS * QCDscale_VV QCDscale_Vg" >> $card
    echo "nuisance edit rename Wg * QCDscale_VV QCDscale_Vg" >> $card
    echo "nuisance edit rename WgS * QCDscale_VV QCDscale_Vg" >> $card
done

text2workspace.py Full2016_whss.txt -o Full2016_whss.root  -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
                   --PO 'map=.*/.*WH_.*:r_VH[1,-10,10]' \
                   --PO 'map=.*/.*ZH_.*:r_VH[1,-10,10]'

text2workspace.py Full2017_whss.txt -o Full2017_whss.root  -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
                   --PO 'map=.*/.*WH_.*:r_VH[1,-10,10]' \
                   --PO 'map=.*/.*ZH_.*:r_VH[1,-10,10]'

text2workspace.py Full2018_whss.txt -o Full2018_whss.root  -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
                   --PO 'map=.*/.*WH_.*:r_VH[1,-10,10]' \
                   --PO 'map=.*/.*ZH_.*:r_VH[1,-10,10]'

text2workspace.py FullRunII_WHSS.txt -o FullRunII_WHSS.root  -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
                   --PO 'map=.*/.*WH_.*:r_VH[1,-10,10]' \
                   --PO 'map=.*/.*ZH_.*:r_VH[1,-10,10]'

text2workspace.py Full2016_whss_test.txt -o Full2016_whss_test.root  -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
                   --PO 'map=.*/.*WH_.*:r_VH[1,-10,10]' \
                   --PO 'map=.*/.*ZH_.*:r_VH[1,-10,10]'

text2workspace.py Full2017_whss_test.txt -o Full2017_whss_test.root  -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
                   --PO 'map=.*/.*WH_.*:r_VH[1,-10,10]' \
                   --PO 'map=.*/.*ZH_.*:r_VH[1,-10,10]'

text2workspace.py Full2018_whss_test.txt -o Full2018_whss_test.root  -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
                   --PO 'map=.*/.*WH_.*:r_VH[1,-10,10]' \
                   --PO 'map=.*/.*ZH_.*:r_VH[1,-10,10]'

text2workspace.py FullRunII_WHSS_test.txt -o FullRunII_WHSS_test.root  -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
                   --PO 'map=.*/.*WH_.*:r_VH[1,-10,10]' \
                   --PO 'map=.*/.*ZH_.*:r_VH[1,-10,10]'

