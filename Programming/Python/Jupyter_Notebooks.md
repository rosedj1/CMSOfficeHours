# IPython and Jupyter Notebooks

An interactive playground to test Python code.

## Useful Hotkeys (for a Mac)

```
Cmd + ]   # tab/indent
Cmd + [   # untab/dedent
Cmd + /   # comment highlighted text (also uncomments)
X         # delete selected cell
Z         # undo cell deletion
Ctrl + Shift + '-'    # Split cell. 
```

Other cool tricks:
Click the left part of the output of a cell to contract and scroll through the output

- makes your Jupyter Notebook more manageable

You can incorporate HTML into markdown cells:

```html
<img src="https://drive.google.com/uc?export=view&id=1ouoxR1b2bgBv7hKrO8jhpoWg5vfgYhT6" alt="drawing" width="400" align='left' style='float:right'/>
<br><br>
# *Signal Exploration<br>X &#8594; YH &#8594; 4b*
Author: Suzanne Rosenzweig
```

## Magic

Jupyter has special **magic commands**. They come in two flavors:

1. **line magics** start with one `%` symbol: `%timeit normal_code_here`
2. **cell magics** start with `%%` and must be at the top of the cell:

### Useful magics

```python
%%capture

```

## Also look into

- Jupyter lab
- jhub (Jupyter Hub)
