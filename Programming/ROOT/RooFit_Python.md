# RooFit Python

RooFit is an **incredibly powerful statistics package** that uses ROOT.

## The Basics

_Everything_ in RooFit is its own object.
For example, the independent variable `x`:

```python
import ROOT as r
x = r.RooRealVar("x", "The Independent Variable", 0, 500, "GeV")  # (name, title, min, max, units)
# Now `x` has its own set of methods, like:
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

### Build a **workspace** to organize your objects

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

### Generic fitting routine

```python
x = w.var('x')        # Independent variable.
pdf = w.pdf('model')  # The function to describe the data.
frame = x.frame()     # The axes.
data = pdf.generate(ROOT.RooArgSet(x))  # The data themselves.
data.plotOn(frame)    # Draw it on your axes.
result = pdf.fitTo(data)  # Fit the pdf onto the data. Store the info for later.
result = pdf.fitTo(data, ROOT.RooFit.Save(), ROOT.RooFit.PrintLevel(-1))
pdf.plotOn(frame)
frame.Draw()
```

Useful fit result methods:

```python
# Do the fit:
result = my_pdf.fitTo(roodataset)

# View fit values:
result.Print()
result.Print("v")  # Verbose.
list(result.floatParsFinal())
# View the value of a fit parameter which you named "mean":
result.floatParsFinal().find("mean").getVal()
result.correlationHist()

# Other fit info:
result.edm()  # ??
result.minNll()  # Minimum of negative log likelihood.
result.correlation("bkgfrac", "mean")  # Correlation between 2 variables.
result.correlationMatrix()
result.covarianceMatrix() 

# Save your fit info to a ROOT file.
f = ROOT.TFile("myfitresult.root", "RECREATE")
result.Write("stored_fit_result")
f.Close()
# Retrieve it:
result = gDirectory.Get("stored_fit_result")

# Plot it if you want.
result.plotOn(frame, sigma1, sig1frac, "ME12ABHV")
   # M - a marker at the best fit result
   # E - an error ellipse calculated at 1-sigma using the error matrix at the minimum
   # 1 - the 1-sigma error bar for parameter 1
   # 2 - the 1-sigma error bar for parameter 2
   # B - the bounding box for the error ellipse
   # H - a line and horizontal axis for reading off the correlation coefficient
   # V - a line and vertical axis for reading off the correlation coefficient
   # A - draw axes for reading off the correlation coefficients with the H or V options
```

```python
mean = r.RooRealVar("mean","Mean of Gaussian",-10,10)
sigma = r.RooRealVar("sigma","Width of Gaussian",3,-10,10, "GeV")  # Can assign units to var.
gauss = r.RooGaussian("gauss","The Gaussian PDF",x,mean,sigma)

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

## Useful RooDataSet methods

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

### Random dude's example of PyROOT RooFit code

```python
import ROOT

x = ROOT.RooRealVar("x", "x", -5, 5)
mu = ROOT.RooRealVar("mu", "mu", 0, -1, 1)
sigma = ROOT.RooRealVar("sigma", "sigma", 1, 0.1, 2)
pdf = ROOT.RooGaussian("gaus", "gaus", x, mu, sigma)

data = pdf.generate(ROOT.RooArgSet(x), 10000)

pdf.fitTo(data)

frame = x.frame()
data.plotOn(frame)
pdf.plotOn(frame)

pdf.paramOn(frame,
            ROOT.RooFit.FillColor(ROOT.kRed),
            ROOT.RooFit.Label("Global Fit parameters:"),
            ROOT.RooFit.Layout(0.1, 0.4, 0.9),
            ROOT.RooFit.Format("NEU", ROOT.RooFit.AutoPrecision(1)),
            ROOT.RooFit.ShowConstants())

canvas = ROOT.TCanvas()
frame.Draw()

# I really don't like this
canvas.GetListOfPrimitives().FindObject("gaus_paramBox").SetTextColor(ROOT.kRed)
# this crash my computer:
canvas.GetListOfPrimitives().FindObject("gaus_paramBox").SetTextSize(0.025)
```