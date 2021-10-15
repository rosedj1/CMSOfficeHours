# The Power of ROOT within the Comfort of Python

Mention `conda activate my_root_env`.

## Tutorials

- [PyROOT Manual](https://root.cern/manual/python/) from ROOT website.
- [Example PyROOT scripts](https://root.cern.ch/doc/v612/group__tutorial__pyroot.html) from the ROOT website.
- [More example scripts.](https://root.cern/doc/master/group__tutorial__pyroot.html)

## More Resources

- [Scikit-HEP](https://scikit-hep.org/):
  - Amazing packages to help with your particle physics analysis.
- [Pyroot_Zen](https://pyroot-zen.readthedocs.io/en/latest/#): Make ROOT even more Pythonic.

## TFile

The ROOT version of a file.

```python
```

## TTree

The ubiquitous data container for event information.

### Loop over events in TTree

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
```

### Make a new TTree and store values inside

```python
import ROOT as r
from array import array

# You must open/create your file before playing with the TTree.
newfile = r.TFile("/work/area/newfile.root", "recreate")
newtree = r.TTree("t1", "My New Tree")

# Make a pointer to store values. 
ptr = array('f', [0.])  # Use 'f' for floats, 'd':doubles, 'i':ints.
# Store a bool:
# ptr_bool = np.array([0], dtype=np.bool)
# newtree.Branch("is3P1F", ptr_bool, "is3P1F/O")
# ...but it shows up as an `int`...

# Make a branch in the TTree.
# First and third arguments should exactly match. 
# Third argument needs a type, using a capital letter. 
newtree.Branch("m4mu", ptr, "m4mu/F")

# Do analysis loop to store the value of each entry in newtree.
for x in range(5):
    ptr[0] = x**2  # Store value in pointer which points to newtree.
    newtree.Fill()  # This saves the "row" info in the TTree.

# You must write the TTree to the file and close the file!
newtree.Write()
newfile.Close()
```

### Create a copy of a TTree

```python
# Clone the structure of an existing TTree `t` with 0 events:
newtree = t.CloneTree(0)
# Use `-1` to clone all events.
```

- Also check out [this nice explanation](https://wiki.physik.uzh.ch/cms/root:pyroot_ttree).
- [More elaborate way](https://root.cern.ch/gitweb/?p=root.git;a=blob;f=tutorials/pyroot/staff.py;h=d955e2ca7481a9a507cb40dbb71c2f85ac12bbbc;hb=HEAD), using C++ structs.

When you close a file (`f.Close()`), then your histograms may be closed with them.
To keep your hist open, do:

```python
hist.SetDirectory(0)  # Must be called before you close the file.
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

## Common ROOT Objects

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

# Drawing Options Description
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

fitfunc = r.TF1("f1", "gaus", 1, 3)
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

# Other useful methods.
gr.GetN()        # Return the number of points in the graph.
gr.GetPointX(4)  # Return the x-coordinate of point 4. First point indexed at 0.
gr.GetPointY(4)  # Return the y-coordinate of point 4.
```

### TGraphErrors

A TGraph but with x and y errorbars.

```python
```

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

### Legends

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

### Fit Functions

```python
from ROOT import TF1, gStyle
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

## More ROOT Quirks

Run your `.rootlogon.C` file using Python: `ROOT.gROOT.LoadMacro('.rootlogon.C')`

Print **global environment variables** to access things like fonts:

- `ROOT.gEnv.Print()`
- `gPad.SetLogy()`

Set a default layout for all your plots by making a **TStyle**:

Learn how to modify a statistics box: [https://root.cern.ch/doc/master/classTPaveStats.html](https://root.cern.ch/doc/master/classTPaveStats.html)

```python
def make_pretty_plots():
    """Return a TStyle object which sets consistent plots."""
    tdrStyle = ROOT.TStyle("tdrStyle","Style for P-TDR")

    tdrStyle.SetCanvasDefH(620) #600 Height of canvas (and the page).
    tdrStyle.SetCanvasDefW(600) # Width of canvas (and the page).
    tdrStyle.SetPadGridX(True)
    tdrStyle.SetPadGridY(True)
    tdrStyle.SetHistLineColor(1)
    tdrStyle.SetNumberContours(100)
    tdrStyle.SetOptStat("iouRMe")
    tdrStyle.SetStatX(0.90)  # x-pos of top-right corner of stats box.
    tdrStyle.SetStatY(0.90)  # y-pos of top-right corner of stats box.
    tdrStyle.SetStatFormat("6.4g")  # width?.<num_sig_figs>
    tdrStyle.SetTitleFont(42, "XYZ")  # Change the font title to 42 along x, y, and z axes.
    # Changing the font of the title is very unintuitive.
    tdrStyle.SetTitleFont(42, "somethingelse")  # Second argument must NOT be "X", "Y", or "Z".
    tdrStyle.SetTitleFontSize(0.031)
    tdrStyle.SetOptFit(1)

    tdrStyle.cd()
    return tdrStyle
```

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

## Items to research

- [PyROOT Hats](https://indico.cern.ch/event/917673/)
