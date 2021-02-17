# FWLite

Check out the [CMS Workbook](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookFWLitePython)
for using FWLite with Python.

## What is FWLite?

**FrameWork Lite (FWLite)** is an interactive analysis tool integrated with the CMSSW Event Data Model (EDM) Framework. It allows you to automatically load the shared libraries which define the CMSSW data formats and the tools provided, to easily access parts of the event in the EDM format within ROOT interactive sessions. It reads ROOT files, has full access to the class methods, and there is no need to write full-blown framework modules. Thus using FWLite allows you to do CMS analysis outside the full CMSSW framework.

## How to access FWLite

First do `cmsenv` under a CMSSW_X_Y_Z directory, then boot up the iPython interpreter
by typing `ipython` in your terminal. Now do:

```python
import ROOT
from DataFormats.FWLite import Events, Handle
```

If you did not get any errors, then you have imported **FWLite**!

### FWLite Example Script

```python
import ROOT
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.gSystem.Load("libDataFormatsFWLite.so")
ROOT.FWLiteEnabler.enable()
from DataFormats.FWLite import Events, Handle

events = Events("/path/to/MINIAOD_file.root")  # Events takes '.root' file.
hndl_muons = Handle('std::vector<pat::Muon>')  # Handle takes objects.
label = ("slimmedMuons", "", "PAT")

events.size()  # Total number of events.
for count,evt in enumerate(events):
    if count > 10: break
    evt.getByLabel(label, hndl_muons)
    muons = hndl_muons.product()
    if muons.size() > 0:
        print "-"*20
        for p in muons:
            print p.pdgId(), p.pt(), p.eta()
```

event object looks like:
`<DataFormats.FWLite.Events instance at 0x7f61ea583cf8>`

handle object looks like:
`std::vector<reco::GenParticle>`

From `edmDumpEventContent` of miniAOD file:

```bash
vector<pat::Electron>  "slimmedElectrons"  ""   "PAT"
vector<pat::Muon>      "slimmedMuons"      ""   "PAT"
```

Example command:

```bash
FWLiteHistograms inputFiles=slimMiniAOD_MC_MuEle.root outputFile=ZPeak_MC.root maxEvents=-1 outputEvery=100
```

## CMS Configuration Files

[FWCore.ParameterSet.Config](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookConfigFileIntro)

Many examples of `_cfg.py` can be found in:

- `/CMSSW/CMS.PhysicsTools/PatAlgos/test`
- `/CMSSW/CMS.PhysicsTools/PatExamples/test`

## Other Resources

- [How to write an EDAnalyzer.](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookWriteFrameworkModule?LOCALSHELL=bash)
- [More potentially useful examples/info on FWLite.](https://twiki.cern.ch/twiki/bin/view/Main/CMSSWCheatSheet#Other_possibly_useful_stuff)
