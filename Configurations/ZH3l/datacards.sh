#!/bin/bash

set -e 

DIR=$PWD

inputPRUNE=${CMSSW_BASE}/src/PlotsConfigurations/Configurations/ZH3l/scripts/inputs_to_prune_VHlep.py

for year in Full2016_v6 Full2017_v6 Full2018_v6
do
    echo " --> $year"
    cd $DIR;
    YEAR=`echo $year | awk -F "Full" '{print $2}' | awk -F "_v6" '{print $1}'`
    cd $year/WHSSvar

    #echo "mkDatacards.py --pycfg configuration.py --inputFile rootFiles_ZH3l_${YEAR}_v7_STXS/plots_ZH3l_${YEAR}_v7_STXS.root"
    #mkDatacards.py --pycfg configuration.py --inputFile rootFiles_ZH3l_${YEAR}_v7_STXS/plots_ZH3l_${YEAR}_v7_STXS.root

    # Zero bins
    #python /afs/cern.ch/user/d/dittmer/public/zeroBins.py

    # Pruning
    #echo "  --> Pruning"
    
    #find -L datacards_ZH3l_${YEAR}_v6_WHSSvar -name 'datacard.txt' | while read line
    #do 
#	echo "python /afs/cern.ch/user/d/dittmer/private/Combine/ModificationDatacards/PruneDatacard.py -d $line -o $line.pruned.txt -i ${inputPRUNE} --suppressFluctuationError=1 -t 0.00001"
#	python /afs/cern.ch/user/d/dittmer/private/Combine/ModificationDatacards/PruneDatacard.py -d $line -o $line.pruned.txt -i ${inputPRUNE} --suppressFluctuationError=1 -t 0.00001
#    done
 
    python $DIR/removeLowStats.py
done
