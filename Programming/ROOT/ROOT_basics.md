# The ROOT of High-Energy Physics Data Analysis

*FIXME: Needs to be heavily revised!*

## Other ROOT tutorials

- Here is a [comprehensive and XKCD-comic-filled tutorial](ROOT_Tutorial_with_XKCD_Pitstops.pdf) on how to use ROOT.
- Enjoyable [slides](http://hadron.physics.fsu.edu/~skpark/document/ROOT/RootLecture/)
from 2009.
- A [2-day ROOT course on GitHub](https://github.com/root-project/training/tree/master/BasicCourse).
If you want the boiled down version, keep reading the notes below.
- [Some dude's surprisingly useful notes to himself.](https://twiki.cern.ch/twiki/bin/view/Main/RootNotes)

## How to Start ROOT

**ROOT** is easily installed with **CMSSW**.

1. Enter a CMSSW environment: `cd /path/to/CMSSW_10_2_18/src/`
   1. Don't have a CMSSW environment? Do:

   ```bash
   source /cvmfs/cms.cern.ch/cmsset_default.sh
   cmsrel CMSSW_10_2_18
   ```

2. Then do `cmsenv` to make CMSSW commands available to you.
3. Finally, open up ROOT: `root -l` (the letter "ell")
   1. The `-l` flag keeps the splash window from popping up.

## Basic ROOT Commands

```c++
.q                 // Quit out of ROOT. If ROOT ever freezes, you can always Ctrl-C.
.?                 // View a list of commands.
.help              // Open a help menu.
.!<shell_command>  // Pass a command from ROOT to your terminal: .!pwd
.x my_root_file.C  // Execute a macro.
.L my_root_file.C  // Load a macro to make its functions available to ROOT.
.L my_root_file.C+ // Compile a macro to make machine code.
```

### Use ROOT like a calculator

```c++
2 + 3              // Prints 5
TMath::Power(2,3)  // Prints 8.0000000
sqrt(4)            // Prints 2.0000000
```

### Plot a Function

```c++
TF1 f1("func1", "cos(x)*exp(-x)", 0, 5)  // A TF1 object is a 1-D function.
f1.Draw()                                // Draw the function to a TCanvas.
```

After the `Draw()` call, a **TCanvas** should pop up on your screen with a red line drawn: ![FIXME: add the graph](yo).

**IMPORTANT**: Use your cursor to _right-click_ on different parts of the TCanvas: the red line, the axis numbers, the title, the white space.
You can change many aspects of the plots like this.
**This is also a great way to see which objects correspond to which "TClass".**

You can update the plot _in real time_ in two ways:

1. Directly from the command line. Try: `f1.SetTitle("Shiny New Title")`
2. Right-clicking on the TCanvas.

See if you can make the following changes directly through the TCanvas:
- change the Title to `"My First Function"`.

ROOT has tab-completion so if you don't exactly remember the command
you can type: `f1.SetTi` and then hit the Tab key to fill in the rest.

### Creating Pointers

```c++
TFile* file = new TFile("test_file.root", "read");
TH1D* hist = new TH1D("example","example",100,-3,3);

TDatime now;
TDatime *p;    // Declare a pointer to a TDatime object, name it p.
p = &now;      // Set the pointer p to the address of object now.
p->Print();    // Call the Print() method of the object p is pointing to.
(*p).Print();  // *p is the object p is pointing to. The `*` is the dereference operator.
```

**Notice:** Pointers use the `->` operator, while objects use the `.` operator. 

## Example Scripts

### A Simple C++ Function

Put this code into a file called **mult.C**.
```c++
Double_t mult(Double_t a, Double_t b = 2) {
// multiply a and b
   return a * b;
}
```

Now open the ROOT interpreter (`root -l`), load the file (`.L mult.C`),
and call the `mult()` function by typing: `mult(4,10)`.

- The parameter `b = 2` means that `b` will have a default value of `2`, if you don't specify any value for `b`.

### Open a ROOT file and access TTree info

The script below shows how to open a root file,
open the TTree inside, and extract a value (`m4mu`) stored inside.

```c++
void open_file_print_val() {
    // Open the root file.
    TFile* infile = TFile::Open("/path/to/root_file.root");
    // Access the TTree.
    TTree* tree = (TTree*)gDirectory->Get("tree_name");
    // Tell ROOT to read from the TTree branch called "m4mu".
    tree->SetBranchStatus("m4mu",1);
    // Use a variable to hold the values from the TTree.
    Float_t m4mu;
    tree->SetBranchAddress("m4mu", &m4mu);
    // Extract a value from the 5th event.
    tree->GetEntry(5);
    cout << "For event 5, m4mu = " << m4mu << endl;
    return 0;
}
```

Save the script above in a file called **open_file_print_val.C**.
Then do `root -l open_file_print_val.C` to run it.

## Most Common ROOT Objects

### TTree

The essential data storage container in ROOT.

Imagine a TTree to be like a spreadsheet.
Each row is an event (usually) and each column is a variable
(think: pT, energy, mass, x_position, etc.).

- Columns are called **branches**.
- TTrees are actually much more powerful than a spreadsheet because each
branch can hold a different type of data (int, vector, hist, TTree, etc.).

[Make a subset of a TTree.](https://root.cern.ch/doc/master/copytree3_8C.html)

#### Skim certain branches of a TTree

```cpp
void skim_certain_branches() {
    TFile *tf = new TFile("infile.root", "READ");
    TTree *tree = (TTree*)tf->Get("Events");

    // Turn off all branches, then manually turn on the ones to keep.
    tree->SetBranchStatus("*", 0);
    tree->SetBranchStatus("LepPt", 1);
    tree->SetBranchStatus("nBX", 1);

    TFile *tf_out = new TFile("outfile.root", "RECREATE");
    TTree *newtree = tree->CloneTree(10);  // Clone 10 events. Use -1 for all.

    newtree->Write();
    return;
}
```

### TChain

Chains multiple TTrees together (perhaps they even live in different files).

### TCanvas

This is the "canvas" onto which your plots will be drawn. Make a TCanvas pointer:

```c++
TCanvas* c1 = new TCanvas("c1_name", "The Title", 800, 600);  // int pixel_width_x, int pixel_width_y
c_obj = TCanvas("name", "The Title");  // This is not a pointer, but a TCanvas object.
```

#### Change the look of your TCanvas

```c++
c1->SetTickx(1);    // Add x-ticks to the right side of the canvas.
c1->SetTicky(0);    // Remove y-ticks from the top of the canvas.
c1->SetTicks(1,0);  // x-ticks on, y-ticks off.

// Other TCanvas methods.
c1->SetBatch();     // Don't let plots pop up to the screen. Makes your code run faster.
c1->SetFillColor(42);  // Paint the area outside the axes of the plot. 

// Move the edges of the canvas (say to make room for a ratio plot):
c1->SetBottomMargin(0.2);
c1->SetTopMargin(0.0);
c1->SetLeftMargin(0.1);
c1->SetRightMargin(0.1);
```

After you draw a histogram to your canvas, you can save the figure:
c->SaveAs("path/to/myplot.pdf")

**Save many plots into one pdf!**
```c++
c1 = ROOT.TCanvas()
c1.Print(outpath_pdf + "[")
h_m4mu.Draw("hist")
c1.Print(outpath_pdf)
h_m4mu_corr.Draw("hist")
c1.Print(outpath_pdf)
h_m4mu_diff.Draw("hist")
c1.Print(outpath_pdf)
c1.Print(outpath_pdf + "]")

c1->Print("MyPdf.pdf[")    // Note the opening '['.
c1->Print("MyPdf.pdf")
...
c1->Print("MyPdf.pdf]")    // Close the PDF, with the ']'.
```

Put multiple plots on the same TCanvas:

```c++
TCanvas* c1 = new TCanvas("c1", "Main plot and ratio plot", 800, 800);
TPad* ptop = new TPad("ptop", "Main plot", 0.0, 0.3, 1.0, 1.0);  // (name,title,xmin,ymin,xmax,ymax)
TPad* pbot = new TPad("pbot", "Ratio plot", 0.0, 0.0, 1.0, 0.3);
ptop->Draw();
pbot->Draw();

TH1F* h1 = new TH1F("h1", "Main hist", 200, -10, 10);
TH1F* h2 = new TH1F("h2", "Bottom hist", 100, 0, 5);
h1->FillRandom("gaus", 10000);
h2->FillRandom("expo", 5000);

ptop->cd();
h1->Draw();  // h1 will be drawn to top pad.
pbot->cd();
h2->Draw();  // h2 will be drawn to bottom pad.


// Alternatively you can divide the original canvas up into equal regions.
TCanvas *c1 = new TCanvas("c1","multipads",900,700);
gStyle->SetOptStat(0);
c1->Divide(1,2,0,0);  // Make 1 col and 2 rows of plots, with 0 x-spacing and 0 y-spacing.
TH21 *h1 = new TH21("h1","test1",10,0,1);
TH21 *h2 = new TH21("h2","test2",10,0,1);

c1->cd(1);
gPad->SetTickx(2);
h1->Draw();

c1->cd(2);
gPad->SetTickx(2);
gPad->SetTicky(2);
h2->GetYaxis()->SetLabelOffset(0.01);
h2->Draw();
```

### Graphs

TGraph

gr1.GetXaxis().SetRangeUser(-3.5, -2)  

Multigraph:

```c++
mg = TMultiGraph("<internal_name>", "<title>")

mg.SetMaximum(<maxval>)		# set y-axis to <maxval>

You can fit functions to the histogram:
mumuMass->Fit("gaus")
- or use a histogram
g1 = new TF1("m1","gaus",85,95);
mumuMass->Fit(g1,"R");
- here mumuMass is the name of the histogram
- Easy way to fit a histo:
h1.Fit("gaus", "S", "", x_min, x_max) 
- the "S" argument lets you Save the parameters in a variable for later access
```

To learn more about fitting functions, go to LPC machines at Fermilab:
/uscms/home/drosenzw/nobackup/YOURWORKINGAREA/CMSSW_9_3_2/src/
And follow these directions:
https://twiki.cern.ch/twiki/bin/viewauth/CMS/SWGuideCMSDataAnalysisSchoolPreExerciseFourthSet

### Changing text

```cpp
// How to change axis labels (not axis titles):
tg->GetXaxis()->SetBinLabel

// OR

TH1F* h = (TH1F*) tg->GetHistogram()->Clone();
for (Int_t i = 0; i < tg->GetN(); i++)
    h->GetXaxis()->SetBinLabel(i + 1, x_labels[i].c_str());

h->Draw("AXIS");
tg->Draw("LP");
```

## Other ROOT Info

### Some types in ROOT

Most ROOT types begin with `T`.
So instead of type `string`, ROOT uses `TString`:

```cpp
TString infile = "path/to/file.root";
```

- *NOTE: You MUST use double quotes (`"`) and not single quotes (`'`)!*

| ROOT Types | Usual C++ Type | Description |
|---|---|---|
| `Int_t` | `int` | Integers, like 4, 100, 0|
| `Double_t` | `double` | Double precision floats, like 1.2345678909284|
| `Long64_t` | `long`FIXME |
ULong64_t

The most important ROOT objects:
| ROOT Class | Kind of Object | Short Description |
|---|---|---|
| `TH1` | Histogram |  |
| `TF1` | 1-dim Function | |
| `TLorentzVector` | 4-vector | |

#### How to determine the type of a branch in a TTree

This is a sloppy way to do it but it works:

```cpp
// Make a variable to attach to the branch.
Int_t var;
tree->SetBranchAddress("mass4mu", &var);
// At this point, ROOT will either complain that branch "mass4mu: is not of
// type Int_t and it will tell you the real type or if there's no problem then
// you know the branch is of type Int_t!
```

### Format text

How to use a `TString`:

```c++
TString greeting = "hello there";
TString new_greeting = greeting + "yo whaddup!";
cout << new_greeting << endl;  // hello thereyo whaddup!
```

Convert a number to a TString.

```cpp
ULong64_t Run;
oldtree->SetBranchAddress("Run", &Run);
oldtree->GetEntry(0);
TString s_Run = std::to_string(Run);
```

How to **combine** a `TString` with other types:

```c++
Int_t k = 3;
Double_t pT[5] = {5, 10, 20};
TString parabolic_name = TString::Format("parabolic_graphs_pT%f_%d", pT[1], k)
// parabolic name looks like: "parabolic_graphs_pT10.000000_3"
// To get rid of the trailing zeroes, do: TString::Format("parabolic_graphs_pT%.0f_%d",...)
```

Can also use the `Form()` function to combine `string`s into `TString`s:

```c++
TString nome_canvas = Form("Integral = %.0f", 136.5);
nome_canvas += Form("%d", h+1);
histo_name = lepton_type.at(j) + Form("Pt_Lep%d", i);
histo_name = Form("UnbinnedPt_%s_%.0f_%.0f_%s_%s", lepton_type[j].Data(), pT_bins.at(y-1), pT_bins.at(y), eta_bins_name[x-1].Data(), eta_bins_name[x].Data());
nome = Form("eta_%d_phi_%d", x, y);

// Can also put TStrings inside of Form():
nome = Form("eta_%s", nome_canvas.Data());
```

How to pass a `string` into `tree->GetEntries(cuts)`:

```c++
Double_t m4mu_min = 105.0;
Double_t m4mu_max = 140.0;
string cuts = Form("m4mu > %.1f && m4mu < %.1f", m4mu_min, m4mu_max)
tree->GetEntries(cuts.c_str())
```

### Global Pointers

They begin with a "g".

```c++
gROOT->SetBatch();      // Plots will NOT be drawn to the screen (speeds up code).
gStyle->SetOptStat(0);
```

rootlogon.C - Code that is executed at startup. 
rootalias.C - Put frequently used functions in here.

In the ROOT interpreter, you can do: `.L your_script.C` to **L**oad your script's function. Then just do: `your_script(whatever,params)` to run it.

See where your ROOT install files live: `echo $ROOTSYS`

Cryptic ROOT commands to look into:

```c++
gInterpreter->GenerateDictionary("vector<vector<float> >", "vector");
```

If you have Python and ROOT installed, you may be able to open a 
Jupyter Notebook running ROOT C++ by typing this in your terminal: `root --notebook`

## General Tips while Using ROOT

Objects should be drawn (`obj->Draw()`) only **once**.
- Use `c->Modified()` to update an already drawn object.

Use the ROOT interpreter to **test pieces of your code**, before you put it into a script.

Make a nice multiplication/times symbol using ROOT: `thing1 #upoint thing2`

- Comes out as a small dot.

## More Resources

- [ROOT Presentation (shorter)](http://physics.bu.edu/NEPPSR/2007/TALKS-2007/ROOT_Tutorial_Bose.pdf)
- [ROOT Presentation (longer)](http://nuclear.ucdavis.edu/~calderon/Presentations/ROOT-TipsTricks.pdf)
- [Nevis Columbia links](https://www.nevis.columbia.edu/~seligman/root-class/links.html)
- [ROOT for Beginners](https://en.wikitolearn.org/ROOT_for_beginners)

## Scrap ROOT code: to organize

```c++
string outputFileName = opts["output"].as<string>();
tree = (TTree*)_infile->Get("tree");
auto t = f->Get<TTree>("tree");
```

---

## Header files

Keep your code organized by **defining functions, etc.** in header files.
Let's define a function called `linspace()` in a file called `linspace.h`:

```cpp
#ifndef LINSPACE_H
#define LINSPACE_H

#include <vector>

vector<double> linspace(double start, double stop, int num);

#endif
```

Then fill out the guts of this function in an *implementation file*:

```cpp
#include "linspace.h"  // Must include the header file!
#include <vector>

vector<double> linspace(double start, double stop, int num) {
    int steps = num - 1;
    vector<double> pts;
    // Width of each segment.
    double width = (stop - start) / steps;
    pts.push_back(start);
    // Create the intermediate points, between start and stop.
    for (int k = 1; k < steps; k++) {
        pts.push_back(start + k*width);
    }
    // Finally add the end point.
    pts.push_back(stop);
    return pts;
}
```

Now anyone can use these header and implementation files in their code.
As an example, let's make a file called `testyboi.C`:

```cpp
#include "linspace.h"  // Again, include the header file.
#include <iostream>
#include <vector>

using namespace std;

void testyboi(double start, double stop, int num) {
    vector<double> myrange;
    myrange = linspace(start, stop, num);
    for (int k = 0; k < myrange.size(); k++) {
        cout << "myrange[" << k << "] is: " << myrange[k] << endl;
    }
}
```

Now have ROOT compile and run your code:

```cpp
root -l
.L linspace.cpp+  // The `+` sign compiles the implementation file.
.L testyboi.C     // This just loads the testyboi function into ROOT.
testyboi(2, 6, 8)
// Executes the testyboi function.
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

### Use Poisson (Asymmetrical) Error Bars
```cpp
#include "TH1.h"
{
  TH1D * h1 = new TH1D("h1","h1",50,-4,4);
   h1->Sumw2(kFALSE);
   h1->FillRandom("gaus",100);

   h1->SetBinErrorOption(TH1::kPoisson);

    //example: lower /upper error for bin 20
    int ibin = 20;
    double err_low = h1->GetBinErrorLow(ibin);
    double err_up = h1->GetBinErrorUp(ibin);
    

   // draw histogram with errors 
   // use the drawing option "E0" for drawing the errors
   // for the bin with zero content

   h1->SetMarkerStyle(20);
   h1->Draw("E");
}   
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

### Make a ratio plot

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

### Normalize Hist

```c++
h->Scale(1/h->Integral())
```
