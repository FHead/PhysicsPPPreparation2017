# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: hlt -s RAW2DIGI,L1Reco,RECO,HLT:HighPTV42Legacy,EI,DQM -n 200 --filein root://xrootd.cmsaf.mit.edu//store/user/gsfs/Pythia8_TTBar_pp_CUETP8M1_5020GeV/RAW_20171007/171009_115554/0000/step2_pp_DIGI_L1_DIGI2RAW_HLT_1.root --eventcontent DQM --datatier DQMIO --conditions 92X_upgrade2017_realistic_v11 --mc --process reHLT --hltProcess reHLT --era=Run2_2017
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('reHLT',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('HLTrigger.Configuration.HLT_HighPTV42Legacy_cff')
process.load('CommonTools.ParticleFlow.EITopPAG_cff')
process.load('DQMOffline.Configuration.DQMOfflineMC_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(200)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('root://xrootd.cmsaf.mit.edu//store/user/gsfs/Pythia8_TTBar_pp_CUETP8M1_5020GeV/RAW_20171007/171009_115554/0000/step2_pp_DIGI_L1_DIGI2RAW_HLT_1.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('hlt nevts:200'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.DQMoutput = cms.OutputModule("DQMRootOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('DQMIO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('hlt_RAW2DIGI_L1Reco_RECO_HLT_EI_DQM.root'),
    outputCommands = process.DQMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from HLTrigger.Configuration.CustomConfigs import ProcessName
process = ProcessName(process)

from Configuration.Applications.ConfigBuilder import ConfigBuilder
process.DQMOffline.visit(ConfigBuilder.MassSearchReplaceProcessNameVisitor("HLT", "reHLT", whitelist = ("subSystemFolder",)))
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '92X_upgrade2017_realistic_v11', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.eventinterpretaion_step = cms.Path(process.EIsequence)
process.dqmoffline_step = cms.EndPath(process.DQMOffline)
process.dqmofflineOnPAT_step = cms.EndPath(process.DQMOffline)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)

process.load('HLTrigger.HLTanalyzers.HLTBitAnalyser_cfi')
process.hltbitanalysis.HLTProcessName = cms.string('reHLT')
process.hltbitanalysis.hltresults = cms.InputTag( 'TriggerResults','','reHLT')
process.hltbitanalysis.l1GtReadoutRecord = cms.InputTag('simGtDigis','','reHLT')
process.hltbitanalysis.l1GctHFBitCounts = cms.InputTag('gctDigis','','reHLT')
process.hltbitanalysis.l1GctHFRingSums = cms.InputTag('gctDigis','','reHLT')
process.hltbitanalysis.UseTFileService = cms.untracked.bool(True)
process.hltBitAnalysis = cms.EndPath(process.hltbitanalysis)
process.TFileService = cms.Service('TFileService', fileName = cms.string('openHLT___JOB__.root'))

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.eventinterpretaion_step,process.dqmoffline_step,process.dqmofflineOnPAT_step,process.DQMoutput_step,process.hltBitAnalysis])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)



# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
