# Python Basics

## Resources and Tutorials

- For all your Python needs: [Real Python](https://realpython.com/python-first-steps/).

Use **Python3**, since Python2 is no longer supported.

Boot up the Python interpreter by typing `python` into your shell. You'll see something like this:

```
Python 3.7.4 (default, Aug 13 2019, 15:17:50) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

## Anaconda

"[Package, dependency and environment management for any language](https://conda.io/en/latest/) — 
Python, R, Ruby, Lua, Scala, Java, JavaScript, C / C++, FORTRAN, and more."

```python
conda install package
conda install scipy=2.3.4 -n my_env  # Can install specific versions into specific virtual envs.
```

help(<object>)			# brings up a help menu (docstring?) for <object>
e.g.	help(os.makedirs)	

It is often useful to debug a python script by doing:
python -i <script.py>
- this executes the script and then puts you in the python interpreter
- This is beneficial because now all variables have been initialized and you can play around!

## How to structure your project

Never use `from somepackage import *`

- **Cool trick:** Use the Linux command `tree` to see your directory structure.

## Printing and Formatting

The preferred way to print is to use "f-strings":

```python
var1 = "this"
var2 = "AWESOME"
mystr = f"Use brackets like {var1} and even call methods: {var2.lower()}"

# Specify precision, padding, alignment:
val = 12.3
print(f"the value is {val:>7.4f}")
# The `.4f` means to 4 decimal places as a float
# The `7` means to pad using a width of 7 chars
# The `>` means "right-aligned"

# You can do multiline f-strings:
msg = (
    f"Put your text on {num_lines} lines."
    f"It looks really good this way!"
)
```

If you are (unfortunately) working in Python2, then you can import f-strings.
Simply put this at the top of your code:
`# -*- coding: future_fstrings -*-`

Another flexible way to print variables:

```python
print "Hello, {}. You are {}.".format(name, age)
# You can specify which var goes where:
print "Hello, {1}. You are {0}.".format(age, name)
# General format:
# {<var>:<width>.<prec><type>}

# Example:
print "Time={:.1f}, {:15.4E}".format(t, nanosec)
# Here the :15 will "pad" (make room for) 15 chars

# Other useful tricks:
{:>8}     # Pad with 8 spaces, align text to the right.
{:8}      # Default aligns left.
{:_>8}    # Pad with '_' chars.
{:^8}     # Align to the center.
{:8.5}    # Pad with 8 spaces, but keep only first 5 chars of string. 
{:d}      # Digit (integer).
{:06.2f}  # Floats.
# - This pads 6 spaces, puts 0's out front, at a decimal precision of 2.
```

Least preferred way to print:

```python
"Hello, %s. You are %s." % (name, age)		# called "%-formatting", not suggested by the docs!
- However, this method seems the most reliable and easy to read when using LaTeX substitution.
Example: cuts =  r"$%.1f < m_{\mu\mu} < %.1f$ GeV" % (self.massZ_min, self.massZ_max)
- If you tried to use .format, then the m_{...} would be mistaken for a variable substitution. 
    - I think you can escape this though by doing double m_{{\mu\mu}}
```

## The most common objects in Python

### Dictionaries

mydict = {}
- Mutable

Dictionaries work by using 'key', 'value' pairs. 
- Using a key on a dictionary, reveals the corresponding value.
mydict = {'a':1, 'b':9}
So `mydict['b']` gives 9
Add a new key, value pair:
mydict["this is neat"] = "some new value"

Check if a key is in your dict:
`'a' in mydict` gives True

Alternative way to retrieve values:
mydict.get('b')

Delete a key,value pair:
del mydict['a']
- Will remove the key 'a' and its value

Get an iterable of all the keys:
mydict.keys()
- Note: you'll have to convert this to a list!
- Like: list(mydict.keys())

Get an iterable of all the keys:
mydict.values()    # Again, convert this to a list!

Get an iterable of all the (key,value) pairs:
mydict.items()     # Convert to a list and you will have a list of tuples.

Combine dictionaries into a single dict:
mydict.update(other_dict)

Iterate over values:
for val in mydict.values():
Iterate over keys and values:
for key,val in mydict.items():
	print "The key is:", key, "and the value is:", val
iterkeys()

Sort by keys, return values:
sorted_ls_of_vals = [value for (key, value) in sorted(my_dict.items())]
Sort by values, return keys:
sorted_ls_of_keys = sorted(my_dict, key=my_dict.__getitem__)

### Lists
- Unordered and mutable!
mylist = [1,3,'hey']			# lists can hold different data types
mylist.append(4.6)			# permanently appends value to mylist

### Sets
Unordered, immutable objects
- good for removing duplicates and for doing math operations like: union, intersection, subset, etc.

`set(1, 2, 3, 3)`
- returns: {1, 2, 3}

`set1 & set2`
- returns all elements common to set1 and set2
`set1 | set2`
 - returns all elements from both set1 and set2
`set1 - set2`
- return a new set with elements from set1 which are not in set2
`set1 <= set2`
- return a 

### Tuples
- Ordered and immutable!
Very similar to lists... except tuples are immutable!
They are processed faster than lists


for loops
for item1,item2 in zip( list1,list2 ):	# will iterate through item1 at same time as item2
	# do stuff

range
- creates an iterable object
- useful for "for loops"
xrange is faster and requires less memory, but has less versatility

Ternary operator: 
```python
[on_true] if [expression] else [on_false]
```

How to check the type of an object:
isinstance(obj, float)

### Functions

Variable number of arguments:
def asManyAsYouWant(var, *argv):	# pass in as many arguments into argv as you want
	for arg in argv:					# each one will be iterated over
		print "do stuff"

- NOTE: argv is a tuple!

Lambda functions
A way to write quick functions

square = lambda x: x**2
pythag = lambda x,y: np.sqrt(x**2 + y**2)
ls = lambda : os.listdir()
printstuff = lambda *args: print args
- can handle any number of arguments
Call these functions with: 
- square(), pythag(), etc. 

Probably safer to put the arguments of an if statement in parentheses:
if (not os.path.exists(<path_to_dir>)): print "this dir doesn't exist"

Passing arguments to script:
myscript.py  arg1  arg2
sys.argv[0]	# name of script (myscript.py)
sys.argv[1]	# first argument passed to script (arg1)
sys.argv[2]	# first argument passed to script (arg2)

Useful string methods:
<string>.lstrip()			# temporarily removes whitespace from beginning of <string> to first non-whitespace char
<string>.rstrip('/')			# temp. remove a '/' from the right-part of <string>
<string>.startswith('#')		# return bool if string starts with '#'
mystr.strip('e')    # Removes ALL 'e' chars at beginning and end of mystr.

module 	= container for code, e.g. a .py file (which is called a submodule!)
package = modules that contain other modules, e.g. a directory with an __init__.py file
Module vs. Script:
- a module gets imported into other modules: `import numpy`  # numpy is a module 
- a script is executed by the Python interpreter  # `python script.py`  # Though script is a module!
- Remember that 

### Classes

A class is a *blueprint* that you use to make objects (like cars, ninjas, galaxies, etc.).


```python
class Vectors:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def length(self):
        return np.sqrt(x**2 + y**2 + z**2)

# Now you can create objects:
myobj = Vector(9,4,2)  # Create the object.
myobj.x                # Get x coord.
myobj.length()         # Get length of myobj.
```

Built-in methods:__doc__
__init__
__module__
__dict__
dir(myobj)		# show all the attributes of myobj
myobj.__dict__		# returns a dictionary of {attributes:values}


Useful statements:
`assert <condition>`    # Quickly check that condition is True. Raise error if not.
Can also do:
assert <condition>, "Error message here"

---

## Packages

numpy
import numpy as np
Modify certain values in an array:
np.where(<condition>, if_true, if_false)
Example:
>>> np.where(np.arange(5) < 3, -1, myarr)
array([-1,-1,-1,3,4])

Speed tests:
import numpy as np
myarr = np.arange(100000)
%timeit max(myarr)  # 8.08 ms ± 56.3 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
%timeit np.max(myarr)  # 57.4 µs ± 1.68 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
%timeit myarr.max()  # 55.1 µs ± 1.12 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
- Use arr.max(), over np.max(arr), over max(arr)

%timeit np.shape(arr)[0]  # 548 ns ± 25.6 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
%timeit len(arr)  # 57.9 ns ± 1.41 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
- Use len(arr) over np.shape(arr)[0]



### glob

```python
import glob
file_list = glob.glob("/rosedj1/Higgs/*/Data*.root")  # stores matched files in a list object!
glob.glob("/home/file?.txt")  # `?' will match a single character: fileA.txt, file7.txt
```

Remember, that it's not regex! It's standard UNIX path expansion.
How to use wildcards:

| `*` | matches 0 or more characters |
| `?` | matches 1 character in that position |
| `[0-9]` | matches any single digit |

pickle
Save your objects for later use by "pickling" them:
```python
import pickle    # Or: import _pickle as pickle
my_obj = CoolClass()
with open(<file_to_write_to>.pkl,'wb') as outpkl:
    pickle.dump(my_obj, outpkl, pickle.HIGHEST_PROTOCOL)

del my_obj    # To make sure it's gone.
Easily restore the pickled object:
with open(<file_written_to>.pkl,'rb') as infile:
    my_obj_again = pickle.load(infile)
  ```


sys
import sys
print sys.version			# find out what version of python is running the script
sys.exit()					# Immediately ends program. Useful for debugging. 
sys.getsizeof(obj)    		# Find out size of any object (in bytes)

os
import os
os.getcwd()					# returns string of current working dir (equivalent to `pwd`)
os.system()					# not recommended, since the output is not stored in a variable; 							only 0 (success) or 1 (failure) will get stored; use module: subprocess instead
os.path.join(<dir1>, <dir2>)		# finds path to <dir1> and <dir2> into single path, supplying '/' as needed
os.path.split(<path/to>/<file>)	# returns a 2-tuple with (<path/to>, <file>) (good for finding the parent dir of <file>)
os.path.exists()				# 
os.makedirs(<dirpath>)			# make directory <dirpath>, recursive
os.environ['USER']				# returns string of current user (same as doing `echo $USER` in bash)


pathlib (Python >= 3.5)
import pathlib
pathlib.Path("/path/to/dir").mkdir(parents=True, exist_ok=True)


subprocess
Python can run shell commands
import subprocess
subprocess.call( ['<cmd1>', '<cmd2>', ...] )		# passes commands to shell
var = subprocess.check_output(<cmd>)		# allows you to store output of <cmd> in var
var = subprocess.check_output(['ls', '-a'])

ret_output = subprocess.check_output('date')
print ret_output.decode("utf-8")
- Thu Oct  5 16:31:41 IST 2017

Clean way:
import shlex, subprocess
command_line = "ls -a"
args = shlex.split(command_line)
p = subprocess.Popen(args)

Example:
import subprocess, shlex                                                       

# This is useful:
def shellcmd(command_line):                                                                                            
	args = shlex.split(command_line)
	proc = subprocess.Popen(args) 
	return
                  
My own similar version:
def run_cmd(cmd_str):
    cmd_list = cmd_str.split()
    result = sp.call(cmd_list)

# I'm not sure what the function below is good for:
def processCmd(cmd):                                                                                            
    args = shlex.split(cmd)                                                    
    sp = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = sp.communicate()                                                                           
    return out, err                                                            


### time


```python
import time
time.perf_counter()  # Stands for "performance counter"
# - This gives you a number of seconds elapsed since the program began. 
# - Handy for taking differences in times:
start = time.perf_counter()
# <lots of tasty code>
end = time.perf_counter()
elapsed_time = end - start
print(elapsed_time)
```

### argparse

Pass in command line options to your script: `python myscript.py --xmin=0 --xmax=10`

**Note:** It is difficult to use **bools** as input arguments!

- A quick hack is to pass in `0` and `1` instead. *Python is forgiving.* :-)

```python
import argparse
def ParseOption():
    parser = argparse.ArgumentParser(description='submit all')
    parser.add_argument('--min', dest='min_Zmass', type=float, help='min for Zmass')
    parser.add_argument('--filename', dest='filename', type=str, help='output file')
    parser.add_argument('--widthZ', dest='widthZ', type=float, help='Z width in MC or pdg value')
    parser.add_argument('--plotBinInfo', dest='binInfo', nargs='+', help='', type=int)
    parser.add_argument('--doubleCB_tail',dest='doubleCB_tail', nargs='+', help='', type=float)
    parser.add_argument('--doREFIT', dest='doREFIT', action='store_true', default=False, help='doREFIT')
    args = parser.parse_args()
    return args

# Call the function.
args = ParseOption()
# Retrieve values from args object.
args.Z_width
massZErr_rel_min = args.min_relM2lErr

# This is the correct way to handle accepting multiple arguments.
# '+' == 1 or more.
# '*' == 0 or more.
# '?' == 0 or 1.
# An int is an explicit number of arguments to accept.
parser.add_argument('--nargs', nargs='+')

# To make the input integers
parser.add_argument('--nargs-int-type', nargs='+', type=int)
```

# Execute other python scripts from a python script:
Python3: exec(open("script_to_run.py").read())
Python2: execfile("script_to_run.py")

How does the internal variable `__name__` work?
When the python interpreter runs over a script, it sets that module's 
__name__ variable to "__main__". 
Example:
Think of it as each module (Python script) having its own __name__ variable.
Suppose you have two modules: 
1. script.py
2. another.py  # which has this inside: import script
Compare these:
python script.py  
- __name__ gets set to "__main__"
python another.py  
- __name__="__main__"(for another.py)
- __name__="script" (for script.py)
If script.py had the canonical `if __name__=="__main__":` block, 
then that block would NOT execute when script.py gets imported into another module!

Find indices of the minimum of arr:
np.unravel_index(np.argmin(<arr>, axis=None),<>.shape)

Suzanne discovered how to **modify the size of different axes** (e.g. to add a ratio plot!):

```python
fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True, gridspec_kw={'height_ratios': [3, 1]})
```

## Importing Packages and Modules

If you get ImportError, then most likely the python interpreter doesn't know the path to your package
1. Do echo $PYTHONPATH to see which paths the python interpreter knows about
2. Do export PYTHONPATH=$PYTHONPATH:<path/to/package>    # permanently append <path/to/package> to $PYTHONPATH
3. Make sure that you have the file __init__.py in each dir of your package.
    - can do: find <path/to/package> -type d -exec touch '{}/__init__.py' \;
More on this: https://askubuntu.com/questions/470982/how-to-add-a-python-module-to-syspath/471168

sys.path 							# list of python packages; python searches these file paths for packages to use
sys.path.append(<path/to/package>)	# temporarily append <path/to/package> to PYTHONPATH
sys.path.insert(0, <path/to/package>)	# temporarily insert <path/to/package> to PYTHONPATH as the 0th element in the sys.path list

import os,ROOT,pickle                                                                   
from .Utils.processCmds import processCmd                                               
                                                                                        
class Hadder(object):                                                                   
    def haddSampleDir(self,dir_path):                                                   
        processCmd('sh '+os.path.join(dir_path,"hadd.sh"))                              
                                                                                        
    def makeHaddScript(self,dir_path,sampleNames,outputInfo):                           
        haddText="hadd -f {0} ".format(dir_path+"/"+outputInfo.TFileName)               
        basedir = os.path.dirname(dir_path)+"/"                                         
        for sampleName in sampleNames:                                                  
            haddText += " {0}/*_{1}".format(basedir+sampleName,outputInfo.TFileName)+" "
            #haddText += "\n"                                                           
        outTextFile = open(dir_path+"/hadd.sh","w")                                     
        outTextFile.write(haddText)                                                     

np.log10(x)
dir(numpy)
- gives big list of all available functions in numpy
lists:
x= [3,-1,5.5,0]
np.mean(x) —> 1.875
map(np.exp,x)
- ^maps a function to each element to a list
Define an array of ‘r’ values and one of ‘theta’ values
a = np.arange(1,10).reshape(3,3) —> makes a 3x3 array
a.size	# 
a.shape	# 
np.linspace(start,stop,number_of_values)

np.arctan2(y,x)
Element-wise arc tangent of x1/x2 choosing the quadrant correctly.

Meanings of underscores in variable names:
By the way, a double underscore is often called a 'dunder'!
_var		# when you import using, say: 'from ROOT import *', then '_var' will not be imported
                - single underscores are meant for variables for internal use only (within classes, e.g.); not enforced by interpreter
var_		# this one's easy: a trailing underscore is used simply to avoid naming conflicts (e.g., class_ = 'just a regular string')
__var		# interpreter will intentionally name-mangle this var so that it doesn't get overwritten
__var__	# only used for special vars native to the Python language; don't define these yourself!
_		# used as a placeholder var in a function or something; a 'throw-away' variable

## Naming Conventions in Python

- **modules** (filenames like `my_script.py`) should have short, all-lowercase names, with underscores
- **packages** (directories) should have short, all-lowercase names, preferably without underscores
- **classes** should use the CapWords convention.

| Type | Public |
| ---- | ------ |
| Packages | `lower_with_under` |
| Modules | `lower` |
| Classes | `CapWords` |
| Exceptions | `CapWords` |
| Functions | `lower_with_under()` |
| Global/Class Constants | `CAPS_WITH_UNDER` |
| Global/Class Variables | `lower_with_under` |
| Instance Variables | `lower_with_under` |
| Method Names | `lower_with_under()` |
| Function/Method Parameters | `lower_with_under` |
| Local Variables | `lower_with_under` |

| Global/Class Constants | CAPS_WITH_UNDER |
- If you want to make an **Internal names** then just *precede* the name with a '_': `_`

Reading from and writing to files:
Read lines from a file:
with open(<filename>) as f:
	content = f.readlines()

Write to a file:
with open(savePath + saveName + ".txt", "w") as myfile:
   myfile.write('rootPath: ' + rootPath1 + '\n')       
   myfile.write('rootfile: ' + rootfile1 + '\n')       
   for i in range(len(vars1_x)):                       
       myfile.write('var_x: ' + vars1_x[i] + '\n')     
       myfile.write('var_y: ' + vars1_y[i] + '\n')     
       myfile.write('cut: ' + cuts1[i] + '\n')         
myfile.close()  # don't even need this                                     

Reading this way will store each line as an element in a list:
data = [line.strip() for line in open('mytext.txt', 'r')]


Module Import Errors:
Jupyter Notebook: Does `sys.executable` show what you expect?
- Make sure that it points to the spot where your packages are stored.
I have anaconda as my package manager, so I do:
conda list
Can also find paths to python executables by doing:
which python
which python3

if sys.executable in your JupyterNB doesn't point where you want, 
then you have to change where it points to in the kernel.json file.
Find the file by doing:
from jupyter_core.paths import jupyter_data_dir
print(jupyter_data_dir())
- It will print out some kind of <out/path>
- Then edit the <out/path>/kernel.json to contain the correct path.
- You can find what one possible path could be by doing this in your terminal: which python

## IPython

IPython is like a quick jupyter notebook for your terminal.
Extremely useful for its "magic" commands, tab completion, 
and ability to go back and edit blocks of code.

```python
?			# Intro and overview of IPython
%quickref	# quick reference

A command that starts with % is called a "line magic" and %% is called a "cell magic"
- these are non-native to C++ or python, but understood by the IDE for really cool effects!

%magic			# bring up tutorial on magics
%lsmagic			# bring up magic commands
%<magicname>?	# get help on <magicname>

Cell Magic:
%%!		
<commands>		# begins a cell magic and then passes the cell to the shell 
```

If you need to pass in arguments into a script using ipython:

```python
ipython <script.py> -- --arg1 --arg2	# note the '--' between <script.py> and arg1
```

## uproot

`import uproot`

Use uproot to convert a root file to np.array:
- https://masonproffitt.github.io/uproot-tutorial/aio.html

Open your root file:
f = uproot.open(<file.root>)

See what branches and objects are stored inside:
f.keys()

df.iloc[num] is faster than df.loc[index]

Can save ONE array to a file in .txt format:
np.savetxt('newfile.txt', myarr) 
- Quick and dirty.
- Allows for easy formatting of array.
- Can save multiple arrays so long as they are the same size.

Read a DF from a csv file:
df = pd.read_csv("path/to/file.csv")
Write DF to csv:

## The logging Module

The ultimate Python debugger. There are 5 levels of debuggification:
 
1. Debug
2. Info
3. Warning
4. Error
5. Critical

```python
import logging

# Create and configure logger.
logging.basicConfig(filename = "path/to/file.log",  # If DNE, Python will make it.
                    level = logging.DEBUG)  # Default level is >=30 (WARNING), so make it DEBUG instead.
logger = logging.getLogger()

# Test the logger.
logger.info("Log message here.")
# Will print into file.log: 'INFO:root:Log message here.'
```

It is useful to print the time, etc.:

```python
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"  
# More info at: https://www.python.org/dev/peps/pep-0282/

logging.basicConfig(filename = "path/to/file.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = "w")  # Will overwrite the existing file. 

# Test messages.
logger.debug("A harmless debug message.")
logger.info("Hey, there you are. You're there.")
logger.warning("Watch it, buddy.")
logger.error("Pi is not exactly 3.")
logger.critical("The Ancient One is awakening.")
```

---

## Jupyter Notebooks

Good for exploratory coding. 
NOT good for big team coding.
Consider using PyCharm for a similar experience AND a variable explorer(?).

Why do I use Jupyter Notebooks?
- They are modular: run cells in any order, rerun them, 
- Easy to copy/paste
- Multiple cursor features
- Plots show up in the notebook
- Can still run bash commands
- Tab completion

Tips and Tricks:

```python
!echo "run bash commands"    # A bang `!` lets you execute bash commands.
print("Don't show output");  # A semicolon at the end supresses output.

# Useful shortcuts:
Enter    # Enter edit mode.
Esc      # Enter command mode.

# In command mode:
H    # Help and hotkey menu. 
P    # Open command palette.
K    # Go to cell above (like Vim).
J    # Go to cell below (like Vim).
A    # Add cell above.
B    # Add cell below.
F    # Enter find-replace mode.
X    # Delete current cell.
C    # Copy selected cells.
V    # Paste selected cells.
O    # Condense/Expand cell output.
M    # Change cell to Markdown text.
Y    # Change cell to code.

Shift + J    # Highlight current cell and one below.
Shift + K    # Highlight current cell and one above. (Thanks, Vim!)
Shift + M    # Merge multiple cells into one.

In edit mode:
Shift + Tab         # Look up Docstring of function/class. VERY POWERFUL. Cursor must be on function.
- You can also cycle by doing `Shift + Tab` over and over.
Ctrl + Shift + -    # Split current cell in two.
Cmd + /             # (Un)Comment all highlighted code.
Cmd + D             # Delete line.
Cmd + ]             # Indent right.
Cmd + [             # Indent left.

Hold Opt (or Alt) and drag cursor    # Rectangular selection.
Cmd + click    # Use multiple cursors on different lines.
```

### Jupyter Markdown

Use LaTeX font simply by typing normal LaTeX text:

- `$ \frac{\sigma}{x} $`

Favorite magics:

```python
%config InlineBackend.figure_format = 'retina'    # Show incredibly high-resolution images:
%matplotlib inline      # Show plots in Jupyter Notebook.
%matplotlib notebook    # Make INTERACTIVE plots!

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"    # Show output of all lines
# InteractiveShell.ast_node_interactivity = "last_expr"    # Show output of just last line (default).
```

Neat extensions:
Themes:
pip install jupyterthemes
Dark theme:
In your terminal: jt -t chesterish
restore the main theme:
jt -r 

You can use jupyter notebooks on remote machines!

1. On remote machine: jupyter notebook --no-browser --port=8881
2. On local machine: ssh -NL 8888:localhost:8881 <UN@host.server.com>
3. In browser, go to: localhost:8888

---

## Things to look into

- Python3: `inspect`
- root_pandas
- uproot
- `conda install root-c conda-forge`
- Topics to research:
- import multiprocessing
- datetime.datetime.now()