# FWLite

Check out the [CMS Workbook](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookFWLitePython) 
for using FWLite with Python.

## _What is FWLite?_

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
from DataFormats.FWLite import Events, Handle

events = Events("/path/to/MINIAOD_file.root")      # Events takes '.root' file.
handle = Handle('std::vector<reco::GenParticle>')  # Handle takes objects.
label = ("genParticles", "", "GEN")

for count,e in enumerate(events):
    if count > 10: continue
    e.getByLabel(label,handle)
    genParticles = handle.product()     # No longer genParticles
    print "-"*20
    for p in genParticles:
        if not p.isHardProcess(): continue
        print p.pdgId(),p.pt(),p.eta()
```

event object looks like:
<DataFormats.FWLite.Events instance at 0x7f61ea583cf8>
handle object looks like:
std::vector<reco::GenParticle>

From edmDumpEventContent of miniAOD file:
vector<pat::Electron>  "slimmedElectrons"  ""   "PAT"     
vector<pat::Muon>      "slimmedMuons"      ""   "PAT"     

Define a label tuple for the last three columns:
label = ("slimmedElectrons","","PAT")
Then can do:
e.get


handle.product(): 
<ROOT.vector<pat::Electron> object at 0x10172dd0>

```python
import ROOT
ROOT.gSystem.Load("libFWCoreFWLite.so")
ROOT.gSystem.Load("libDataFormatsFWLite.so")
ROOT.FWLiteEnabler.enable()
from DataFormats.FWLite import Events, Handle

DeltaR = ROOT.Math.VectorUtil.DeltaR
DeltaR2 = lambda a, b: DeltaR(a.p4(), b.p4())
DeltaPhi = ROOT.Math.VectorUtil.DeltaPhi
DeltaPhi2 = lambda a, b: DeltaPhi(a.p4(), b.p4())

events = Events("/path/to/MINIAOD_file.root")
hndl_muons = Handle('std::vector<pat::Muon>')
label = ("slimmedMuons", "", "PAT")

hist_muon_pt = ROOT.TH1D('muon_pt', ';leading muon: P_{T};events', 50, 0., 500.)

for evt in events:
    evt.getByLabel('slimmedMuons', hndl_muons)
    muons = hndl_muons.product()
    if muons.size():
        hist_muon_pt.Fill( muons[0].pt() )

# Make a ROOT file:
# hist_muon_pt.SaveAs("/home/rosedj1/public_html/FWLite_Practice/Test_Plots/firstplot.root")

# Draw the histogram.
c_first = ROOT.TCanvas("c_first", "Let's plot this purdy boi")
hist_muon_pt.Draw("hist e1")


# Alternate way:
for count, event in enumerate(events):
    if count > 10: break
    event.getByLabel(label, handle)
    patParticles = handle.product()
     
    for p in patParticles:
        print p.pdgId(), p.pt(), p.eta()
```

Example command:
```bash
FWLiteHistograms inputFiles=slimMiniAOD_MC_MuEle.root outputFile=ZPeak_MC.root maxEvents=-1 outputEvery=100
```

[More potentially useful examples/info on FWLite.](https://twiki.cern.ch/twiki/bin/view/Main/CMSSWCheatSheet#Other_possibly_useful_stuff)

@@ 
Test this *section* for markdown.
It should _not_ have *any special _markdown_* whatsoever. 