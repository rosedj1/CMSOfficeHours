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
- [Presentation](https://indico.cern.ch/event/602457/contributions/2435408/attachments/1434598/2205444/luisoni_powheg.pdf)
by Gionata Luisoni on LO vs. NLO math in MC production.

## Notes on MC generators

| MC Generator | What for it mean? | How to use it | Order |
| ------------ | ----------------- | --- |
| `Pythia8` | General purpose | | |
| `Herwig++` | General purpose | | |
| `POWHEG` | Matrix Element (ME) calculator| [How to use it](https://twiki.cern.ch/twiki/bin/viewauth/CMS/PowhegBOXPrecompiled#How_to_Run_a_POWHEG_gridpack_and) | NLO |
| `MadGraph5_amCatNLO` | ME calculator | [How to use it](https://twiki.cern.ch/twiki/bin/view/CMS/QuickGuideMadGraph5aMCatNLO) | |
| `Alpgen` | ME calculator | | |
| `JHUGen` | | | |
| `Tauola` | | | |
| `Delphes` | Fast multipurpose detector response simulation | [How to use it](https://cp3.irmp.ucl.ac.be/projects/delphes/wiki)| |

### Notes on ME generators

They usually produce an **LHE** (Les Houches Event) file,
which is just a big ASCII (txt) file with all the produced event info in it.

- LHE files are usually stored at: `/eos/cms/store/lhe/`
- Within CMSSW, typically the command `cmsRun`

## MadGraph

[Useful notes by Flip Tanedo](https://www.physics.uci.edu/~tanedo/files/notes/ColliderMadgraph.pdf)

- Includes how to install MadGraph, a tutorial on how to use it,
and the math behind it all.

### Tips and Tricks

Syntax of the `generate` command:

```bash
generate INITIAL STATE > REQ S-CHANNEL > FINAL STATE $ EXCL S-CHANNEL /
FORBIDDEN PARTICLES COUP1=ORDER1 COUP2=ORDER2 @N
# -- generate diagrams for a given process
# Example 1: generate l+ vl > w+ > l+ vl a $ z / a h QED=3 QCD=0 @1
# Example 2: generate p p > t t~ w+ [QCD]
# When a coupling order is specified or [QCD], the process is NLO.
# See: https://arxiv.org/pdf/1405.0301.pdf, pp. 64, 120.

# Alternative required s-channels can be separated by "|":
b b~ > W+ W- | H+ H- > ta+ vt ta- vt~
# If no coupling orders are given , MG5 will try to determine
# orders to ensure maximum number of QCD vertices.
# Note that if there are more than one non-QCD coupling type ,
# coupling orders need to be specified by hand.

# Decay chain syntax:
core process , decay1 , (decay2 , (decay2 ’, ...)), ... etc
# Example: p p > t~ t QED=0, (t~ > W- b~, W- > l- vl~), t > j j b @2
# Note that identical particles will all be decayed.
# To generate a second process use the "add process" command
```

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

## How to find info about a MC sample

[Monte-Carlo Request Management (MCM)](https://cms-pdmv.cern.ch/mcm/)

1. Go to MCM > Request > Output Dataset > search the full name of the sample.
1. Copy the PrepId (in the left-most column).
1. In the Dataset name column, click the little "chained request" symbol to see the history of the sample.
1. In the bottom-right, click "All" to show all results.
1. In the Chain column, search for the copied PrepId.
1. Click the generator PrepId (the first PrepId in the chain and usually contains 'LHEGS')

EITHER:

1. In the Actions column, click the Get dictionary icon (it's a down arrow).
1. Search for "https://" to find the fragment URL.
1. Go to this link and deduce whether LO, NLO, or NNLO.

OR:

1. Select View > check 'Fragment' > in the Fragment column, click the cross icon.

