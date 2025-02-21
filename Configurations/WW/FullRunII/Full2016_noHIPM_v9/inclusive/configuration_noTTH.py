# Configuration file to produce initial root files -- has both merged and binned ggH samples

treeName = 'Events'

tag = 'WW2016_noHIPM_v9_incl_noTTH'

# used by mkShape to define output directory for root files
outputDir = 'rootFile_JES_noTTH'

# file with TTree aliases
aliasesFile = 'aliases_noTTH.py'

# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py' 

# file with list of samples
samplesFile = 'samples.py' 

# file with list of samples
plotFile = 'plot.py' 

# luminosity to normalize to (in 1/fb)
lumi = 16.81 

# used by mkPlot to define output directory for plots
outputDirPlots = 'plots_JES_noTTH'

# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards_JES_noTTH'

# structure file for datacard
structureFile = 'structure.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances_noTTH.py'
