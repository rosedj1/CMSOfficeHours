# Vaex

- [ ] Which is faster?
- root2array -> DataFrame(arr) -> df.to_csv() 
- each time, instead of saving the arr and loading 
[ ] Still having memory trouble...
4 GB root file can be converted to a DataFrame. 
The DF can be saved as these files types with the follow sizes:
== 7.97 GB hdf5
== 8.06 GB arrow
== 17.68 GB csv
- I think feather beats all these... but not sure.
You can convert root files directly into hdf5 files!
Do the shell command (after doing `cmsenv`):
root2hdf5 <file.root>

Loading a ~4 GB root file into a DataFrame, consumes too much RAM.
I have stored these DFs to disk (HDF, feather) but it takes too long
to load them and, again, you then hold the DF in memory. VERY BAD!
- The 'vaex' package IS the solution!

It's quite CPU intensive to:
1. root2array
2. make arr into DataFrame
3. save df as .csv file. 
- Use: df.to_feather(outfile)
- Fast and efficient storage type.
EVEN BETTER? Use uproot

Looks like the package 'vaex' may be the way to go when working with large datasets.
- It doesn't load the DF into memory! 
- It calls the data on demand, keeping it on disk. 
import vaex
Load a DF into memory (bad!) from a csv:
vdf = vaex.from_csv("path/to/data.csv")
- Took 4m59s to load 15E6 rows (bad!)
Convert to 'hdf5' format:
vdf.export_hdf5("path/to/data.hdf5")
Open hdf5 file and load DF:
vdf_fromhdf5 = vaex.open("path/to/data.hdf5")    # Can also use: csv, hdf5, etc.
- Took 153ms to load 15E6 rows (AMAZING!)
- This DF is not stored in memory! The data are called as needed. 
- open() is the general method and is slower than a specific method like: `from_`

Convert to 'arrow' format:
vdf.export_arrow("path/to/data.arrow")  # or:
vdf.export("path/to/data.arrow")
- Can export to other formats.
Try to open arrow file, but it failed as of 2020/05/07:
vdf_fromarrow = vaex.open("path/to/data.arrow")
- Unfortunately not able to open DF from arrow file...
- Get: AttributeError: 'pyarrow.lib.Column' object has no attribute 'chunk'

What ultimately worked for me:
Had to go from csv -> hdf5:
`vdf = vaex.from_csv("path/to/data.csv")`
`vdf.export_hdf5("path/to/data.hdf5")`
`vdf_fromhdf5 = vaex.open("path/to/data.hdf5")`    # This dude consumes no RAM!!!

- Unable to load a DF from a file.arrow! :-(
- Stick with hdf5.
- Another note: when a pandas DF converts a file to hdf5, it is not compatible with vaex hdf5. So must go through csv first.

Can open many files at once:
df_names_all = vaex.open_many(['file1.hdf5', 'file2.hdf5'])

vaex
An incredible out-of-memory big data analyzer. 
- It uses Vaex DataFrames (VDF) objects, sometimes called Datasets.
import vaex
vdf = vaex.open("path/to/data.hdf5")

Get the expression that references the column 'pT1':
vdf.pT1  # Equivalently: vdf["pT1"]
- This is an out-of-memory column of your data!!!
Get the corresponding numpy array:
vdf.pT1.values  # A regular numpy array instead of an expression.

expressions can use .where(), similar to numpy.where()
- vdf.phi1.where((vdf.pT1 < 50), 5)
- but it's not working as expected...

Check out all expression methods here:
https://vaex.readthedocs.io/en/latest/api.html#expression-class

SELECTIONS:
Filter the col and IT DOESN'T MAKE A COPY!
Get a bool expression:
vdf.pT1 > 45
- Returns the pT1 values as an expression.
This should be very useful but it's not working properly:
vdf.pT1.where( (vdf.pT1 > 45),  3)
- Only returns a bool array when should return pT1 vals.
- I don't think the 3 does anything...

Get a subset of the VDF using a bool expression:
subset = vdf[vdf.pT1 > 45]

Get values while making a selection:
x_vals = vdf.evaluate("d0BS1", selection=vdf.pT1 < 30)
x_vals = vdf.evaluate("d0BS1", selection="pT1 < 30")
- NOTE: evaluate() returns a np.array
Alternatively:
selec = vdf.pT1 < 30
x_vals = vdf[selec].d0BS1.evaluate()

Make a mask that vaex remembers?
selec = vdf.select((vdf["pT1"] > 50) & (vdf["pT1"] < 60))

HANDY EXPRESSION METHODS:
Evaluate some stats on an expression:
vdf.pT1.abs()
vdf.pT1.sum()
vdf.pT1.mean()
vdf.pT1.clip(50, 60)  # vals<50 become 50 and vals>60 become 60.
vdf.pT1.count()

- 

PLOTTING:
Plot a histogram (so freaking easy!):
vdf.plot1d(vdf.pT1)  # pT1 is one of the columns in vdf.
- Can of course do: getattr(vdf, "pT1")
vdf.plot1d(vdf.pT1, selection="pT1 < 30", limits=[0,50], marker="")

Make a 2-D plot:
vdf.plot(vdf.d0BS1, vdf.pT1)  # (x_var, y_var)



OTHER COOL STUFF:
Combine two VDFs:
vdf_combined = vdf1.concat(vdf2)

Drop a column:
vdf.drop("pT1", inplace=True)  # inplace=True results in a permanent change.

Use the vdf.apply() method to apply a function to all rows in a VDF:
- it is fast too!
Example:
def calc_dphi(phi2, phi1):
    dphi = phi2 - phi1
    while (dphi >= np.pi): dphi -= 2*np.pi  
    while (dphi < -np.pi): dphi += 2*np.pi
    return dphi
vdf.apply(calc_dphi, (vdf.phi2, vdf.phi1))
- 9.16 ms ± 1.25 ms per loop (mean ± std. dev. of 7 runs, 100 loops each)
Compare that time to:
tmp_dphi = vdf.phi2 - vdf.phi1
np.where((tmp_dphi.values < -1*np.pi), tmp_dphi.values + 2*np.pi, tmp_dphi.values)
np.where((tmp_dphi.values >    np.pi), tmp_dphi.values - 2*np.pi, tmp_dphi.values)
- 372 ms ± 3.23 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
- Using .values takes a long time. 
- Had to iterate over all entries twice! (bad)
Another test to confirm that vdf.apply() is the way to go:
%timeit vdf['explicit'] = np.sqrt(deta2_ser**2 + dphi2_ser**2) 
%timeit vdf['apply'] = vdf.apply(calc_dR, (deta2_ser, dphi2_ser))
- 9.13 ms ± 1.78 ms per loop (mean ± std. dev. of 7 runs, 100 loops each)
- 5.86 ms ± 897 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
HOWEVER... Perhaps it isn't as fast as doing native 
expression manipulation...

Convert a VDF to a pandas DataFrame:
df = vdf.to_pandas_df()