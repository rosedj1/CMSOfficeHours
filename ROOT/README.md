# The ROOT of all ~Evil~ High-Energy Physics Data Analysis

## Histograms
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

Rebinning should be rather easy! 
- there is a Rebin method
- Errors are automatically recalculated
Normalizing Histos:
Use: Scale(1/h->Integral)

```c++
// Load histo from root file:
TFile f("histos.root");
TH1F *h = (TH1F*)f.Get("hgaus");

// Make histogram pointer.
TH1F* h = new TH1F("h","My Histogram",100,-20,20)
TH1F h("hgaus", "histo from a gaussian", 100, -3, 3);
h.FillRandom("gaus", 10000);
h->Write();

h->FillRandom("gaus", 5000)		# Fill h1 with 5000 random points pulled from Gaussian Distribution
h->Fill(gRandom->Gaus(4,2))	# Fill h1 with a single point pulled from Gaussian with mu=4, sigma=2
								(do a for loop to fill it with many points)
	for (int i=0; i<1000; i++) {h->Fill(gRandom->Gaus(40,15));}
h->GetEntries()				# Returns how many total values have been put into the bins
h->GetMaximum()				# Returns the number of entries inside the bin which holds the most entries
h->GetMinimum()				# Returns the number of entries inside the bin which holds the fewest entries
h->GetBinContent(<int bin_num>)	# Returns the number of entries inside bin number bin_num
h->GetMaximumBin()			# Tells you which bin holds the most entries; Returns the bin number(not x value of bin!)

	mumuMass->GetXaxis()->GetBinCenter(mumuMass->GetMaximumBin())		# returns most-probable value of histo

h->GetMaximumStored()				# ???
h->GetMean()							# Get average of histogram
h->GetStdDev()						# Get standard deviation of histo
h->GetXaxis()->GetBinCenter(<int bin>)	# returns the x value where the center of bin is located
h->GetXaxis()->SetRangeUser(-5, 5)  // Changes the x-axis range to [-5, 5].
h->GetNbinsX()						# Returns the number of bins along x axis
h->Fill(<int bin_num>, <double val>)		# Fills bin number bin_num with value val
h->SetBinContent(<int bin>, <double val>)	# Deletes whatever is in bin number bin, and fills it with value val
											(this counts as adding a NEW entry!)
h->SetAxisRange(double <xmin>, double <xmax>, "<X or Y>") 	# 
h->IntegralAndError(<bin1>,<bin2>,<err>)					# calculates the integral 
    - err will store the error that gets calculated
    - so before you execute the IntegralAndError, first do err = Double(2) to create the err variable 
h->SetLogy()							# set y axis to be log scale
ACTUALLY CANVAS SETS c1.SetLogy(True)
h->GetName()    # Returns name of histo.

TH2F
h2->Integral()									# calculate integral over ALL bins
h2->IntegralAndError(xbin1, xbin2, ybin1, ybin2, err)	# calculates the integral over square region, specified by bins
- err will store the error that gets calculated
- so before you execute the IntegralAndError, first do err = Double(2) to create the err variable 
h2->Draw("COLZ1")	# "COL" means color, "Z" means draw the color bar, "1" makes all cells<=0 white!

Bin convention:
bin = 0; underflow bin
bin = 1; first bin with low-edge xlow INCLUDED
bin = nbins; last bin with upper-edge xup EXCLUDED
bin = nbins+1; overflow bin

h->Draw()
h->Draw("HIST")	# Make sure to draw a histogram
h->Draw("HIST e")	# Draw histogram with error bars ( where err = sqrt(num_entries_in_bin) )
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