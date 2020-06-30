# RooFit

A powerful fitting and statistics package for ROOT.

## Philosophy

Essentially everything in RooFit is a C++ object:

| **RooFit Object** | **...corresponds to...** |
|-------------------|--------------------------|
| `RooRealVar` |      a variable (like x) |
| `RooAbsReal` |      a function (like f(x)) |
| `RooAbsPdf` |       a pdf |
| `RooArgSet` |       a vector (space point) |
| `RooRealIntegral` | integral |
| `RooAbsData` |      list of space points |
| `RooFormulaVar` |   formula with variables |
| `RooDataSet`|       a list of data |
| `RooDataHist` |     a histogram |

- "Abs" stands for **abs**tract
RooDataHist	# a histogram: only accepts values as a RooArgList object

### RooDataSet

A RooDataSet is a list of data. It can be used to do **unbinned fits**.

How to do a binned vs. unbinned fit:

- Put data in RooDataSet -> unbinned fit
- Put data in RooDataHist -> binned fit

Create a RooDataSet:

```c++
TTree* tree = (TTree*)gDirectory->Get("tree");
RooRealVar x("x", "m_{4#mu}", 105, 140, "[GeV]");
RooDataSet data("data", "dataset with x", tree, x)
RooDataSet *data = sum.generate(x,2000);
```

### Put fit parameters on the plot

```c++
RooPlot* xframe = x.frame(RooFit::Title("My RooFit Plot"));  // x is a RooRealVar.
DSCB.paramOn(xframe, RooFit::Layout(xmin, xmax, ymax));  // ymin will be automatically determined.
```

#### Pretty up the plot

```c++
xframe->getAttText()->SetTextSize(0.025);
xframe->getAttText()->SetTextColor(kRed);
xframe->Draw();

TString integ = Form("Integral = %.0f", 136.5);
TLatex* tex = new TLatex(0.6, 0.3, integ);  // TLatex(x_left, y_top, text)
tex->SetNDC();
tex->SetTextColor(kGreen+2);
tex->Draw();
```
