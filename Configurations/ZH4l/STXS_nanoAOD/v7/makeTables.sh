#!/bin/bash

set -e

for year in Full2016nano_STXS_1p1 Full2017nano_STXS_1p1 Full2018nano_STXS_1p1
do
    echo " --> $year"
    YEAR=`echo $year | awk -F "Full" '{print $2}' | awk -F "nano" '{print $1}'`
    mkTable.py ${year}/Combination/fitDiagnosticsZH4l_${YEAR}.root -e --mergingMap merging_map_VH.py --fancyTable --mergedOnly --decimals 1
    mv yields_table.tex yields_table_${YEAR}.tex
done
