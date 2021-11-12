# Histograms

[An excellent summary.](https://root.cern.ch/root/htmldoc/guides/users-guide/Histograms.html#statistics-display).

## Make Your First Histogram

```python
from ROOT import TH1F
h = TH1F("h_name", "The Histogram Title", 10, 0, 50)
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

### Make a hist with variable bin width

Make bin edges at: `x = [5, 10, 20, 30, 50, 100]`

```python
import numpy as np
import ROOT as r
h1 = r.TH1F("h1", "Variable Bin Width", 5, np.array([5, 10, 20, 30, 50, 100], dtype=float))
```

---

Rebinning should be rather easy!
- there is a Rebin method
- Errors are automatically recalculated

```python
h.Rebin(3)  # Merge three bins at a time (1-3, 4-6, 7-9, etc.). Default=2.
```

Normalizing Histos:

```c++
h->Scale(1/h->Integral())
```

## Common Histogram Methods

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

### Hist Contents

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

### Statistics of your Hist

```python
h.GetMean()         # Return: 1/N * sum(entries_bin_k * center_bin_k)
h.GetMeanError()    # Return the error on the mean.
h.GetStdDev()       # Return the root-mean-square (RMS).
h.GetStdDevError()  # Return the error on the RMS.
```

### Decorate your hist

```python
h.GetXaxis().SetTitleOffset(1.3)
h.SetMarkerStyle(20)  # Put a black data point at the top of each bin.
```

#### Statistics Box

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

Example showing how to move the stats box:

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

### Draw your Hist

```python
h_Jpsi_m2mu.SetTitle("MC 2017 J/#psi mass resonance, fit range = #mu#pm%.1f#sigma"%num_sigmas)
h_Jpsi_m2mu.SetXTitle(m_mumu_str)
h_Jpsi_m2mu.SetYTitle("Events / [%.4f GeV]" % h_Jpsi_m2mu.GetBinWidth(0) )
#h.SetLogy()  # Set y axis to be log scale? CANVAS SETS LOGSCALE: c.SetLogy(True)

canv = TCanvas(filename, filename, 600, 600)
canv.Print(fullpath_pdf + "[")  # Opens DPF.
canv.cd()
canv.Print(fullpath_pdf + "]")  # Closes PDF.

```

```c++
// Load histo from root file:
TFile f("histos.root");
TH1F *h = (TH1F*)f.Get("hgaus");

// Make histogram pointer.
TH1F* h = new TH1F("h","My Histogram",100,-20,20)
TH1F h("hgaus", "histo from a gaussian", 100, -3, 3);

h->FillRandom("gaus", 5000)		# Fill h1 with 5000 random points pulled from Gaussian Distribution
h->Fill(gRandom->Gaus(4,2))	# Fill h1 with a single point pulled from Gaussian with mu=4, sigma=2
								(do a for loop to fill it with many points)
	for (int i=0; i<1000; i++) {h->Fill(gRandom->Gaus(40,15));}
h->GetMaximum()				# Returns the number of entries inside the bin which holds the most entries
h->GetMinimum()				# Returns the number of entries inside the bin which holds the fewest entries
h->GetMaximumBin()			# Tells you which bin holds the most entries; Returns the bin number(not x value of bin!)

	mumuMass->GetXaxis()->GetBinCenter(mumuMass->GetMaximumBin())		# returns most-probable value of histo

h->GetMaximumStored()				# ???
h->GetXaxis()->GetBinCenter(<int bin>)	# returns the x value where the center of bin is located
h->GetXaxis()->SetRangeUser(-5, 5)  // Changes the x-axis range to [-5, 5].
h->SetBinContent(<int bin>, <double val>)	# Deletes whatever is in bin number bin, and fills it with value val
											(this counts as adding a NEW entry!)
h->SetAxisRange(double <xmin>, double <xmax>, "<X or Y>") 	# 
h->Integral(3, 9)  // Integrate bin contents from bin 3 to 9.
h->IntegralAndError(<bin1>,<bin2>,<err>)					# calculates the integral 
    - err will store the error that gets calculated
    - so before you execute the IntegralAndError, first do err = Double(2) to create the err variable 

// TH2F
h2->Integral()  // calculate integral over ALL bins
h2->IntegralAndError(xbin1, xbin2, ybin1, ybin2, err) // calculates the integral over square region, specified by bins
- err will store the error that gets calculated
- so before you execute the IntegralAndError, first do err = Double(2) to create the err variable 
h2->Draw("COLZ1") // "COL" means color, "Z" means draw the color bar, "1" makes all cells<=0 white!

h->Draw()
h->Draw("hist")    // Make sure to draw a histogram
h->Draw("hist e")  // Draw histogram with error bars ( where err = sqrt(num_entries_in_bin) )
h->Draw("hist e1") // Error bars ( where err = sqrt(num_entries_in_bin) )

// Bin convention:
// bin = 0; underflow bin
// bin = 1; first bin with low-edge xlow INCLUDED
// bin = nbins; last bin with upper-edge xup EXCLUDED
// bin = nbins+1; overflow bin
```

Boot up the ROOT interpreter:

```bash
root -l
```

```c++
// Common variables types:
int num;
TString finalstate;
float_t mass2l;
Long64_t nentries = tree->GetEntries();


// How to use these variables:
int some_num = 5;
TString some_str = "Text goes here";
some_str.Data();  // Returns "Text goes here".

// Print to the screen.
std::cout << "Hi there. This is text from this script." << std::endl;

// Vectors (arrays).
std::vector<int> vec;
vec.push_back(4);  // Add an element with value 4 to this vector.
vec[0];            // Return the value of the 0th element (4).
vec.at(0)          // Another way to access the 0th element.
vec.clear()        // Empty the vector.
vec.size()         // Return the number of elements in vec.

std::vector<TString> years;  // Make a vector of TStrings.
years.push_back("2020");
years.push_back("2021");
years[1].Data()              // Access the 1st element. Returns "2021".

TString formatted_txt;
formatted_txt = Form("This is the year: %s", years.at(1))


// for loops
for(int y = 0; y < years.size(); y++) {
    // Do stuff here;
}
```

You can avoid all the `std::` calls by doing:
```c++
using namespace std;

cout << years.size() << endl;
```

```c++
TFile f("histos.root", "new");

TFile* infile = TFile::Open("somerootfile.root", "read");  // Open a root file.
TTree* tree;  // Make a TTree pointer.
if(!infile){  // Make sure you can access the TFile.
    cout << "ERROR could not find the file" << endl;
    continue;
}
else{
    cout << "File opened." << endl;
    infile->cd("Ana");  // Go into the TDirectoryFile.
    tree = (TTree*)gDirectory->Get("passedEvents");
    // Event *event   = new Event();
    tree->SetBranchStatus("*",0);
    tree->SetBranchStatus("Run",1);
```

## Make a 2-dim histogram

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

### Get a slice of a 2-dim hist

Make a **projection** along an axis:

```python
# Slice the TH2 at x-bin 3 and the entire y-axis:
proj_y = h2.ProjectionY("proj_y", 3, 3)

# `proj_y` is a TH1D which can use all the familiar TH1 methods:
proj_y.GetEntries()
proj_y.Draw("same")
```

## Make a ratio plot

```cpp
void ratioplot1() {
   gStyle->SetOptStat(0);
   auto c1 = new TCanvas("c1", "A ratio example");
   auto h1 = new TH1D("h1", "h1", 50, 0, 10);
   auto h2 = new TH1D("h2", "h2", 50, 0, 10);
   auto f1 = new TF1("f1", "exp(- x/[0] )");
   f1->SetParameter(0, 3);
   h1->FillRandom("f1", 1900);
   h2->FillRandom("f1", 2000);
   h1->Sumw2();
   h2->Scale(1.9 / 2.);
   h1->GetXaxis()->SetTitle("x");
   h1->GetYaxis()->SetTitle("y");
   auto rp = new TRatioPlot(h1, h2);
   c1->SetTicks(0, 1);
   rp->Draw();
   c1->Update();
```

## Histogram quirks

Instead of doing `canv.RedrawAxis()` do: `hist.Draw("sameaxis")`

- _What does `h.Draw("samex0")` do?_

## Other useful histogram methods

```python
h2.FindLastBinAbove(3)  # Return the last bin whose content > 3.
h2.Reset("ICE")         # Empties hist, but only Integral, Contents and Errors.
```

## Tutorials on ROOT Histograms

- [From the ROOT website](https://root.cern/manual/histograms/)
- [ALL histogram options](https://root.cern.ch/root/htmldoc/guides/users-guide/Histograms.html)
