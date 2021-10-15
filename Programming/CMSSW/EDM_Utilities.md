# HEP Computing

## CMSSW

The CMS Collaboration uses CMS SoftWare (CMSSW) to analyze real and simulated data.
The main executable to process things is cleverly called `cmsRun`:

```bash
cmsRun your_config_file.py
```

You will need to do `cmsRun` on a **configuration file**, which usually ends in `_cfg.py`.
Here's an example of a config file:

```python
# Import CMS python class definitions such as Process, Source, and EDProducer
import FWCore.ParameterSet.Config as cms

# Import contents of a file
import Foo.Bar.somefile_cff

# Set up a process, named RECO in this case
process = cms.Process("RECO")

# Configure the object that reads the input file
process.source = cms.Source("PoolSource", 
    fileNames = cms.untracked.vstring("test.root")
)

# Configure an object that produces a new data object
process.tracker = cms.EDProducer("TrackFinderProducer")

# Configure the object that writes an output file
process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string("test2.root")
)

# Add the contents of Foo.Bar.somefile_cff to the process
# Note that more commonly in CMS, we call process.load(Foo.Bar.somefile_cff)
# which both performs the import and calls extend.
process.extend(Foo.Bar.somefile_cff)

# Configure a path and endpath to run the producer and output modules
process.p = cms.Path(process.tracker)
process.ep = cms.EndPath(process.out)
```

- [Guts of a config file.](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideAboutPythonConfigFile)
- [How to interactively inspect your cfg file.](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookConfigFileIntro)

---

## Build Files

Learn about build files [here](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookBuildFilesIntro).

## Redirectors

`root://cmsxrootd.fnal.gov//store/data/Run2016C/SingleMuon/...`

## EDM Utilities

[Event Data Model (EDM)](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookCMSSWFramework#EdM)
commands make it easy to look at the guts of MiniAOD files.

Say you want to analyze samples that come from this dataset:

```bash
/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM
```

You can find the associated root files on **DAS** or from the command line:

```bash
dasgoclient --query="file dataset=/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM" --format=plain
```

See what data are in the Event by doing `edmDumpEventContent your_file.root`.
The output should look like this:

```bash
Type                      Module                Label                         Process
--------------------------------------------------------------------------------------
LHEEventProduct           "source"              ""                            "LHE"
GenEventInfoProduct       "generator"           ""                            "SIM"
edm::ValueMap<bool>       "muons"               "muidGlobalMuonPromptTight"   "RECO"
...
```

- **Type:** The C++ class type of the data.
- **module label:** The label assigned to the module that created the data.
- **product instance label:** The label assigned to the object from within the module.
- **process name:** The  process name as set in the job that created the data.

Try printing out the [collections](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideRecoDataTable) in your MiniAOD file:

```bash
edmEventSize -v your_file.root
```

Commands:

- `edmFileUtil`: uses a LFN (logical file name, an alias used for any site) to find a PFN (physical file name, actual file path)
- `edmDumpEventContent`: see what class names etc. to use in order to access the objects in the MiniAOD file
- `edmProvDump`: Prov=Provenance (origin, source, history), one can print out all the tracked parameters used to create the data file. For example, one can see which modules were run and the CMSSW version used to make the MiniAOD file.
- `edmEventSize`: determines size of different branches
- `edmPickEvents`: search a data set for a particular event.

```bash
# Run over a specific Run:LumiSect:Event
edmPickEvents.py "/DoubleMuon/Run2018D-PromptReco-v2/MINIAOD" 321834:84:126135620
```

```bash
files=( /DoubleMuon/Run2018D-PromptReco-v2/MINIAOD )
files+=( /EGamma/Run2018D-22Jan2019-v2/MINIAOD )
files+=( /EGamma/Run2018D-PromptReco-v2/MINIAOD )
for f in "${files[@]}"; do
    edmPickEvents.py "${f}" 321834:84:126135620
done
```

## Examples

For any of the below commands, you can do: `<cmd> --help`

```bash
edmFileUtil -d /store/relval/CMSSW_10_2_0/RelValZMM_13/MINIAODSIM/PUpmx25ns_102X_upgrade2018_realistic_v9_gcc7-v1/10000/3017E7A1-178D-E811-8F63-0025905A6070.root
```

Output:

```bash
root://cmsxrootd-site.fnal.gov//store/relval/CMSSW_10_2_0/RelValZMM_13/MINIAODSIM/PUpmx25ns_102X_upgrade2018_realistic_v9_gcc7-v1/10000/3017E7A1-178D-E811-8F63-0025905A6070.root
```

Other ways to use these commands:

```bash
edmDumpEventContent --all myfile.root
edmDumpEventContent --all --regex slimmedMuons root://cmsxrootd.fnal.gov//store/user/cmsdas/2019/pre_exercises/0EE14BA8-41BB-E611-AD2F-0CC47A4D760A.root 
```

>>> spits out info about class names to access objects in MiniAOD file
- the columns are: (1) type of data, (2) module label, (3) product instance label, (4) process name

edmProvDump root://cmseos.fnal.gov//store/user/cmsdas/2019/pre_exercises/0EE14BA8-41BB-E611-AD2F-0CC47A4D760A.root > EdmProvDump.txt

edmEventSize -v `edmFileUtil -d /store/user/cmsdas/2019/pre_exercises/0EE14BA8-41BB-E611-AD2F-0CC47A4D760A.root` > EdmEventSize.txt 
edmEventSize -v slimMiniAOD_MC_MuEle.root

The main contents of the MiniAOD are:

- High level physics objects (leptons, photons, jets, ETmiss), with detailed information in order to allow e.g. retuning of identification criteria, saved using PAT dataformats. Some preselection requirements are applied on the objects, and objects failing these requirements are either not stored or stored only with a more limited set of information. Some high level corrections are applied: L1+L2+L3(+residual) corrections to jets, type1 corrections to ETmiss.
- The full list of particles reconstructed by the ParticleFlow, though only storing the most basic quantities for each object (4-vector, impact parameter, pdg id, some quality flags), and with reduced numerical precision; these are useful to recompute isolation, or to perform jet substructure studies. For charged particles with pT > 0.9 GeV, more information about the associated track is saved, including the covariance matrix, so that they can be used for b-tagging purposes.
- MC Truth information: a subset of the genParticles enough to describe the hard scattering process, jet flavour information, and final state leptons and photons; GenJets with pT > 8 GeV are also stored, and so are the other mc summary information (e.g event weight, LHE header, PDF, PU information). In addition, all the stable genParticles with mc status code 1 are also saved, to allow reclustering of GenJets with different algorithms and substructure studies. 
- Trigger information: MiniAOD contains the trigger bits associated to all paths, and all the trigger objects that have contributed to firing at least one filter within the trigger. In addition, we store all objects reconstructed at L1 and the L1 global trigger summary, and the prescale values of all the triggers.

Data within an Event are identified by 4 quantities:

1. Types:edm::PSimHitContainer, reco::TrackCollection, etc.
2. Module Label (label assigned to module that created the data):"SimG4Objects" or "TrackProducer"
3. Product Instance Label (label assigned to object from within module):"default", "picky", "first hit"
4. Process Name

## Resources
