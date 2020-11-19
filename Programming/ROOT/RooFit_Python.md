# RooFit Python

Make an independent variable `x`:

```python
import ROOT as r
x = r.RooRealVar("x", "The Independent Variable", 0, 500, "GeV")  # (name, title, min, max, units)
x.setBins(50)
x.getBins()  # Returns the number of bins.
x.setRange('fit_region', 105, 140)
x.getTitle()  # Returns the title of the variable.
x.getUnit()  # Returns the unit.
x.getMax()  # Returns the max possible? or max populated within x?
```

A `RooRealVar` can make a `frame`:

```python
frame = x.frame()
# Add a title.
frame = x.frame(r.RooFit.Title("A title for the frame"))

# Some frame methods:
frame.numItems()          # Number of members in frame.
frame.nameOf(2)           # Name (str) of second member in frame.
statsbox = frame.findObject("stats")  # After a hist, etc. has drawn stats.
obj = frame.getObject(3)  # Get the third object stored in the frame. USEFUL!
frame.remove("stats")     # Remove the stats box from the frame.
frame.Draw("same")        # Can also try "same axis".
frame.Print()             # See what objects are in your frame.
# See what their names are:
for index in range(int(frame.numItems())):
   print(f"object #{index}: {frame_corr.nameOf(index)}")
```

How some of these work:

```python
massZ = RooRealVar("name", "title", value, min, max)
RooArgSet(w.var.("massZErr"))
RooArgList(lambda_,  massZErr)
RooFormulaVar("sigma","@1*@0", RooArgList(lambda_,  massZErr))
```

Build a **workspace** to organize your objects:

```python
w = ROOT.RooWorkspace('w')
```

Then you can add things to the workspace, like variables, pdfs, and factories:

```python
w.factory('Gaussian::g(x[-5,5],mu[-3,3],sigma[1])')  # Defines a Gaussian and ranges for x, mu, sigma.
w.factory('Exponential::e(x,tau[-0.5,-3,0])')
w.factory('SUM::model(s[50,0,100]*g, b[100,0,1000]*e)')
```

- This factory is going to add the two pdfs together per event.
- We expect the signal (s) to have around 50 events, but it can span 0 to 100. It will have a Gaussian (g) shape.
- More info about [`factory()`](https://root.cern.ch/doc/master/classRooWorkspace.html#a0ddded1d65f5c6c4732a7a3daa8d16b0)

Useful workspace methods:

```python
w.Print()    # See what's inside your workspace.
```

Generic fitting routine:

```python
x = w.var('x')
pdf = w.pdf('model')
frame = x.frame()
data = pdf.generate(ROOT.RooArgSet(x))
data.plotOn(frame)
fit_result = pdf.fitTo(data)
fit_result = pdf.fitTo(data, ROOT.RooFit.Save(), ROOT.RooFit.PrintLevel(-1))
pdf.plotOn(frame)
frame.Draw()
```

```python
mean = r.RooRealVar("mean","Mean of Gaussian",-10,10)
sigma = r.RooRealVar("sigma","Width of Gaussian",3,-10,10, "GeV")  # Can assign units to var.
gauss = r.RooGaussian("gauss","The Gaussian PDF",x,mean,sigma)

# View fit values:
fit_result = my_pdf.fitTo(roodataset)
fit_result.Print()
# - fit values (e.g. "my_mean") will get printed

#Retrieve fit values:
w.var("my_mean").getVal()	# 

w.pdf(<RooAddPdf>).fitTo(<RooDataSet>)

Different Built-In PDFs:
bw = RooBreitWigner("<name>", "<title>", <var>, <mean>, <gamma>)
cb = RooCBShape("<name>", "<title>", <var>, <mean>, <sigma>, <alpha>, <n>)
ex = RooExponential("name", "title", <var>, tau)
voigt = RooVoigtian()

Convolute PDFs:
RooFFTConvPdf("name", "title", variable, pdf1, pdf2)

import ROOT as r
rds = RooDataSet("rds","dataset from tree", tree, r.RooArgSet(x))
rds = RooDataSet("rds","dataset from tree", tree, r.RooArgSet(x), "cut string")  # Needs testing.
rds = RooDataSet('data', 'dataset', r.RooFit.Import(tree), r.RooArgSet(rooVar), r.RooFit.Cut(Cut + ' && 1' ))  # Needs testing.
```

## Useful RooDataSet methods:

```python
rds.SaveAs('my_RooDataSet.root')  # FIXME: Test this.
rds.Print()       # get basic info about dataset
rds.numEntries()  # get entries of the dataset
rds.sumEntries()  # Fast method than rds.numEntries()?
rds.ls()          # get a little info about dataset
rds.get()         # returns the coordinates of the current RooArgSet (vectors?)
rds.GetName()     # returns name
rds.GetTitle()    # returns title
rds.add(<val>)    # add some value to your dataset?
rds.reduce(RooFit.Cut(cuts_str))  # Applies cuts to dataset?
```

Convolute PDFs into a RooAbsPdf object (sig+bkg model):
```python
CBxBW  = RooFFTConvPdf("CBxBW","CBxBW", massZ, BW, CB)
bkg = RooExponential("bkg","bkg", massZ, tau)
fsig = RooRealVar("fsig","signal fraction", self.shapePara["fsig"])
model = RooAddPdf("model","model", CBxBW, bkg, fsig)

import ROOT as r
p = r.RooRealVar(‘x’,’x’,6.9,0,15)

w = r.RooWorkspace(‘w’)
w.factory(‘x[6.8,0,15]’)
```

## How to do an unbinned fit

Example below shows an unbinned **Gaussian** fit:

```python
import ROOT as r
data = np.array(my_fancy_data_to_be_fit)

min_ = data.min()
max_ = data.max()
avg_ = data.mean()
std_ = data.std()

x = r.RooRealVar("x","x", min_, max_)
mean = r.RooRealVar("mean","Mean of Gaussian", avg_, min_, max_)
sigma = r.RooRealVar("sigma","Width of Gaussian", std_, 0, 1000)
gauss = r.RooGaussian("gauss","gauss(x,mean,sigma)", x, mean, sigma)

# Make RooDataSet.
ptr = array('f', [0.])
tree = ROOT.TTree("tree", "tree")
tree.Branch("x", ptr, "x/F")
for val in data:
   ptr[0] = val
   tree.Fill()
rds = ROOT.RooDataSet("rds","dataset from tree", tree, ROOT.RooArgSet(x))

# Modify fit range, if needed.
fit_x_min = x_min + 3
fit_x_max = x_max - 4.5

# Find and fill the mean and sigma variables.
result = gauss.fitTo(rds,
                     r.RooFit.PrintLevel(-1),  # Prints fewer details to screen.
                     r.RooFit.Range(fit_x_min, fit_x_max)
         )

fit_stats_ls = [mean.getVal(), mean.getError(), sigma.getVal(), sigma.getError()]
```

## More info here: https://github.com/clelange/roofit/blob/master/rf108_plotbinning.py

```python
xframe = x.frame(r.RooFit.Range(-15, 15),
                  r.RooFit.Title("x distribution with custom binning"))
data.plotOn(xframe, r.RooFit.Binning(30))  # Use only 30 bins.

c = r.TCanvas("c_plotbinning", "Playing with plotbinning", 800, 400)
# Split the canvas up into 2 pads.
c.Divide(2)
# Go into the first pad.
c.cd(1)
ROOT.gPad.SetLeftMargin(0.15)
dtframe.GetYaxis().SetTitleOffset(1.6)
dtframe.Draw()
c.cd(2)
ROOT.gPad.SetLeftMargin(0.15)
aframe.GetYaxis().SetTitleOffset(1.6)
aframe.Draw()

c.SaveAs("rf108_plotbinning.png")
```

## Other Resources on RooFit

- [A short Jupyter Notebook using PyROOT](https://www.nikhef.nl/~vcroft/GettingStartedWithRooFit.html)
- [Hands-on Advanced Tutorials](https://lpc.fnal.gov/programs/schools-workshops/hats.shtml) (HATS)
  - Will require access to Indico.

# HZZ Analyzer for CMS Run2

## How to install the Analyzer

```bash
# Prepare your area.
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_6_12
cd CMSSW_10_6_12/src
cmsenv

# Install the repo.
git cms-init
git clone -b 10_6_12 https://ferrico@github.com/ferrico/UFHZZAnalysisRun2.git
git config merge.renameLimit 999999
cp UFHZZAnalysisRun2/install*.sh .
chmod u+x install_2.sh
./install_2.sh
```

## How to use the Analyzer

Now you can run over the template files found in `UFHZZAnalysisRun2/UFHZZ4LAna/python/`:

```bash
cmsRun UFHZZAnalysisRun2/UFHZZ4LAna/python/Sync_102X_2016_Legacy_cfg.py
cmsRun UFHZZAnalysisRun2/UFHZZ4LAna/python/Sync_102X_2017_Legacy_cfg.py
cmsRun UFHZZAnalysisRun2/UFHZZ4LAna/python/Sync_102X_2018_Legacy_cfg.py
```

Only run over **a maximum of 10K events** locally.
If you need to run over more, then you should submit a CRAB job:

```bash
cp UFHZZAnalysisRun2/Utilities/crab/* .
# Initialize your proxy. If you get errors, check your certificate.
# May need to instead do: `voms-proxy-init -voms cms -rfc`
voms-proxy-init --valid=168:00
source /cvmfs/cms.cern.ch/crab3/crab.sh

# Submit your job:
python SubmitCrabJobs.py -t "myTask_Data" -d datasets_2016ReReco.txt -c UFHZZAnalysisRun2/UFHZZ4LAna/python/templateData_80X_M1703Feb_2l_cfg.py

# or similary for MC:
python SubmitCrabJobs.py -t "myTask_MC" -d datasets_Summer16_25ns_MiniAOD.txt -c UFHZZAnalysisRun2/UFHZZ4LAna/python/templateMC_80X_M17_4l_cfg.py
```

### Check the status of your job

You can use manageCrabTask.py to check the status, resubmit, or kill your task. E.g. after submitting:

```bash
nohup python -u manageCrabTask.py -t resultsAna_Data_M17_Feb19 -r -l >& managedata.log &
```

This will start an infinite loop of running crab resubmit on all of your tasks, then sleep for 30min.
You should kill the process once all of your tasks are done.
Once all of your tasks are done, you should run the following command to purge your crab cache so that it doesn't fill up:

```bash
python manageCrabTask.py -t resultsAna_Data_M17_Feb19 -p
```

## Useful templates

```bash
UFHZZ4LAna/python/templateMC_102X_Legacy16_4l_cfg.py
UFHZZ4LAna/python/templateMC_102X_Legacy17_4l_cfg.py
UFHZZ4LAna/python/templateMC_102X_Legacy18_4l_cfg.py
UFHZZ4LAna/python/templateData_102X_Legacy16_3l_cfg.py
UFHZZ4LAna/python/templateData_102X_Legacy17_3l_cfg.py
UFHZZ4LAna/python/templateData_102X_Legacy18_3l_cfg.py
```