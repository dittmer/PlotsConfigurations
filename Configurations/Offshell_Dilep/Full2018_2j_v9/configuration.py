# example of configuration file
treeName= 'Events'

tag = 'hww_offshell_UL_2018'


# used by mkShape to define output directory for root files
outputDir = 'rootFile'
# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py' 

# file with list of samples
samplesFile = 'samples.py' 

# file with list of samples
plotFile = 'plot.py' 



# luminosity to normalize to (in 1/fb)
lumi = 59.83

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
# outputDirPlots = '~/www/plotCR'
outputDirPlots = 'plots_2017'

# used by mkDatacards to define output directory for datacards
outputDirDatacard =  'datacards_2017'



# structure file for datacard
structureFile = 'structure.py'


# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'

