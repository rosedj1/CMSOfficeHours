# More info here: https://github.com/clelange/roofit/blob/master/rf108_plotbinning.py

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