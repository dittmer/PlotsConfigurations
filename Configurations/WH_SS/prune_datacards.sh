#!/bin/bash

DIR=$PWD

cd /afs/cern.ch/user/d/dittmer/private/Combine/CMSSW_10_2_13/src/
eval `scramv1 runtime -sh`
cd /afs/cern.ch/user/d/dittmer/private/Combine/ModificationDatacards

find -L $DIR/ -name 'datacard.txt' | while read line; do
    echo $line
    python PruneDatacard.py -d $line -o $line.pruned.txt -i $DIR/inputs_to_prune_VHlep.py --suppressFluctuationError=1 -t 0.00001
done

cd $DIR
