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

- [Intro to MC Generation](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookGenIntro)
- https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookGeneration)

## Notes on MC generators

| MC Generator | What for it mean? | How to use it |
| ------------ | ----------------- | --- |
| `Pythia8` | General purpose | |
| `Herwig++` | General purpose | |
| `POWHEG` | Matrix Element (ME) calculator| [How to use it](https://twiki.cern.ch/twiki/bin/viewauth/CMS/PowhegBOXPrecompiled#How_to_Run_a_POWHEG_gridpack_and) |
| `MadGraph5_amCatNLO` | ME calculator | [How to use it](https://twiki.cern.ch/twiki/bin/view/CMS/QuickGuideMadGraph5aMCatNLO) |
| `Alpgen` | ME calculator | |
| `JHUGen` | | |

### Notes on ME generators

They usually produce an **LHE** (Les Houches Event) file,
which is just a big ASCII (txt) file with all the produced event info in it.

- LHE files are usually stored at: `/eos/cms/store/lhe/`
- Within CMSSW, typically the command `cmsRun`

### MadGraph

- [Tanedo's Personal Notes](https://www.physics.uci.edu/~tanedo/files/notes/ColliderMadgraph.pdf)
on how to install MadGraph and the math behind it all.

## Use CMSSW to generate events

`cmsDriver.py --help`

- [How to use cmsDriver](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideCmsDriver).