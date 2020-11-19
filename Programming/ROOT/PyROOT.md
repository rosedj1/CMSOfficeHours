# The Power of ROOT within the Comfort of Python

Mention `conda activate my_root_env`.

## Tutorials

- [PyROOT Manual](https://root.cern/manual/python/) from ROOT website.
- [Example PyROOT scripts](https://root.cern.ch/doc/v612/group__tutorial__pyroot.html) from the ROOT website.
- [More example scripts.](https://root.cern/doc/master/group__tutorial__pyroot.html)

## More Resources

- [Pyroot_Zen](https://pyroot-zen.readthedocs.io/en/latest/#): Make ROOT even more Pythonic.

## How to make a TTree and store values using PyROOT

### Example

```python
import ROOT as r
# You must open/create your file before playing with the TTree.
newfile = r.TFile("/work/area/newfile.root", "recreate")
tree = r.TTree("t1", "My New Tree")

# Make a pointer to store values. 
ptr = array('f', [0.])  # Use 'f' for floats, 'd':doubles, 'i':ints. 

# Make a branch in the TTree.
# First and third arguments should exactly match. 
# Third argument needs a type, using a capital letter. 
tree.Branch("m4mu", ptr, "m4mu/F")

# Do your analysis to get value to be stored.
val = 1 + 2  # Example value.
ptr[0] = val

# Finally fill the tree with this value.
tree.Fill()  
```

- Also check out [this nice explanation](https://wiki.physik.uzh.ch/cms/root:pyroot_ttree).
- [More elaborate way](https://root.cern.ch/gitweb/?p=root.git;a=blob;f=tutorials/pyroot/staff.py;h=d955e2ca7481a9a507cb40dbb71c2f85ac12bbbc;hb=HEAD), using C++ structs.

When you close a file (`f.Close()`), then your histograms may be closed with them.
To keep your hist open, do:
```python
hist.SetDirectory(0)  # Must be called before you close the file.
```

Suzanne's method of splitting a TCanvas up into different pads:
```python
# This program prints the mass distribution for samples with varying values of the selection criteria, Delta R.

print("[INFO] Importing libraries...")
from ROOT import TFile, TH1F, TCanvas, gROOT, kTRUE, gPad
import numpy as np
gROOT.SetBatch(kTRUE)

num_bins = 30
lower_bound = 0
upper_bound = 1600 # 300 for mH, 800 for mY, 1600 for mX

print("[INFO] Building canvas...")
c1 = TCanvas("c1", "Mass Distribution") # Canvas object
c1.Divide(1,2) # Divide canvas into 2 pads (1 columns, 2 rows)

c1.cd(1)
gPad.SetLogy() # Set y-axis to log scale
f1 = TFile("test_NMSSM_XYH_bbbb_MC_005.root") # Open ROOT file
t1 = f1.Get("bbbbTree") # Extract ROOT tree
h1 = TH1F("h1","DeltaR = 0.05", num_bins, lower_bound, upper_bound) # Create histogram object
t1.Draw("HH_m >> h1","gen_H1_b1_matchedflag >= 0 && gen_H1_b2_matchedflag >= 0 && gen_H2_b1_matchedflag >= 0 && gen_H2_b2_matchedflag >= 0","goff") # Fill histogram with events that pass the selection criteria
h1.Draw("hist e1") # Draw histogram

c1.cd(2)
gPad.SetLogy()
f2 = TFile("test_NMSSM_XYH_bbbb_MC_010.root")
t2 = f2.Get("bbbbTree")
h2 = TH1F("h2","DeltaR = 0.10", num_bins, lower_bound, upper_bound)
t2.Draw("HH_m >> h2","gen_H1_b1_matchedflag >= 0 && gen_H1_b2_matchedflag >= 0 && gen_H2_b1_matchedflag >= 0 && gen_H2_b2_matchedflag >= 0","goff")
h2.Draw("hist e1")

c1.Draw() # Draw canvas
c1.SaveAs("distribution_mX.pdf") # Save canvas
```

Suzanne's code to plot 2 histograms to the same axes and
plot their ratio on a separate axes below.

```python
from matplotlib import gridspec
def PlotMe(data, kinematic, color, label, bins=None, ax=None):
    """
    This function plots the kinematics in order to all have the same basic format (e.g. left).
    """
    try:
        if bins == None: range, bins = setupPlotting(kinematic)
        else: range, bins_temp = setupPlotting(kinematic)
    except: range, bins_temp = setupPlotting(kinematic)
    if ax == None:
        n, bins, patches = plt.hist(data, range=range, bins=bins, histtype='step', align='mid', color=color, label=label)
    else:
        n, bins, patches = ax.hist(data, range=range, bins=bins, histtype='step', align='mid', color=color, label=label)
    plt.legend(loc='best', prop={'size': 12})
    return n, bins, patches

fig = plt.figure() # Build figure
gs = gridspec.GridSpec(2, 1, height_ratios=[4, 1]) # Allow for axes of various sizes
ax = fig.add_subplot(gs[0]) # Build first axis with aspect ratio gs[0]
n_denom, bins1, patches = PlotMe(reco_data['jet_bTagScore'], kin, color='blue', label=r'baseline', ax=ax)
n_num, bins2, patches = PlotMe(btag, kin, color='orange', label=r'$\Delta R < {}$'.format(deltaR_cut), bins=bins1, ax=ax)
ax.xaxis.set_major_formatter(plt.NullFormatter())
ax.text(1500,10**3,"{:.1f}% Retention".format(float(np.shape(btag)[0])/float(np.shape(reco_data['jet_bTagScore'])[0])*100),weight='bold',fontsize=12)
x = (bins1[1:] + bins2[:-1])/2
eff_hist = np.true_divide(n_num, n_denom, out=np.zeros_like(n_num), where=n_denom!=0)
ax = fig.add_subplot(gs[1])
ax.plot(x, eff_hist)
ax.set_xlabel(r'$p_T$ [GeV]')
ax.set_ylim([0,1.0])
plt.tight_layout()
pdf.savefig()
plt.clf()
```

## Common ROOT Objects

### Text Boxes

You have a few options:

#### TPaveText (my preferred object)

```python
# (xmin, ymin, xmax, ymax, "BRNDC")
# BR = shadow appears in Bottom-Right corner.
pave = ROOT.TPaveText(0.08, 0.5, 0.45, 0.7, "NDC")  # NDC = normalized coord.
pave.SetFillColor(0)
pave.SetFillStyle(1001)  # Solid fill.
pave.SetBorderSize(1) # Use 0 for no border.
pave.SetTextAlign(11) # 11 is against left side, 22 is centered vert and horiz.
pave.SetTextSize(0.06)
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


#### Option 2: TLaTeX

```python
latex = r.TLatex()
latex.SetNDC()
latex.SetTextSize(0.013)
latex.SetTextColor(r.kRed)
bestfit_mean = 0.006718
latex.DrawLatex(0.185, 0.90, f"#mu = {bestfit_mean:%.3E}")
latex.DrawText(0.1, 0.8, "mean  = %.5E" % bestfit_mean_corr)

# You can also associate a name and title to your latex obj:
latex1 = r.TLatex()  # Default coord: (x=0,y=0)
latex1.SetTitle("A new title")
latex1.GetTitle()  # Returns str "A new title".
latex1.SetText(0.4, 0.3, "new words here")  # WARNING: this changes the title!
str(latex)  # Return the name and title associated with this obj.
```

#### Option 3: TPad

```python
pad = r.TPad("pad", "A pad with a hist", 0.03, 0.02, 0.97, 0.57)
legend =  rt.TPad("legend_0","legend_0",x0_l,y0_l,x1_l, y1_l )
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
gr.GetYaxis().SetRangeUser(-0.2, 0.2)
gr.Draw("APC")  # Draw the Axes, Points, and a smooth Curve.

# Drawing Options Description
"A"	Axis are drawn around the graph
"I"	Combine with option 'A' it draws invisible axis
"L"	A simple polyline is drawn
"F"	A fill area is drawn ('CF' draw a smoothed fill area)
"C"	A smooth Curve is drawn
"*"	A Star is plotted at each point
"P"	The current marker is plotted at each point
"B"	A Bar chart is drawn
"1"	When a graph is drawn as a bar chart, this option makes the bars start from the bottom of the pad. By default they start at 0.
"X+"    # The X-axis is drawn on the top side of the plot.
"Y+"    # The Y-axis is drawn on the right side of the plot.
"PFC"   # Palette Fill Color: graph's fill color is taken in the current palette.
"PLC"   # Palette Line Color: graph's line color is taken in the current palette.
"PMC"   # Palette Marker Color: graph's marker color is taken in the current palette.
"RX"    # Reverse the X axis.
"RY"    # Reverse the Y axis.

# Other useful methods.
gr.GetN()        # Return the number of points in the graph.
gr.GetPointX(4)  # Return the x-coordinate of point 4.
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
mg.Add(gr,"lp")
mg.Add(grerr,"cp")
mg.Draw("a")
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

Print **global environment variables** to access things like fonts: `ROOT.gEnv.Print()`

Set a default layout for all your plots by making a **TStyle**:

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

### Items to research

- [PyROOT Hats](https://indico.cern.ch/event/917673/)
