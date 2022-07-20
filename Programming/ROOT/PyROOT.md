# The Power of ROOT within the Comfort of Python

"PyROOT" is simply using ROOT in the Python environment.
For example:

```python
from ROOT import TFile, TCanvas

f = TFile.Open("myfile.root", "read")
h = f.Get("my_hist")

c = TCanvas()
h.Draw()
c.Print()
```

## Install ROOT in Python

I highly recommend Anaconda (`conda`) to install ROOT.
[Here's a nice tutorial.](https://iscinumpy.gitlab.io/post/root-conda/)

## Common ROOT Objects

Nearly all of ROOT's classes start with a 'T'.
Here are the most common:

### TFile

The ROOT version of a file.

```python
f = TFile.Open("myfile.root", "read")
f.ls()  # View contents in myfile.root.
f.Close()
```

### Histograms

Make Your First Histogram

```python
from ROOT import TH1F
h = TH1F("h_name", "Lepton pT", 10, 0, 50)
```

- This makes a histogram (**H**) that is 1-dimensional (**1**) of floating point numbers (**F**).
- The hist has 10 bins, which span the x-axis from `x = 0` to `x = 50`.
- The _internal name_ of the histogram is `h_name` and the _title_ is `The Histogram Title`.

It's probably more efficient to set the binwidth than the num_bins!
NOTE!!!
The stats box that appears on histogram refers to the UNBINNED data!
i.e. you will get the same mean, stdev to appear
regardless of how you bin the data.
There is an "overflow bin" on the right edge of the histogram that collects entries which lie outside the
histogram x range. These entries are NOT counted in the statistics (mean, stdev), BUT they are counted
as new entries!
- There's also an underflow bin
Therefore, entries in overflow bins DO count towards total entries, but not towards statistics, like Integral()

**IMPORTANT:**
If you extract a hist from a TFile, the hist will disappear once the TFile is closed.
Avoid this by doing `h.SetDirectory(0)`:

```python
f = TFile(infile, "read")
h = f.Get("lep_pT")
h.SetDirectory(0)  # Now hist will stay alive after f is closed.
f.Close()
```

#### Make a hist with variable bin width

Make bin edges at: `x = [5, 10, 20, 30, 50, 100]`

```python
import numpy as np
import ROOT as r
h1 = r.TH1F("h1", "Variable Bin Width", 5, np.array([5, 10, 20, 30, 50, 100], dtype=float))
```

Rebinning is easy!

```python
h.Rebin(3)  # Merge three bins at a time (1-3, 4-6, 7-9, etc.). Default=2.
```

- Errors are automatically recalculated

#### Normalize Hist

Check ROOT_Basics.md.

#### Common Histogram Methods

```python
h.GetEntries()            # Return the number of total entries in all bins.
h.GetName()               # Returns the internal name of hist.
h.GetTitle()              # Returns the title of hist.
h.Fill(7)                 # Put one entry into the bin where x = 7 (so not the 7th bin!).
h.Fill(7, 100)            # Put 100 entries into the bin where x = 7.
h.GetMean()               # Get the mean of the UNBINNED data.
h.GetNbinsX()             # Return the number of bins along the x-axis.
                          # (Does not include under/overflow bins.)
h.GetBinContent(3)        # Return the number of entries in (height of) bin 3.
                          # (bin 0 is underflow and bin max+1 is overflow)
                          # This is also called the "weight" of the bin.
h.GetBinCenter(2)         # Get the x-axis value corresponding to the center of bin 2.
h.GetBinLowEdge(k)        # Get the left edge of the bin k. k=0 is overflow, k=1 is first bin.
h.GetBinUpEdge(k)         # Get the right edge of the bin k.
h.GetBinWidth(2)          # Get the bin width of bin 2.
h.FindBin(5.3)            # Get bin number of bin at x = 5.3.
h.FillRandom("gaus", 10)  # Fill the hist with 10 random entries from a gaus distribution.
h.Sumw2()                 # IMPORTANT! Tells the hist to handle errors using sqrt(sum(weights^2)).
h.StatOverflows(True)     # IMPORTANT! Count under/overflow bins in stats. Default is False.
h.Write()                 # Save your hist to the open root file.
```

#### Hist Contents

```python
h.Integral(2, 3)  # Sum the bin contents from bin2 to bin3.
                  # Same as doing h.GetBinContent(2) + h.GetBinContent(3).
# Example:
# bin1 has weight = 3
# bin2 has weight = 2
# bin3 has weight = 6
h.Integral(1, 2) # Returns 5
h.Integral(2, 3) # Returns 8
h.Integral(1, 3) # Returns 11
```

#### Decorate your hist

```python
h.GetXaxis().SetTitleOffset(1.3)
h.SetMarkerStyle(20)  # Put a black data point at the top of each bin.
```

#### Statistics of your Hist

```python
h.GetMean()         # Return: 1/N * sum(entries_bin_k * center_bin_k)
h.GetMeanError()    # Return the error on the mean.
h.GetStdDev()       # Return the root-mean-square (RMS).
h.GetStdDevError()  # Return the error on the RMS.
```

##### Statistics Box

After drawing a histogram, you can **modify the statistics box** (see below).
[Also check this out.](https://root.cern.ch/root/htmldoc/guides/users-guide/Histograms.html#statistics-display).

```python
h.SetStats(0)  # Turn stats box off (1 = on).
# Create the statsbox and access it.
h.Draw()
gPad.Update()              # Not always necessary, but sometimes helpful.
statsbox = h.FindObject("stats")  # "stats" is a reserved name for the stats box.

# Now you can access and modify the statsbox info.
statsbox.GetOptStat()      # Will return something like `1111` (from ksiourmen).
statsbox.SetOptStat(1010)  # Controls what info is displayed in statsbox. FIXME: broken?
# mode = ksiourmen  (default = 000001111)
# k = 1;  kurtosis printed
# k = 2;  kurtosis and kurtosis error printed
# s = 1;  skewness printed
# s = 2;  skewness and skewness error printed
# i = 1;  integral of bins printed
# o = 1;  number of overflows printed
# u = 1;  number of underflows printed
# r = 1;  rms printed
# r = 2;  rms and rms error printed
# m = 1;  mean value printed
# m = 2;  mean and mean error values printed
# e = 1;  number of entries printed
# n = 1;  name of histogram is printed

# Access the coordinates of the edges of the statsbox.
statsbox.GetX1NDC()  # Return the x-val of box left edge, as a fraction of canvas width.
statsbox.SetX2NDC(0.7)  # Set the x-val of box right edge, as a fraction of canvas width.
statsbox.SetY1NDC(0.8)  # Set the y-val of box bottom edge, as a fraction of canvas height.
statsbox.GetY2NDC()  # Return the y-val of box top edge, as a fraction of canvas height.
# Alternatively you can use the x-axis and y-axis values as a reference,
# instead of using a fraction of the canvas:
statsbox.GetX1()  # Return the x-val of box left edge, according to x-axis scale.
statsbox.SetY2()  # Set the x-val of box right edge, according to x-axis scale.

# Default NDC() vals:
statsbox.GetX1NDC() : 0.780
statsbox.GetX2NDC() : 0.980
statsbox.GetY1NDC() : 0.695
statsbox.GetY2NDC() : 0.935
```

Move the stats box:

```python
h.Draw()
statsbox = h.FindObject("stats")
statsbox.SetX1NDC(0.6)
statsbox.SetX2NDC(0.8)
h.Draw()  # Must redraw hist.
c.Update()
```

See what objects your histogram knows about:

```python
h.GetListOfFunctions().Print()
```

#### Draw your Hist

Check ROOT_Basics.md.

#### Make a 2-dim histogram

```python
import ROOT as r
import numpy as np
h2 = r.TH2F("h2", "Fill with text",
              7, np.array([5,7,10,14,20,27,38,50], dtype=float),
              5, np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0]))

# Make random values and fill the hist.
for _ in range(10000):
    x = np.random.random() * 100.
    y = x / 100.
    h2.Fill(x, y)

# Draw the hist to a canvas.
c1 = r.TCanvas()
h2.Draw("colz")  # colz will draw the z-axis as a color bar.
c1.Draw()
```

You can play with the color bar (called a color palette in ROOT):

```python
h2.Draw("colz text e")                # Writes the value stored in each 2D bin on the bin +- weight.
h2.GetZaxis().SetRangeUser(10, 20)  # Restrict color bar to have limits: [10, 20].
r.gStyle.SetPalette(55)               # Change the color map. Default is kBird.
# More color maps: https://root.cern.ch/doc/master/classTColor.html#C06
h2.SetContour(100)                   # Split the color bar into 100 colors (creates a nice gradient).
r.gStyle.SetPaintTextFormat("6.1f words")   # Format of the text to be displayed on all cells.
r.gStyle.SetOptStat(0)                # Don't display hist stats.
c1.Draw()
```

#### Get a slice of a 2-dim hist

Make a **projection** along an axis:

```python
# Slice the TH2 at x-bin 3 and the entire y-axis:
proj_y = h2.ProjectionY("proj_y", 3, 3)

# `proj_y` is a TH1D which can use all the familiar TH1 methods:
proj_y.GetEntries()
proj_y.Draw("same")
```

#### Make a ratio plot

Check ROOT_Basics.md.

#### Pretty up your histogram

Change the number of tick marks on the axis:

```python
h.GetXaxis().SetNdivisions(5, 2, 3, False)
# The 5 indicates 5 primary divisions along x-axis (so 4 visible tick marks).
# The 2 is the number of secondary divisions in each primary division.
# The 3 means the number of tertiary divisions in each secondary division.
# False means do not let ROOT optimize.
# Equivalently:
h.GetXaxis().SetNdivisions(510)  # Divisions along x-axis.
# 510 means 10 primary divisions and 5 secondary divisions. The formula is:
# n = n1 + 100*n2 + 10000*n3
# n1 : num primary div, n2 : num secondary div, n3 : num tertiary div.

```

#### Histogram quirks

Instead of doing `canv.RedrawAxis()` do: `hist.Draw("sameaxis")`

- _What does `h.Draw("samex0")` do?_

#### Other useful histogram methods

```python
h2.FindLastBinAbove(3)  # Return the last bin whose content > 3.
h2.Reset("ICE")         # Empties hist, but only Integral, Contents and Errors.
```

#### Tutorials on ROOT Histograms

- [From the ROOT website](https://root.cern/manual/histograms/)
- [ALL histogram options](https://root.cern.ch/root/htmldoc/guides/users-guide/Histograms.html)

### TTree

The ubiquitous data container for event information.
Powerful and very useful.

#### Extract information within TTree

```python
f = ROOT.TFile("infile_path.root")
tree = f.Get("treename")

for n_evt in range(tree.GetEntries()):
    # Set the internal ROOT pointer at the first event.
    tree.GetEntry(n_evt)
    # Now extract event info.
    # Here I assume that "pT_muon" is a branch in my TTree.
    pT = tree.pT_muon

# There is more pythonic way to iterate over TTree events.
for evt in tree:
    evt.pT_muon

# Which is fastest?
for evt in tree:
    # Do stuff.
for ct in range(tree.GetEntries()):
    tree.GetEntry(ct)
    # Do stuff.
while tree.GetEntry(ct):
    # tree.GetEntry() returns num_bytes (> 0 when the entry exists).
```

#### Create a copy of a TTree

```python
# Clone the structure of an existing TTree `t` with 10 events:
new_tree = t.CloneTree(10)
new_tree = t.CloneTree(-1, "fast") # Clone all events quickly.

# You can turn off a TTree branch so it doesn't get cloned.
tree.SetBranchStatus("eventWeight", 0)
# Or turn off all branches and then turn on (1) the ones you want.
tree.SetBranchStatus("*", 0)
tree.SetBranchStatus("eventWeight", 1)
# Then clone the TTree.
```

#### Make a new TTree and store values inside

```python
import ROOT as r
from array import array

# You must open/create your new TFILE before playing with the new TTree.
newfile = r.TFile("/work/area/newfile.root", "recreate")
new_tree = r.TTree("t1", "My New Tree")

# Make a pointer to store values.
ptr = array('f', [0.])  # Use 'f' for floats, 'd':doubles, 'i':ints.

#=== Store a bool. ===#
# ptr_bool = np.array([0], dtype=np.bool)
# new_tree.Branch("is3P1F", ptr_bool, "is3P1F/O")
# ...but it shows up as an `int`...

# Make a branch in the TTree.
# First and third arguments (branch name) should exactly match.
# Third argument needs a type, using a capital letter.
new_tree.Branch("m4mu", ptr, "m4mu/F")

# Do analysis loop to store the value of each entry in new_tree.
for x in range(5):
    ptr[0] = x**2  # Store value in pointer which points to new_tree.
    new_tree.Fill()  # This saves the "row" info in the TTree.

# You must write the TTree to the file and close the file!
new_tree.Write()
newfile.Close()
```

#### Modify value of existing branch

```python
from array import array

# Create a pointer.
ptr_eventWeight = array('f', [0.])
# Attach pointer to branch.
new_tree.SetBranchAddress("eventWeight", ptr_eventWeight)
# Change value which pointer points to.
ptr_eventWeight[0] = 1.2
new_tree.Fill()
```

- Also check out [this nice explanation](https://wiki.physik.uzh.ch/cms/root:pyroot_ttree).
- [More elaborate way](https://root.cern.ch/gitweb/?p=root.git;a=blob;f=tutorials/pyroot/staff.py;h=d955e2ca7481a9a507cb40dbb71c2f85ac12bbbc;hb=HEAD), using C++ structs.

#### Use TTree to Quickly Draw Histograms

Suppose your TTree is called `tree` and has branches:

- `mass4l`
- `pT1`
- `eta1`

```python
# Make a histogram of the mass4l values:
tree.Draw('mass4l')

# Draw the mass4l hist, but only select events in which pT1 > 20:
tree.Draw("mass4l", "pT1 > 20")
# You can stack cuts and use TMath operators:
tree.Draw("mass4l", "(pT1 > 20) && (abs(eta1) > 0)")

# Turn graphics off (so don't draw) the first 100 entries, starting at entry 50:
tree.Draw("mass4l", "pT1 > 20", "goff", 100, 50)

# Select every 5th entry (row) in the TTree:
tree.Draw("mass4l", "Entry$ % 5")
```

- [The docs](https://root.cern/doc/master/classTTree.html#autotoc_md1037) for `tree.Draw()`.

#### Create New Histgrams with `tree.Draw()`

```python
from ROOT import gDirectory, gPad

# Draw the pT1 branch and save the histogram as "h_new" in the current directory.
tree.Draw("pT1 >> h_new", "y > 0")
# then retrieve it:
h = gDirectory.Get("h_new")

# If you have an open TFile (f), "h_new" is added to that directory:
f.ls()  # View "h_new" and all other objects.
h_again = f.Get("h_new")
```

You can access the newly-created histogram to modify and/or draw it.

```python
htemp = gPad.GetPrimitive("htemp")
htemp.SetMarkerStyle(20)
htemp.Draw("e")

# Can also control htemp's dimensions (100 bins, x_min=10, x_max=60):
t.Draw("mass4l >> htemp(100, 10, 60)", "pT1 > 20")
```

#### Fill Already Existing Histgrams with `tree.Draw()`

Syntax: `tree.Draw(branch >> hist)`

```python
# Make empty hist with 30 bins in the range x = [-15, 15]:
h = TH1F('h_pT', 'Lepton pT', 30, -15, 15)
tree.Draw('pT1 >> h_pT', '', 'goff')

# If you call tree.Draw() again, then the data in h_pT will vanish.
# Put a `+` sign in front of the hist name to append more data:
tree.Draw('pT2 >> +h_pT', '', 'goff')
```

When you close a TFile (`f.Close()`), then your histograms may be closed with them.
To keep your hist (`h`) open, do:

```python
h.SetDirectory(0)  # Must be called before you close the file.
```

Divide your TCanvas up into different pads
and save a multi-page pdf:

```python
outpath_file = "/path/to/outfile.pdf"
c = r.TCanvas()
c.Divide(2,1)  # 2 cols, 1 row
c.Print(outpath_file + "[")
for pT in pT_ls:
    gr, gr_witherrs = make_two_graphs()
    c.cd(1)
    gr.Draw("ALP")
    c.cd(2)
    gr_witherrs.Draw("ALP")
    c.Update()
    c.Print(outpath_file)
c.Print(outpath_file + "]")
```

```python
ROOT.gPad.GetUymin() # Return the axis y-min of current pad.
ROOT.gPad.GetUymax() # Return the axis y-max of current pad.
```

### Text Boxes

You have a few options:

#### TPaveText (my preferred object)

```python
# (xmin, ymin, xmax, ymax, "BRNDC")
# BR = shadow appears in Bottom-Right corner.
pave = r.TPaveText(0.08, 0.5, 0.45, 0.7, "NDC")  # NDC = normalized coord.
pave.SetFillColor(0)
pave.SetFillStyle(1001)  # Solid fill.
pave.SetBorderSize(1) # Use 0 for no border.
pave.SetTextAlign(11) # 11 is against left side, 22 is centered vert and horiz.
pave.SetTextSize(0.025)
pave.AddText(0.1, 0.5, "words go here")  # (x, y, "text")
pave.AddText("E = #sqrt{#vec{p}^{2} + m^{2}}")  # Accommodates LaTeX!
pave.Draw("same")

# Retrieve a specific line:
latex = pave.GetLineWith("go here")  # Returns a TLatex object.
latex.SetTitle("These are new words.")  # Change this line.

# See what's written on your pave.
line_ls = list(pave.GetListOfLines())  # Each line is a TLatex object.
first_line = line_ls[0]
str(first_line)  # Return the first line in your pave as a string.
# It will look like this: 'Name:  Title: Fit 3:'

pave.Print() # See a bunch of info about your pave.
```

#### Option ?: TText

```python
txt = r.TText()
# txt = r.TText(0.85, 0.90, "Hi there")    # Can initialize text object with chars.
# txtnew.SetNDC()
txt.SetTextSize(0.04)
txt.SetTextFont(43)
txt.SetTextColor(r.kBlue)
txt.DrawTextNDC(0.3, 0.4, "Hello world!")  # x,y as a fraction of the canvas width
# txt.DrawText(100, 250, "Hello world!")   # x,y in axis coordinates.
```

#### Option ?: TPaveText

So far I've found this to be the best way to add text to the canvas.

#### Option 2: TLatex

ROOT supports LaTeX symbols.
However instead of using a backslash (`\`), use a hashtag (`#`):
`#p_{T}^{#mu}`

- [List of symbols](https://root.cern.ch/doc/master/classTLatex.html#L5)
- Cursive 'ell': `"m_{4#font[12]{l}} (GeV)"`

```python
tex = r.TLatex()
tex.SetNDC()
tex.SetTextSize(0.013)
tex.SetTextColor(r.kRed)
bestfit_mean = 0.006718
# This one TLatex object can draw many different lines.
tex.DrawLatex(0.185, 0.90, f"#mu = {bestfit_mean:%.3E}")
tex.DrawText(0.1, 0.8, "mean  = %.5E" % bestfit_mean_corr)

# You can also associate a name and title to your tex obj:
tex1 = r.TLatex()  # Default coord: (x=0,y=0)
tex1.SetTitle("A new title")
tex1.GetTitle()  # Returns str "A new title".
tex1.SetText(0.4, 0.3, "new words here")  # WARNING: this changes the title!
str(tex1)  # Return the name and title associated with this obj.
```

#### Option 3: TPad

```python
pad = r.TPad("pad", "A pad with a hist", 0.03, 0.02, 0.97, 0.57)
legend = r.TPad("legend_0","legend_0",x0_l,y0_l,x1_l, y1_l )
#legend.SetFillColor( rt.kGray )
legend.Draw()
legend.cd()

# Should be able to draw text on a RooPlot (frame) with:
# NEEDS TESTING
    # // create the box and set its options

#     pavelabel_x_start = ( float(x_max) + float(x_min) ) * 0.65
#     title = r.TPaveLabel( pavelabel_x_start, 300, x_max, 350, 'Come on dude!' )
#     title.SetTextFont( 50 )
#     title.Draw("same")
```

### TGraph

Make a scatterplot:

```python
n_pts = 5
# I prefer to use numpy arrays to perform computations.
x_vals = np.array([2,4,6,8,10])
y_vals = x_vals**2
# Then convert them to array.arrays afterward.
x_arr = array('f', x_vals)
y_arr = array('f', y_vals)
# Make the graph.
gr = TGraph(n_pts, x_arr, y_arr)
# Pretty it up.
gr.SetLineColor(2)
gr.SetLineWidth(2)
gr.SetMarkerColor(4)
gr.SetMarkerStyle(21)
gr.SetMarkerSize(0.5)
gr.SetTitle('Theoretical Muon Trajectory')
gr.GetXaxis().SetTitle('Transverse Pixel/Strip Positions [cm]')
gr.GetYaxis().SetTitle('Distance from x-axis [cm]')
gr.GetXaxis().SetLimits(-0.05, 0.05)  # SetRangeUser() doesn't work for x-axis! SetLimits() instead.
gr.GetYaxis().SetRangeUser(-0.2, 0.2) # Can also use: gr.SetMaximum(0.2)
gr.Draw("APC")  # Draw the Axes, Points, and a smooth Curve.

#--- TGraph Drawing Options ---#
# "A"     # Axis are drawn around the graph
# "I"     # Combine with option 'A' it draws invisible axis
# "L"     # A simple polyline is drawn
# "F"     # A fill area is drawn ('CF' draw a smoothed fill area)
# "C"     # A smooth Curve is drawn
# "*"     # A Star is plotted at each point
# "P"     # The current marker is plotted at each point
# "B"     # A Bar chart is drawn
# "1"     # When a graph is drawn as a bar chart, this option makes the bars start from the bottom of the pad. By default they start at 0.
# "X+"    # The X-axis is drawn on the top side of the plot.
# "Y+"    # The Y-axis is drawn on the right side of the plot.
# "PFC"   # Palette Fill Color: graph's fill color is taken in the current palette.
# "PLC"   # Palette Line Color: graph's line color is taken in the current palette.
# "PMC"   # Palette Marker Color: graph's marker color is taken in the current palette.
# "RX"    # Reverse the X axis.
# "RY"    # Reverse the Y axis.
```

#### Other Useful TGraph Methods

```python
gr.GetN()        # Return the number of points in the graph.
gr.GetPointX(4)  # Return the x-coordinate of point 4. First point indexed at 0.
gr.GetPointY(4)  # Return the y-coordinate of point 4.
```

### TGraphErrors

A TGraph but with x and y errorbars.

If you want to put many TGraphs on the same plot, then use a **TMultiGraph**:

```python
gr = TGraph(3, array('f', [1,2,3]), array('f', [4,5,6]))
grerr = TGraphErrors(n,x,y,ex,ey)
mg = TMultiGraph()
mg.Add(gr,"lp")  # Draw a line and the points.
mg.Add(grerr,"cp")
mg.SetMinimum(0.0)                # Change y-axis limits.
mg.SetMaximum(9.0)
# Changing the x-axis is a little funky.
# First, draw the multigraph, then change the axis.
mg.Draw("a")
r.gPad.Modified()
mg.GetXaxis().SetLimits(1.5, 7.5)  # Change x-axis limits.

# Retrieve the graphs inside of mg:
gr_ls = mg.GetListOfGraphs()
```

### TMultiGraph

```python
import ROOT as r
from array import array
import numpy as np

from Utils_Python.Plot_Styles_ROOT.tdrstyle_official import setTDRStyle,tdrGrid
tdrStyle = setTDRStyle()
tdrGrid(tdrStyle, gridOn=True)

n_pts = 5
# I prefer to use numpy arrays to perform computations.
x_vals = np.array([2,4,6,8,10])
y_vals = x_vals**2
# Then convert them to array.arrays afterward.
x_arr = array('f', x_vals)
y_arr = array('f', y_vals)
# Make the graph.
gr = r.TGraph(n_pts, x_arr, y_arr)
# Pretty it up.
gr.SetLineColor(2)
gr.SetLineWidth(2)
gr.SetMarkerColor(4)
gr.SetMarkerStyle(21)
gr.SetMarkerSize(0.5)
gr.SetTitle('Theoretical Muon Trajectory')
gr.GetXaxis().SetTitle('Transverse Pixel/Strip Positions [cm]')
gr.GetYaxis().SetTitle('Distance from x-axis [cm]')
gr.GetXaxis().SetLimits(-0.05, 0.05)  # SetRangeUser() doesn't work for x-axis! SetLimits() instead.
gr.GetYaxis().SetRangeUser(-0.2, 0.2)

x_vals1 = np.array([2,4,6,8,10])
y_vals1 = x_vals**3
# Then convert them to array.arrays afterward.
x_arr1 = array('f', x_vals1)
y_arr1 = array('f', y_vals1)
# Make the graph.
gr1 = r.TGraph(n_pts, x_arr1, y_arr1)
# Pretty it up.
gr1.SetLineColor(4)
gr1.SetLineWidth(1)
gr1.SetMarkerColor(4)
gr1.SetMarkerStyle(22)
gr1.SetMarkerSize(0.5)
gr1.SetTitle('Something else')
gr1.GetXaxis().SetTitle('another x axis title')
gr1.GetYaxis().SetTitle('yep')
gr1.GetXaxis().SetLimits(-0.05, 0.05)  # SetRangeUser() doesn't work for x-axis! SetLimits() instead.
gr1.GetYaxis().SetRangeUser(-0.2, 0.2)
print(gr1.GetXaxis().GetTitle())
print(gr1.GetYaxis().GetTitle())
print(gr1.GetTitle())

c = r.TCanvas()
c.Draw()
mg = r.TMultiGraph()
mg.Add(gr, "lp")
mg.Add(gr1, "lp")
titles = f"My favorite; {gr.GetXaxis().GetTitle()}; y axis"
mg.SetTitle(titles)
mg.Draw("a")
c.Update()
c.Draw()
```

### TFit

Fitting functions.

#### Fit a TGraph

```python
from ROOT import TF1, gStyle
fitfunc = TF1("f1", "gaus", 1, 3)
# gr is a TGraph.
result = gr.Fit(fitfunc, "S")
# The result pointer is very useful:
cov = result.GetCovarianceMatrix() # Access the covariance matrix.
chi2 = result.Chi2()    # Return the chi^2 of the fit.
par0 = result.Value(0)  # Retrieve the value for the parameter 0.
err0 = result.ParError(0)      # Retrieve the error for the parameter 0.
result.Print("V")       # Print full info of fit verbosely.
result.Write()          # Store fit info in a file.
# You can also get fit info from the fit function itself:
fitfunc.GetChisquare()
fitfunc.GetParameter(0)
fitfunc.GetParError(0)
```

#### Fit a Histogram

```python
fit_func = TF1("f1", "gaus", 70, 110)
fit_func.SetLineColor(1)
fit_func.SetLineWidth(2)
fit_func.SetLineStyle(2)
# Fit it onto a histogram `h1`:
h1.Fit(fit_func,'S')
# The option 'S' saves the fit results into a pointer.
# Check out more options here:
# https://root.cern.ch/doc/master/TGraph_8cxx_source.html#l01080
gStyle.SetOptFit(111)  # Chi^2, param values, and
fit_func.Draw("same")

# Retrieve the fit values:
par_and_err0 = fit_func.GetParameter(0), fit_func.GetParError(0)
par_and_err1 = fit_func.GetParameter(1), fit_func.GetParError(1)
par_and_err2 = fit_func.GetParameter(2), fit_func.GetParError(2)
```

### TLegend

```python
leg = ROOT.TLegend(xmin, ymin, xmax, ymax)
# (All floats between 0 and 1, as a proportion of the x or y dimension)
leg = ROOT.TLegend(0.60, 0.7, 0.8, 0.9)
leg.AddEntry(h1, "lhaid = %s" % pdf1, "lpf")
leg.SetLineWidth(3)
leg.SetBorderSize(0)
leg.SetTextSize(0.03)
leg.Draw("same")
```

### TStyle

Set a default layout for all your plots by making a **TStyle**:

```python
def make_pretty_plots():
    """Return a TStyle object which sets consistent plots."""
    style = ROOT.TStyle("style","Style for P-TDR")

    style.SetCanvasDefH(620) #600 Height of canvas (and the page).
    style.SetCanvasDefW(600) # Width of canvas (and the page).
    style.SetPadGridX(True)
    style.SetPadGridY(True)
    style.SetHistLineColor(1)
    style.SetNumberContours(100)
    style.SetOptStat("iouRMe")
    style.SetStatX(0.90)  # x-pos of top-right corner of stats box.
    style.SetStatY(0.90)  # y-pos of top-right corner of stats box.
    style.SetStatFormat("6.4g")  # width?.<num_sig_figs>
    style.SetTitleFont(42, "XYZ")  # Change the font title to 42 along x, y, and z axes.
    # Changing the font of the title is very unintuitive.
    style.SetTitleFont(42, "somethingelse")  # Second argument must NOT be "X", "Y", or "Z".
    style.SetTitleFontSize(0.031)
    style.SetTitleSize(0.05, "XYZ")  # Font size of axis titles.
    style.SetLabelSize(0.03, "XYZ")  # Font size of numbers on axes.
    style.SetOptFit(1)

    style.cd()
    return style
```

TSyle can also change **histogram** features:

```python
style.SetHistFillColor(1)     # Color_t color=1.
style.SetHistFillStyle(0)     # Style_t styl=0.
style.SetHistLineColor(3)     # Color_t color=3.
style.SetHistLineStyle(0)     # Style_t styl=0.
style.SetHistLineWidth(1.5)   # Width_t width=1.
style.SetHistMinimumZero(1)   # Bool_t zero=kTRUE sets y-axis to 0.
style.SetHistTopMargin(0.05)  # Double_t hmax=0.05.
```

Learn how to modify a statistics box: [https://root.cern.ch/doc/master/classTPaveStats.html](https://root.cern.ch/doc/master/classTPaveStats.html)

- Using a minus sign in a superscript: replace `^-` with `^{#font[122]{\55}}`

## Load C++ script into Python

Suppose you have a script called `simple.C`:

```c++
// A simple function to load into Python.
int easy_func(int x) {
    int y;
    y = x + 4;
    return y;
}
```

There are at least **two ways** to make this function available to Python:

**Option 1:**

Compile the code (`root -l` then `.L simple.C+`) and use the `.so` file:

```python
import ROOT
ROOT.gSystem.Load("./simple_C.so")
ROOT.easy_func(5)  # Returns 9.
```

**Option 2:**

Put the C++ code into a Python string and load it into ROOT:

```python
import ROOT

cpp_code = """
int easy_func(int x) {
    int y;
    y = x + 4;
    return y;
}
"""

ROOT.gInterpreter.ProcessLine(cpp_code)  # or try: gInterpreter.Declare(cpp_code)
ROOT.easy_func(5)  # Returns 9.
```

You may have to combine a couple of these commands:

```python
ROOT.gSystem.Load("./RooMyPDF_DSCB_C.so")
ROOT.gInterpreter.Declare(cpp_code)
ROOT.DSCB_scanner()
```

### Other ways to link C++ and Python in ROOT

Create C++ types:

```python
# Make a vector of strings:
branchList = ROOT.vector('string')()
```

Other possible ways?

```python
cpp_fn = """
ROOT.gInterpreter.Declare()
```

## Uproot

```python
# From Suzanne.
import uproot
import awkward

f = uproot.open(filename)
tree = f['path/to/tree_name']
branches = tree.arrays(namedecode='utf-8')
table = awkward.Table(branches)
nevents = len(table['tree_branch'])

mask = table['tree_branch'] > some_cut
table['tree_branch'][mask]
table['another_tree_branch'][mask]
```

## More ROOT Quirks

Run your `.rootlogon.C` file using Python: `ROOT.gROOT.LoadMacro('.rootlogon.C')`

Print **global environment variables** to access things like fonts:

- `ROOT.gEnv.Print()`
- `gPad.SetLogy()`

## Tutorials

- [PyROOT Manual](https://root.cern/manual/python/) from ROOT website.
- [Example PyROOT scripts](https://root.cern.ch/doc/v612/group__tutorial__pyroot.html) from the ROOT website.
- [More example scripts.](https://root.cern/doc/master/group__tutorial__pyroot.html)

## More Resources

- [Scikit-HEP](https://scikit-hep.org/):
  - Amazing packages to help with your particle physics analysis.
- [Pyroot_Zen](https://pyroot-zen.readthedocs.io/en/latest/#): Make ROOT even more Pythonic.

## Items to research

- [PyROOT Hats](https://indico.cern.ch/event/917673/)
