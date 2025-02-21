#!/bin/bash

DIR=$PWD

cd /afs/cern.ch/user/d/dittmer/private/Combine/CMSSW_10_2_13/src/
eval `scramv1 runtime -sh`
cd /afs/cern.ch/user/d/dittmer/private/Combine/ModificationDatacards

find -L /afs/cern.ch/user/d/dittmer/private/hww2018/CMSSW_9_4_12/src/PlotsConfigurations/Configurations/ZH4l/STXS_nanoAOD/v7/Full2016nano_STXS_1p1/datacard_ZH4l_2016_v7_STXS_sigFix -name 'datacard.txt' | while read line; do
    python PruneDatacard.py -d $line -o $line.pruned.txt -i $DIR/inputs_to_prune_VHlep.py --suppressFluctuationError=1 -t 0.00001
done

find -L /afs/cern.ch/user/d/dittmer/private/hww2018/CMSSW_9_4_12/src/PlotsConfigurations/Configurations/ZH4l/STXS_nanoAOD/v7/Full2017nano_STXS_1p1/datacard_ZH4l_2017_v7_STXS_sigFix -name 'datacard.txt' | while read line; do
    python PruneDatacard.py -d $line -o $line.pruned.txt -i $DIR/inputs_to_prune_VHlep.py --suppressFluctuationError=1 -t 0.00001
done

find -L /afs/cern.ch/user/d/dittmer/private/hww2018/CMSSW_9_4_12/src/PlotsConfigurations/Configurations/ZH4l/STXS_nanoAOD/v7/Full2018nano_STXS_1p1/datacard_ZH4l_2018_v7_STXS_sigFix -name 'datacard.txt' | while read line; do
    python PruneDatacard.py -d $line -o $line.pruned.txt -i $DIR/inputs_to_prune_VHlep.py --suppressFluctuationError=1 -t 0.00001
done

cd $DIR
