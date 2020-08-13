# Monte Carlo Generation and Simulation

A Monte Carlo (MC) generator is a program which simulates particle collisions and all the produced, outgoing particles.
These events are often called **generated** events.

Once the outgoing, fictitous particles have been produced,
they can "go through your detector" -
these are called **simulated** events.

Finally, all of the simulated hits of particles passing through your detector need to be **reconstructed**.
Reconstructed events are built using fancy, connect-the-dots routines.

**Note:**
The term *particle gun* can also be thought of as a "particle beam".
The MC generator makes lots of events with a specific type of particle,
with specified kinematics (pT, eta, etc.).
This way we get *loads* of a single kind of particle.
You may want to shoot a muon gun through the CSCs of CMS
to test a new kind of trigger, for example.

## Resources

- [OpenData intro to MC](http://opendata.cern.ch/docs/cms-mc-production-overview)
- [TWiki: Intro to MC Generation](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookGenIntro)
- [TWiki: Another CMS Workbook](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookGeneration)

## Notes on MC generators

| MC Generator | What for it mean? | How to use it |
| ------------ | ----------------- | --- |
| `Pythia8` | General purpose | |
| `Herwig++` | General purpose | |
| `POWHEG` | Matrix Element (ME) calculator| [How to use it](https://twiki.cern.ch/twiki/bin/viewauth/CMS/PowhegBOXPrecompiled#How_to_Run_a_POWHEG_gridpack_and) |
| `MadGraph5_amCatNLO` | ME calculator | [How to use it](https://twiki.cern.ch/twiki/bin/view/CMS/QuickGuideMadGraph5aMCatNLO) |
| `Alpgen` | ME calculator | |
| `JHUGen` | | |
| `Tauola` | | |
| `Delphes` | Fast multipurpose detector response simulation | [How to use it](https://cp3.irmp.ucl.ac.be/projects/delphes/wiki)| 

### Notes on ME generators

They usually produce an **LHE** (Les Houches Event) file,
which is just a big ASCII (txt) file with all the produced event info in it.

- LHE files are usually stored at: `/eos/cms/store/lhe/`
- Within CMSSW, typically the command `cmsRun`

### MadGraph

- [Tanedo's Personal Notes](https://www.physics.uci.edu/~tanedo/files/notes/ColliderMadgraph.pdf)
on how to install MadGraph and the math behind it all.

---

## Use CMSSW to generate events

You can build any configuration file out of the large collection of CMSSW pre-fabricated configuration application fragments by using `cmsDriver.py`.

- To get this script, simply do: `cmsenv` under a CMSSW dir.
- Help menu: `cmsDriver.py --help`
- [How to use cmsDriver](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideCmsDriver).

Here's a picture that shows the general MC workflow:
![wordshere](https://twiki.cern.ch/twiki/pub/CMS/PdmVAnalysisSummaryTable/AnalysisSummaryTable_20200609.png)

https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmVAnalysisSummaryTable

### How to make GEN-SIM events

First install the Generator package into your CMSSW area:

```bash
cmsrel CMSSW_10_2_18
cd CMSSW_10_2_18/src/
cmsenv        # Set CMS environment variables.
mkdir -p Configuration/Generator/python/
cd !$         # Fancy way of `cd`ing into that new dir.
# Now go grab your favorite GEN fragment from:
# https://github.com/cms-sw/cmssw/tree/master/Configuration/Generator/python
# and place it into your Configuration/Generator/python/ dir.
scram b -j 8  # Compile everything.
```

Monte Carlo generator **fragments** live in `Configuration/Generator/python/`.

- A "fragment" file is the initial script used to start the MC process.
- These configuration files usually end in `*_cfi.py` or `*_cff.py`.
- Use `cmsDriver.py` on a fragment to generate a "step1" config file (the GEN-SIM step):

```bash
cmsDriver.py ZMM_13TeV_TuneCUETP8M1_cfi  --conditions auto:run2_mc -n 10 --era Run2_2018 --eventcontent RAWSIM --step GEN,SIM --datatier GEN-SIM --beamspot Realistic25ns13TeVEarly2018Collision --no-exec
```
