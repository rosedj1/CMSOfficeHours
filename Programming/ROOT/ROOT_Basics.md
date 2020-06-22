# The ROOT of all ~Evil~ High-Energy Physics Data Analysis

Here is a [comprehensive and XKCD-comic-filled tutorial](ROOT_Tutorial_with_XKCD_Pitstops.pdf) on how to use ROOT. If you want the boiled down version, keep reading below.

## Find your ROOTs

**ROOT** is installed with **CMSSW**. So `cd` into a CMSSW environment, like: `cd /path/to/CMSSW_10_2_18/src/`, and then do `cmsenv`. Now you should be able to open up ROOT: `root -l`

- If you need to install a CMSSW environment, [read this](FIXME:link to CMSSW install).
- The `-l` flag keeps the splash window from popping up.

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

## Other ROOT Info

### Some types in ROOT

TString infilename = "path/to/file.root";

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

Use the ROOT interpreter to **test pieces of your code**, before you put it into a script.

## More Resources

- [Nevis Columbia links](https://www.nevis.columbia.edu/~seligman/root-class/links.html)
- [ROOT for Beginners](https://en.wikitolearn.org/ROOT_for_beginners)

- `TChain* tree = sample.getTree();`

## Scrap ROOT code: to organize

```c++
string outputFileName = opts["output"].as<string>();
tree = (TTree*)_infile->Get("tree");
auto t = f->Get<TTree>("tree");
```