#!/bin/bash

pushd $COMBINE_SOURCE_DIR #Set to your combine home directory, e.g. the CMSSW/src directory where combine lives
eval `scramv1 runtime -sh`
popd

# Make combined datacards
#combineCards.py   WZ=Full2016/datacards/wh3l_wz_13TeV/events/datacard.txt \
#                  Zg=Full2016/datacards/wh3l_zg_13TeV/events/datacard.txt > WH3l_2016.txt

#combineCards.py   WZ=Full2017/datacards/wh3l_wz_13TeV/events/datacard.txt \
#                  Zg=Full2017/datacards/wh3l_zg_13TeV/events/datacard.txt > WH3l_2017.txt

#combineCards.py   WZ=Full2018/datacards/wh3l_wz_13TeV/events/datacard.txt \
#                  Zg=Full2018/datacards/wh3l_zg_13TeV/events/datacard.txt > WH3l_2018.txt

combineCards.py WH3l_2016=WH3l_2016.txt WH3l_2017=WH3l_2017.txt WH3l_2018=WH3l_2018.txt > WH3l.txt

# Convert datacards to workspaces
text2workspace.py WH3l_2016.txt -o WH3l_2016.root
text2workspace.py WH3l_2017.txt -o WH3l_2017.root
text2workspace.py WH3l_2018.txt -o WH3l_2018.root
text2workspace.py WH3l.txt -o WH3l.root

combine -M FitDiagnostics --expectSignal=1 --rMin=-10 --rMax=10 WH3l_2016.root --X-rtd MINIMIZER_analytic -n WH3l_2016
combine -M FitDiagnostics --expectSignal=1 --rMin=-10 --rMax=10 WH3l_2017.root --X-rtd MINIMIZER_analytic -n WH3l_2017
combine -M FitDiagnostics --expectSignal=1 --rMin=-10 --rMax=10 WH3l_2018.root --X-rtd MINIMIZER_analytic -n WH3l_2018
combine -M FitDiagnostics --expectSignal=1 --rMin=-10 --rMax=10 WH3l.root --X-rtd MINIMIZER_analytic -n WH3l
