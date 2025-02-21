#!/bin/bash

pushd $COMBINE_SOURCE_DIR #Set to your combine home directory, e.g. the CMSSW/src directory where combine lives
eval `scramv1 runtime -sh`
popd

combine -M MultiDimFit  --algo singles --setParameters r_VH=1 -d Full2016_whss.root --X-rtd MINIMIZER_analytic > Full2016_whss.out
combine -M MultiDimFit  --algo singles --setParameters r_VH=1 -d Full2017_whss.root --X-rtd MINIMIZER_analytic > Full2017_whss.out
combine -M MultiDimFit  --algo singles --setParameters r_VH=1 -d Full2018_whss.root --X-rtd MINIMIZER_analytic > Full2018_whss.out
combine -M MultiDimFit  --algo singles --setParameters r_VH=1 -d FullRunII_WHSS.root --X-rtd MINIMIZER_analytic > FullRunII_WHSS.out

combine -M MultiDimFit  --algo singles --setParameters r_VH=1 -d Full2016_whss_test.root --X-rtd MINIMIZER_analytic > Full2016_whss_test.out
combine -M MultiDimFit  --algo singles --setParameters r_VH=1 -d Full2017_whss_test.root --X-rtd MINIMIZER_analytic > Full2017_whss_test.out
combine -M MultiDimFit  --algo singles --setParameters r_VH=1 -d Full2018_whss_test.root --X-rtd MINIMIZER_analytic > Full2018_whss_test.out
combine -M MultiDimFit  --algo singles --setParameters r_VH=1 -d FullRunII_WHSS_test.root --X-rtd MINIMIZER_analytic > FullRunII_WHSS_test.out

combine -M Significance  --setParameters r_VH=1 -d Full2016_whss.root --X-rtd MINIMIZER_analytic > Full2016_signif_whss.out
combine -M Significance  --setParameters r_VH=1 -d Full2017_whss.root --X-rtd MINIMIZER_analytic > Full2017_signif_whss.out
combine -M Significance  --setParameters r_VH=1 -d Full2018_whss.root --X-rtd MINIMIZER_analytic > Full2018_signif_whss.out
combine -M Significance  --setParameters r_VH=1 -d FullRunII_WHSS.root --X-rtd MINIMIZER_analytic > FullRunII_signif_WHSS.out

combine -M Significance  --setParameters r_VH=1 -d Full2016_whss_test.root --X-rtd MINIMIZER_analytic > Full2016_signif_whss_test.out
combine -M Significance  --setParameters r_VH=1 -d Full2017_whss_test.root --X-rtd MINIMIZER_analytic > Full2017_signif_whss_test.out
combine -M Significance  --setParameters r_VH=1 -d Full2018_whss_test.root --X-rtd MINIMIZER_analytic > Full2018_signif_whss_test.out
combine -M Significance  --setParameters r_VH=1 -d FullRunII_WHSS_test.root --X-rtd MINIMIZER_analytic > FullRunII_signif_WHSS_test.out

