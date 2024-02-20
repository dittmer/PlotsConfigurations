# example of configuration file
treeName= 'Events'

tag = 'hww_offshell_UL_2018'


# used by mkShape to define output directory for root files
eos_space = '/../../../../../../../../../../../../../eos/user/j/jrotter/Latinos_RootFiles/'
outputDir = eos_space + 'Full2018_2j_v9_W_SYST/rootFiles'

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
outputDirPlots = eos_space + '../www/BLINDED_W_SYST_Full2018_2j_v9'#'Full2018_2j_v9/plots_2018'


# used by mkDatacards to define output directory for datacards
outputDirDatacard = eos_space + 'Full2018_2j_v9_W_SYST/datacards_2018'


# structure file for datacard
structureFile = 'structure.py'


# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'

