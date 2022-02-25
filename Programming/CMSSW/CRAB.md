# CRAB - CMS Remote Analysis Builder

CRAB: a utility to submit CMSSW jobs to distributed computing resources.

## Helpful Links

- https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideCrab
CRAB Tutorial
https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3AdvancedTutorial
CRAB FAQ
https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideCrabFaq
CRAB job errors:
https://twiki.cern.ch/twiki/bin/view/CMSPublic/JobExitCodes
CRAB Commands:
https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3Commands
CRAB Config File Parameters:
https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile
CRAB Publishing in DAS:
https://twiki.cern.ch/twiki/bin/view/CMSPublic/Crab3DataHandling#Publication_in_DBS

There is ONE Tier0 site: 
1. CERN
Seven T1 sites: 
1. USA
2. France
3. Spain
4. UK
5. Taiwan
6. Germany 
7. Italy
~55 T2 sites
You must specify config.Site.storageSite, which will depend on which center is hosting your area, and user_remote_dir which is the subdirectory of /store/user/ you want to write to. 
* Caltech storage_element = T2_US_Caltech 
* Florida storage_element = T2_US_Florida 
* MIT storage_element = T2_US_MIT 
* Nebraska storage_element = T2_US_Nebraska 
* Purdue storage_element = T2_US_Purdue 
* UCSD storage_element = T2_US_UCSD 
* Wisconsin storage_element = T2_US_Wisconsin 
* FNAL storage_element = T3_US_FNALLPC 
Check out all the tiers here:
https://cmsweb.cern.ch/sitedb/prod/sites

You need a CRAB config file in order to run an MC event generation code.
- The cmsDriver.py tool helps to generate config files
- Lucien's examples of crab_cfg.py files:
crab_GEN-SIM.py
crab_PUMix.py
crab_AODSIM.py
crab_MINIAODSIM.py

A typical CRAB config file looks like:

```python
from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'CMSDAS_Data_analysis_test0'
config.General.workArea = 'crab_projects'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'slimMiniAOD_data_MuEle_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.totalUnits = ??? 	# This limits how many "events" CRAB will run
config.Data.inputDataset = '/DoubleMuon/Run2016C-03Feb2017-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 50
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON.txt'
config.Data.runRange = '275776-275782'

config.section_("Site")
config.Site.storageSite = 'T2_US_Florida'
```

The /store/user/ area at LPC is commonly used for the output storage from CRAB jobs

How to make CRAB commands available: (must be in CMSSW environment)
cmsenv
source /cvmfs/cms.cern.ch/crab3/crab.sh		#.csh for c-shells

To check that it worked successfully, do:
which crab
> /cvmfs/cms.cern.ch/crab3/slc6_amd64_gcc493/cms/crabclient/3.3.1707.patch1/bin/crab
or:
crab --version
> CRAB client v3.3.1707.patch1

crab checkusername
> Retrieving username from SiteDB...
> Username is: drosenzw

Can also test your EOS area grid certificate link:
crab checkwrite --site=T3_US_FNALLPC	# checks to see if you have write permission at FNAL
crab checkwrite --site=T2_US_Nebraska
crab checkwrite --site=T2_US_Florida

Perhaps it is better to use low num jobs, high num events/job?

First you should run a job locally to make sure all is well:

```bash
cmsRun <step1_*_cfg.py>
```

Then submit to CRAB:

```bash
crab submit -c crabConfig_MC_generation.py
```

Resubmitting a failed CRAB job:

```bash
crab resubmit --siteblacklist='T2_US_Purdue' <crabdir1/crabdir2>  # don't submit to Purdue
# * N.B. only failed jobs get resubmitted
# * There are lots of flags to call to change things like memory usage, priority, sitewhitelist, etc.
# * --sitewhitelist=T2_US_Florida,T2_US_MIT
# * Can also use wildcards: --siteblacklist=T1_*
```

Resubmitting SPECIFIC CRAB jobs:

```bash
crab resubmit --force --jobids=1,5-10,15 <crabdir1/crabdir2>	# N.B. you must --force successful jobs to resubmit
```

***Check number of events from CRAB job*** (Very useful!)
crab report <crab_DIR>/<crab_job>

Check status:
crab status
crab status <crab_DIR>/<crab_job>

Kill a job:
crab kill -d <crab_DIR/crab_job>

For help with MC generation (step1):
https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCRAB3Tutorial#2_CRAB_configuration_file_to_run

Primary Dataset Names:
The primary dataset name of /GenericTTbar/HC-CMSSW_5_3_1_START53_V5-v1/GEN-SIM-RECO is GenericTTbar.

Different ways to interpret the dataset names:
/<primary-dataset>/<CERN-username_or_groupname>-<publication-name>-<pset-hash>/USER
/object_type/campaign/datatier
/Primary/Processed/Tier
/<DatasetName>/<Campaign-ProcessString-globalTag-Ext-Version>/<DataTier>

CRAB stores processed files (on my T2) with the following LFN: 
/store/[user|group|local]/<dir>[/<subdirs>]/<primary-dataset>/<publication-name>/<time-stamp>/<counter>[/log]/<file-name>
- /store/[user|group|local]/<dir>[/<subdirs>] = config.Data.outLFNDirBase
- <primary-dataset>   = config.Data.outputPrimaryDataset
- <publication-name> = config.Data.outputDatasetTag 

Storage path on your T2:
<config.Data.outLFNDirBase>/<config.Data.outputPrimaryDataset>/<config.Data.outputDatasetTag>

Helpful step_cfg.py arguments:
process.options = cms.untracked.PSet(
    numberOfThreads = cms.untracked.uint32(8),
)

## How to skip over lumi sections

1. Retrieve the notFinishedLumis.json with `crab report`.

2. Open the crab config file and change:
   2a. `config.General.requestName = whatever_missingLumis`
   2b. `config.Data.lumiMask = path/to/notFinishedLumis.json`

3. crab submit -c new_config.py
