#!/bin/bash

ALLCUTS=( 'ossf' )
ALLPLOTS=( 'WH3l_drOSll_min'  'Jet_pt1' 'pt1' 'pt2' 'MET_pt' 'WH3l_dphilep1met' )
PLOTNAMES=( 'min OSSF dR(ll)' 'Leading jet p_{T}' 'Leading lepton p_{T}' 'Subleading lepton p_{T}' 'MET' '\Delta\phi(l,MET)' )

for CUT in ${ALLCUTS[@]}; do
    for i in ${!ALLPLOTS[@]}; do
	echo $CUT
	FIT_TEMPLATE=${ALLPLOTS[$i]}
	FIT_NAME=${PLOTNAMES[$i]}
	cp merge_template.py merge_temp.py
	sed -i 's/CUT/'$CUT'/g' merge_temp.py
	sed -i 's/FIT_TEMPLATE/'$FIT_TEMPLATE'/g' merge_temp.py
	mkCombinedPlot.py --pycfg=configuration_OSSF.py --inputCutsList merge_temp.py --variable $FIT_TEMPLATE --variableHR=$FIT_NAME --getVarFromFile=1 --outputDirPlots=combinedPlots/$CUT
    done
done
