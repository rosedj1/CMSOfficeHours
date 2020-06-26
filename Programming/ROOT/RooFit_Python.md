# RooFit Python

Make an independent variable `x`:

```python
x = ROOT.RooRealVar("x","The Independent Variable",-10,10)  # (name, title, min, max)
x.setBins(50)
x.setRange('fit_region', 105, 140)
x.getBins()  # Returns the number of bins.
x.getTitle()  # Returns the title of the variable.
x.getUnit()  # Returns the unit.
x.getMax()  # Returns the max possible? or max populated within x?
```
How some of these work:
massZ = RooRealVar("name", "title", value, min, max)
RooArgSet(w.var.("massZErr"))
RooArgList(lambda_,  massZErr)
RooFormulaVar("sigma","@1*@0", RooArgList(lambda_,  massZErr))

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

Useful workspace methods:

```python
w.Print()    # See what's inside your workspace.
```

Generic fitting routine:
x = w.var('x')
pdf = w.pdf('model')
frame = x.frame()
data = pdf.generate(ROOT.RooArgSet(x))
data.plotOn(frame)
fit_result = pdf.fitTo(data)
fit_result = pdf.fitTo(data, ROOT.RooFit.Save(), ROOT.RooFit.PrintLevel(-1))
pdf.plotOn(frame)
frame.Draw()

```python
mean = ROOT.RooRealVar("mean","Mean of Gaussian",-10,10)
sigma = ROOT.RooRealVar("sigma","Width of Gaussian",3,-10,10, "GeV")  # Can assign units to var.
gauss = ROOT.RooGaussian("gauss","gauss(x,mean,sigma)",x,mean,sigma)
```

View fit values:
fit_result = my_pdf.fitTo(roodataset)
fit_result.Print()
- fit values (e.g. "my_mean") will get printed

Retrieve fit values:
w.var("my_mean").getVal()	# 

w.pdf(<RooAddPdf>).fitTo(<RooDataSet>)

Different Built-In PDFs:
bw = RooBreitWigner("<name>", "<title>", <var>, <mean>, <gamma>)
cb = RooCBShape("<name>", "<title>", <var>, <mean>, <sigma>, <alpha>, <n>)
ex = RooExponential("name", "title", <var>, tau)
voigt = RooVoigtian()

Convolute PDFs:
RooFFTConvPdf("name", "title", variable, pdf1, pdf2)

```python
import ROOT as r
rds = RooDataSet("rds","dataset from tree", tree, r.RooArgSet(x))
rds = RooDataSet("rds","dataset from tree", tree, r.RooArgSet(x), "cut string")  # Needs testing.
rds = RooDataSet('data', 'dataset', r.RooFit.Import(tree), r.RooArgSet(rooVar), r.RooFit.Cut(Cut + ' && 1' ))  # Needs testing.
```

Useful RooDataSet methods:

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
CBxBW     = RooFFTConvPdf("CBxBW","CBxBW", massZ, BW, CB)
bkg = RooExponential("bkg","bkg", massZ, tau)
fsig = RooRealVar("fsig","signal fraction", self.shapePara["fsig"])
model = RooAddPdf("model","model", CBxBW, bkg, fsig)

import ROOT as rt
p = rt.RooRealVar(‘x’,’x’,6.9,0,15)

w = rt.RooWorkspace(‘w’)
w.factory(‘x[6.8,0,15]’)
```

## More info here: https://github.com/clelange/roofit/blob/master/rf108_plotbinning.py

```python
dtframe = dt.frame(ROOT.RooFit.Range(-15, 15),
                       ROOT.RooFit.Title("dt distribution with custom binning"))
data.plotOn(dtframe, ROOT.RooFit.Binning(tbins))

c = ROOT.TCanvas("c_plotbinning", "Playing with plotbinning", 800, 400)
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

- [Links to RooFit Tutorials](https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsWG/HCombExercise#Documentation)
- [A short Jupyter Notebook using PyROOT](https://www.nikhef.nl/~vcroft/GettingStartedWithRooFit.html)
- [Hands-on Advanced Tutorials](https://lpc.fnal.gov/programs/schools-workshops/hats.shtml) (HATS)
   - Will require access to Indico.
   