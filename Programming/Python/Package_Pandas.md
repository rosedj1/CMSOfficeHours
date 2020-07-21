# Pandas

The package **pandas** gives us a way to analyze data in *DataFrames* (essentially a spreadsheet). 

**Terms:**

- **DataFrames** (df): A table of data
- **Series** (ser): A column of data.

Examples:

```python
import pandas as pd
ser = pd.Series(np.arange(10))  # Make a quick Series (column of data).

df = pd.DataFrame(np.random.randn(15,6), columns='A B C D E F'.split())  # Make a quick DataFrame (table of data - like a spreadsheet!)
```

Select the row labeled "3": `df.loc[3]`
Select the 3rd row:
df.iloc[3]    # Stands for "integer-location"
Select entries 3-8:
df.iloc[3:8]    # Still exclusive at both ends, like regular Python.
- This will display the row as a Series.
- Make it look like a DataFrame with an extra `[]`: `df.loc[[3]]`
NOTE: df.loc is a very flexible method!

Add a new series (column) to your existing DF:
df.loc[:,'p1'] = df['pT1'].values / np.sin( df['theta1'].values )
- Only need to do the `.loc` on the LHS, if you are slicing the same df on the RHS.

Drop the series 'pT1' temporarily:
df.drop('pT1')
Make it a permanent change:
df.drop('pT1', inplace=True)

A very efficient way to play with series and DF is by boolean slicing:
ser > 5
- returns a boolean series (Trues and Falses)
Put this back into the original series to get only those values which are > 5:
ser[ser > 5]
- this will NOT be the same size as ser!

Put Series side-by-side for comparison studies:
pd.DataFrame( {'First Col':ser1,
				'Another col':ser2} )

DataFrames are a little tricky to deal with, as far as implementing if/then statements, for loops, etc.
- VECTORIZE!
- Avoid .apply() method!
- swifter is a nice alternative to .apply()
    - simply do: import swifterthen instead of .apply(fn), do: swifter.apply(fn)

Keep entries where ser > 2 and put NaN in all other entries:
ser.where(ser > 2)
- This preserves the original shape of ser
Replace all entries where the condition is satisfied with a value:
ser.mask(ser > 3, 0)
- mask() and where() kind of do inverse things.

if/then -> df.mask(<condition>, <value_when_true>)

Series are friendly to play with, as compared to numpy arrays. 
- This is especially true when you want to only modify certain values of a Series which meet a certain condition
- This is when the mask/where methods are useful.
- numpy arrays don't have native mask-like methods. 

To check the len of a series, it is slower (and more difficult to read) to do:
len(df[ df['col3'] > 5 ])
so use this faster way instead:
sum( df['col3'] > 5 )
However, it is faster to check the rows of a DF by doing:
len(df)

Potentially good methods for DFs:

```python
df.assign
df.rename
df.query
df.sort_values
df.reset_index
df.sample()    # Returns a random row of the DF. 
df.pipe(<fn>)  # Apply a custom function to the DF (in-place!).
```
