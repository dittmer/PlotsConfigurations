#!/bin/bash

mkdir -p /afs/cern.ch/user/n/ntrevisa/work/latinos/UL_production/CMSSW_10_6_27/src/PlotsConfigurations/Configurations/WH_chargeAsymmetry/UL/Full2017_v9/BDTconfig_WH3l/logs_OSSF/
cd /afs/cern.ch/user/n/ntrevisa/work/latinos/UL_production/CMSSW_10_6_27/src/PlotsConfigurations/Configurations/WH_chargeAsymmetry/UL/Full2017_v9/BDTconfig_WH3l/
eval `scramv1 ru -sh`
python ClassificationBDTOSSF.py _matched_signal
