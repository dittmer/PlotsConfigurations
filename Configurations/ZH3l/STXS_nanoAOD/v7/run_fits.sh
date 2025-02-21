#!/bin/bash

pushd /afs/cern.ch/user/d/dittmer/private/Combine/CMSSW_10_2_13/src/
eval `scramv1 runtime -sh`
popd

set -e

DIR=$PWD

for year in Full2016nano_STXS_1p1 Full2017nano_STXS_1p1 Full2018nano_STXS_1p1
do
    echo " --> $year"
    cd $DIR; cd $year ; YEAR=`echo $year | awk -F "Full" '{print $2}' | awk -F "nano" '{print $1}'`

    ## work directory
    cd Combination
    text2workspace.py ZH3l_Full${YEAR}nano_STXS_1p1.txt -o ZH3l_${YEAR}.root  -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
        --PO 'map=.*/.*PTV_LT150.*:r_ptv_lt150[1,-10,10]' \
        --PO 'map=.*/.*PTV_GT150.*:r_ptv_gt150[1,-10,10]'
    combine -M Significance   -t -1 --setParameters r_ptv_lt150=1,r_ptv_gt150=1 ZH3l_${YEAR}.root --X-rtd MINIMIZER_analytic --redefineSignalPOIs r_ptv_lt150     > signif_${YEAR}_ptv_lt150.out 2>&1
    combine -M Significance   -t -1 --setParameters r_ptv_lt150=1,r_ptv_gt150=1 ZH3l_${YEAR}.root --X-rtd MINIMIZER_analytic --redefineSignalPOIs r_ptv_gt150     > signif_${YEAR}_ptv_gt150.out 2>&1
    combine -M MultiDimFit    -t -1 --setParameters r_ptv_lt150=1,r_ptv_gt150=1 ZH3l_${YEAR}.root --X-rtd MINIMIZER_analytic --algo singles                       > mu_${YEAR}.out               2>&1
    combine -M FitDiagnostics -t -1 --setParameters r_ptv_lt150=1,r_ptv_gt150=1 ZH3l_${YEAR}.root --X-rtd MINIMIZER_analytic --saveNormalizations -n ZH3l_${YEAR}
done
