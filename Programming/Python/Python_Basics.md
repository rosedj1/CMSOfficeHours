# Python Basics

## Resources and Tutorials

- For all your Python needs: [Real Python](https://realpython.com/python-first-steps/).
- [Useful reference sheet.](https://pythonprinciples.com/reference/)

Use **Python3**, since Python2 is no longer supported.

Boot up the Python interpreter by typing `python` into your shell. You'll see something like this:

```bash
Python 3.7.4 (default, Aug 13 2019, 15:17:50) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

## Installing Python packages

I **_highly_** recommend using `conda` to manage your Python packages,
but alternatively you can use `pip`:

If you need to install more Python packages (like numpy, vaex, matplotlib, pandas, etc.) then do:

```bash
pip install --user numpy
# Adding the --user flag allows you to install on remote machines,
# when you might not otherwise have the administrator privileges.
```

## Importing Modules

Python looks for modules in `sys.path`:

```python
# Check out your sys.path:
import sys
print(sys.path)
```

As a hack, you can add more paths to this list:

```python
sys.path.append(new_path)
```

Instead, it is better to modify the environment variable `PYTHONPATH`:

```bash
# See what's currently in your PYTHONPATH:
echo $PYTHONPATH
# Append it:
export PYTHONPATH=${PYTHONPATH}:new_path
# TIP: Put this `export` line in your `~/.bash_profile` to have it
# automatically executed on start up.
```

Never use:

```python
from somemodule import *
```

The `*` is the big no-no.
Be explicit in what you import, so a better way would be:

```python
from somemodule import usefulfunction
```

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

```python
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

# Make a dict using a generator:
cjlst_sr_ls_tup = (
    (316666, 781, 1112824102),
    (316877, 47, 74688646),
    (316720, 117, 154779433),
)
cjlst_evtid_sr_dct = {k:['SR'] for k in cjlst_sr_ls_tup}

```

Useful module for naturally sorting strings:
conda install -c anaconda natsort

from collections import OrderedDict  # Make an ordered dictionary.

### Lists

Ordered and mutable objects.

- Probably the most common Python object.

```python
mylist = [1,3,'hey']  # Lists can hold different data types.
mylist.append(4.6)    # Permanently appends value to mylist.

# Make a quick list of strings:
str_ls = 'each word is an element'.split()
# Prints: ['each', 'word', 'is', 'an', 'element']
```

### Tuples

Ordered and immutable objects.

- Just like lists, except **immutable** (*can't append or modify the tuple*).
- They are processed faster than lists.

```python
# Your basic tuple.
mytup = (1,2,3)

# Cool way to unpack a tuple.
x, y, z = (1,2,3)
# print(x)  # Returns 1.
```

### Sets

Unordered and immutable objects.

- good for removing duplicates and for doing math operations like:
union, intersection, subset, etc.

```python
my_set = set(1, 2, 3, 3)
# Reduces to: {1, 2, 3}

# Add elements to set.
my_set.add(4)
# Now contains: {1, 2, 3, 4}

set1 & set2
# Return all elements common to set1 and set2.
set1 | set2
# Return all elements from both set1 and set2.
set1 - set2
# Return a new set with elements from set1 which are NOT in set2.
set1 <= set2
# Return a ???.
```

## Control Flow

### `for` loops

```python
import gc  # Garbage Collector.
# https://rushter.com/blog/python-garbage-collector/
# https://stackify.com/python-garbage-collection/

# Iterate through list1 at the same time as list2
for item1, item2 in zip(list1, list2):
# do stuff
gc.collect()
```

range
- creates an iterable object
- useful for "for loops"
xrange is faster and requires less memory, but has less versatility

Python's "ternary" operator:

```python
[on_true] if [expression] else [on_false]
```

Check the type of an object:

```python
isinstance(obj, float)
# Check if a non-int can be represented as an int:
(4.0).is_integer()
```

### Functions

Variable number of arguments:

```python
def asManyAsYouWant(var, *argv):	# pass in as many arguments into argv as you want
	for arg in argv:					# each one will be iterated over
		print "do stuff"

# NOTE: `argv` is not originally a tuple, but gets passed in as one.
```

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

```python
# In the terminal, do: `python myscript.py arg1  arg2`
sys.argv[0]  # name of script (myscript.py)
sys.argv[1]  # first argument passed to script (arg1)
sys.argv[2]  # first argument passed to script (arg2)
```

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

#### Function Decorators

A **decorator** is a function that "decorates" another function.
Decorators:

- Take in a function as an argument.
- Return a function.

### Classes

A class is a *blueprint* that you use to make objects (think _nouns_, like cars, ninjas, galaxies, etc.):

```python
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def length(self):
        return np.sqrt(self.x**2 + self.y**2 + self.z**2)

# Now you can create objects:
my_vec = Vector(2,3,4)  # Create the object.
my_vec.x                # Get x coord. Returns 2
my_vec.length()         # Get length of myobj. Returns 5.39
```

Use the `namedtuple` data structure to create "quick classes":

```python
from collections import namedtuple
Student1 = namedtuple("Student1", ["name", "gender", "student_id"])
s1 = Student1('Jennifer', 'F', 2020002)
f"Name: {s1.name}; Gender: {s1.gender}; ID #: {s1.student_id}"
# Returns: 'Name: Jennifer; Gender: F; ID #: 2020002'
# We never had to do any `def __init__() stuff!`
```

Built-in methods:

```python
myobj.__dict__  # SUPER USEFUL: returns a dictionary of {attributes:values}
dir(myobj)  # show all the attributes of myobj
__doc__
__init__
__module__
```

Nice way to print out info of your object:

```python
from pprint import pprint
pprint(vars(your_object))
```

Useful statements:
`assert <condition>`    # Quickly check that condition is True. Raise error if not.
Can also do:
assert <condition>, "Error message here"

### Enumeration

[How and why to use enums.](https://florian-dahlitz.de/blog/why-you-should-use-more-enums-in-python#what-is-an-enum)
Enums help to give *names* to numbers:

```python
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 4
    INDIGO = 6

print(Color.GREEN.name)   # Print "GREEN" as str.
print(Color.GREEN.value)  # Print 4 as int.

Color['RED'].value   # Prints 1 as int.
Color(6).name        # Prints "INDIGO".

c = Color.GREEN
c is Color.GREEN  # True.
```

## Packages

### numpy

**Num**erical **Py**thon. Essential and optimized for performing calculations and built-in functions, like sin(), exp(), and much more.

```python
import numpy as np
# Modify certain values in an array:
np.where(<condition>, if_true, if_false)
# Example:
myarr = np.arange(5)
np.where(myarr < 3, -1, myarr)
# Return: array([-1, -1, -1, 3, 4])
```

#### Some Speed Tests

```python
import numpy as np
myarr = np.arange(100000)
%timeit max(myarr)  # 8.08 ms ± 56.3 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
%timeit np.max(myarr)  # 57.4 µs ± 1.68 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
%timeit myarr.max()  # 55.1 µs ± 1.12 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
# CONCLUSION: Use arr.max(), over np.max(arr), over max(arr).

%timeit np.shape(arr)[0]  # 548 ns ± 25.6 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
%timeit len(arr)  # 57.9 ns ± 1.41 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
# CONCLUSION: Use len(arr) over np.shape(arr)[0].
```

### glob

Pattern matching for things like path names and file names.

```python
import glob
file_list = glob.glob("/rosedj1/Higgs/*/Data*.root")  # Stores matched files in a list object.
glob.glob("/home/file?.txt")   # `?' will match a single character: fileA.txt, file7.txt
```

Globbing is not regex! It's standard UNIX path expansion.

How to use wildcards:

| `*` | matches 0 or more characters |
| `?` | matches 1 character in that position |
| `[0-9]` | matches any single digit |

### json

Save your objects for later in a `.json` file:

```python
import json
dct = {'1':'a', '2':'b'}
with open("path/to/newfile.json", "w") as f:
    # Prettify using indent.
    json.dump(dct, f, indent=4, sort_keys=True)
```

- NOTE: The keys of a `.json` file must be `str`.

### pickle

Save your objects for later by "pickling" them:

```python
import pickle    # Or: import _pickle as pickle
my_obj = CoolClass()
with open("outpath/for/pickle.pkl" ,"wb") as outpkl:
    pickle.dump(my_obj, outpkl, pickle.HIGHEST_PROTOCOL)  # Use protocol=2 if using Python2.7 at any point.

del my_obj    # To make sure it's gone.
Easily restore the pickled obj:
with open("outpath/for/pickle.pkl","rb") as inpkl:
    my_obj_again = pickle.load(inpkl)
```

### sys

Access your system's variables, like environmental variables:

```python
import sys
print(sys.version)  # Find out what version of python is running the script
sys.exit()          # Immediately ends program. Useful for debugging.
sys.getsizeof(obj)  # Find out size of any object (in bytes)
```

### os

```python
import os
os.getcwd()					# returns string of current working dir (equivalent to `pwd`)
os.system()					# not recommended, since the output is not stored in a variable; 							only 0 (success) or 1 (failure) will get stored; use module: subprocess instead
os.path.join(<dir1>, <dir2>)		# finds path to <dir1> and <dir2> into single path, supplying '/' as needed
os.path.split(<path/to>/<file>)	# returns a 2-tuple with (<path/to>, <file>) (good for finding the parent dir of <file>)
os.path.exists()				# 
os.makedirs(<dirpath>)			# make directory <dirpath>, recursive
os.environ['USER']				# returns string of current user (same as doing `echo $USER` in bash)
```

### subprocess

Run shell commands within Python:

```python
import subprocess
cmd = ['ls', '-tr']
subprocess.call(cmd)        # Passes the shell command `ls -tr` to the shell.
var = subprocess.check_output(cmd)
var = subprocess.check_output(['ls', '-a'])  # allows you to store output of <cmd> in var

ret_output = subprocess.check_output('date')
print(ret_output.decode("utf-8"))
# Thu Oct  5 16:31:41 IST 2017
```

Clean way:
import shlex, subprocess
command_line = "ls -a"
args = shlex.split(command_line)
p = subprocess.Popen(args)

Example:
import subprocess, shlex

```python
# This is useful:
def shellcmd(command_line):
    args = shlex.split(command_line)
    proc = subprocess.Popen(args)
    return

# My own similar version:
def run_cmd(cmd_str):
    cmd_list = cmd_str.split()
    result = sp.call(cmd_list)

# I'm not sure what the function below is good for:
def processCmd(cmd):
    args = shlex.split(cmd)
    sp = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = sp.communicate()
    return out, err
```

### time

Measure specific time points in your code:

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

NOTE: 2021-04-09:  `optparse` is deprecated. Use `argparse` instead.

Pass in command line options to your script: `python myscript.py --xmin=0 --xmax=10`

**Note:** It is difficult to use **bool**s as input arguments!

- A quick hack is to pass in `0` and `1` instead. *Python is forgiving.* :-)

```python
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument(
    '-x', '--overwrite', dest="ovrwrt", action="store_true",
    help="Overwrite output file. Default is False."
    )
args = parser.parse_args()
overwrite = args.ovrwrt
# Specifying either -x or --overwrite flags will store True in `overwrite`.
# E.g. `python thisscript.py -x`
# Note: 'store_true' is short for:
# `action='store_const', const=True, default=False`
```

```python
import argparse
parser = argparse.ArgumentParser(description='submit all')
parser.add_argument('-v', dest='--verbose', action="store_true")  # Specify just `-v` to get verbose.
parser.add_argument('--min', dest='min_Zmass', type=float, help='min for Zmass')
parser.add_argument('--filename', dest='filename', type=str, help='output file')
parser.add_argument('--widthZ', dest='widthZ', type=float, help='Z width in MC or pdg value')
parser.add_argument('--plotBinInfo', dest='binInfo', nargs='+', help='', type=int)
parser.add_argument('--doubleCB_tail',dest='doubleCB_tail', nargs='+', help='', type=float)
parser.add_argument('--doREFIT', dest='doREFIT', action='store_true', default=False, help='doREFIT')
args = parser.parse_args()

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

### PrettyTable

Print pretty tables to the terminal (stdout).

```python
from prettytable import PrettyTable

t = PrettyTable()
t.field_names = ["mass", "pT", "eta"]  # Headers.
t.add_row([0.105, 50.4, 2.3])
# Note: must add rows, cols, and fields as type `list`.
```

### threading

**Terminology:**

- A motherboard contains one or more **CPUs** (central processing units).
- Each CPU physically sits in a **socket**.
- A CPU is typically split into 1, 2, or 4 **cores**.
- A core is what runs a **process** (a program).
- A core can sometimes run multiple **threads** (tasks of a program).

Example: The Intel Core i9-9900K is a single CPU which sits in 1 socket,
has 8 cores and can run 16 threads.

| **Term** | Definition |
| --- | --- |
| **processor** | CPU, GPU (Graphics PU), APU (Accelerated PU) |
| **core** | A CPU's processor? |
| **process** | A program to run. |
| **thread** | A task. |
| **socket** | The physical seat of a CPU. |

Notes:

- E.g. a motherboard could have 4 CPUs and 4 GPUs.
- A process can be broken up into multiple threads. Think of them as "tasks".
- Threads can only work serially.
- Nowadays CPUs typically have 2 cores.
- A dual-core CPU literally has 2 processing units on the chip.
  - A quad-core CPU has 4 central processing units.

Suppose you have a CPU comprised of 4 physical "cores".

- Each core can only work **serially**, e.g. it can only add two numbers *then* subtract another number.
- But if you work on multilple cores, you can work on processes **in parallel**.
- hyper-threading == simultaneous multithreading

#### Example threading code

```python
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, threadId, name, count):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count

    def run(self):
        print("Starting: " + self.name + "\n")
        print_time(self.name, 1,self.count)
        print("Exiting: " + self.name + "\n")

def print_time(name, delay, count):
    while count:
        time.sleep(delay)
        print ("%s: %s %s" % (name, time.ctime(time.time()), count) + "\n")
        count -= 1

thread1 = MyThread(1, "Thread1", 10)
thread2 = MyThread(2, "Thread2", 5)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Done main thread")
```

pathlib (Python >= 3.5)
import pathlib
pathlib.Path("/path/to/dir").mkdir(parents=True, exist_ok=True)

## Execute other python scripts from a python script

Python3: exec(open("script_to_run.py").read())
Python2: execfile("script_to_run.py")

### *How does the internal variable `__name__` work?*

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

Keep your code **DRY**: "**D**on't **R**epeat **Y**ourself".

That means if you have a nice function that you use over and over,
it is best to write down that function *only once* in some file
and then import that function into other places.

- Added benefit: updating This has the added benefit of only having to  the 

It is best to import 

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

## Meanings of underscores in variable names

A double underscore is often called a **dunder**: `__init__`, `__str__`

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
| --- | --- |
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

**Read lines from a file:**

with open(<filename>) as f:
    content = f.readlines()

  Reading this way will store each line as an element in a list:
data = [line.strip() for line in open('mytext.txt', 'r')]

**Write to a file:**

with open(savePath + saveName + ".txt", "w") as myfile:
   myfile.write('rootPath: ' + rootPath1 + '\n')       
   myfile.write('rootfile: ' + rootfile1 + '\n')       
   for i in range(len(vars1_x)):                       
       myfile.write('var_x: ' + vars1_x[i] + '\n')     
       myfile.write('var_y: ' + vars1_y[i] + '\n')     
       myfile.write('cut: ' + cuts1[i] + '\n')         

Module Import Errors:
Jupyter Notebook: Does `sys.executable` show what you expect?
- Make sure that it points to the spot where your packages are stored.
I have anaconda as my package manager, so I do:

```bash
conda list
# Can also find paths to python executables by doing:
which python
which python3
```

if sys.executable in your JupyterNB doesn't point where you want, 
then you have to change where it points to in the kernel.json file.
Find the file by doing:

```python
from jupyter_core.paths import jupyter_data_dir
print(jupyter_data_dir())
# It will print out some kind of <out/path>
# Then edit the <out/path>/kernel.json to contain the correct path.
# You can find what one possible path could be by doing this in your terminal: which python
```

## IPython

IPython stands for **I**nteractive **Python**.
*Use it frequently!*
Use iPython to test snippets of codelike a quick jupyter notebook for your terminal.
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

```bash
ipython <script.py> -- --arg1 --arg2  # note the '--' between <script.py> and arg1
```

help(<object>)			# brings up a help menu (docstring?) for <object>
e.g. help(os.makedirs)

It is often useful to debug a python script by doing:
python -i <script.py>
- this executes the script and then puts you in the python interpreter
- This is beneficial because now all variables have been initialized and you can play around!

### Useful hotkeys

- `Ctrl + O`: force a new line

## uproot

```python
import uproot

# Open a root file:
f = uproot.open("myfile.root")
# Can directly open up an object:
t = uproot.open("myfile.root:path/to/TTree")
```

### TTrees

```python
t.keys()    # Return a list of branches.
t.values()

branch = t['LepPt'] # Get a whole branch:

t.typenames()  # See the type of each branch.
t.show()       # See even more info about branches.

# Convert a branch to an array (default is 'Awkward Array')"
pt_arr = t["LepPt"].array()
# If this doesn't work you can convert it to a NumPy array (slow):
pt_arr = t["LepPt"].array(library="np")
# Or even a Pandas series:
pt_arr = t["LepPt"].array(library="pd")
```

Use uproot to convert a root file to np.array:

```python
# FIXME
```

### Resources

- [The docs.](https://uproot.readthedocs.io/en/latest/basic.html)
- [Another tutorial.](https://masonproffitt.github.io/uproot-tutorial/aio.html)

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

## Memory Allocation in Python

Every variable in Python is a reference (a pointer) to an object and not the
actual value itself.

```python
# Determine the approximate size of an object:
import sys
print(obj.__sizeof__())
```

## Performance in Python

Run the `cProfile` profiler found in the Python standard library
to check the detailed performance of your code:

```bash
python -m cProfile -o output_file.prof latest_tutorial.py
# Wait for code to run.
python -m pstats output_file.prof
# This takes you to the profile stats browser. It's useful to do:
output_file.prof% strip         
output_file.prof% sort tottime  # `cumtime` counts time when outer fns calls inner fns.
output_file.prof% stats 20      # Show the first 20 lines of stats.
```

`cProfile` is good for identifying which functions consume the most time
but it doesn't tell you *which lines* are troublesome.
Instead, use `line_profiler`:

```python
# Install it.
conda install -c anaconda line_profiler

# Then add the `@profile` decorator above the problem function.
@profile
def big_boi():
    # Function details here.
```

View time details by running the line_profiler in your shell:

```bash
kernprof -l your_script.py
# This will produce a file called: `your_script.py.lprof`. Then do:
python -m line_profiler your_script.py.lprof
```

## Turn your Python script into a shell command

Suppose you have a Python script called, `script.py`.

1. At the very top of your script put:

   ```python
   #!/usr/bin/env python
   ```

2. Make the script executable by the shell:

   ```bash
    chmod u+x script.py
   ```

3. Make a symbolic link to the script:

   ```bash
   ln -s /path/to/script.py ~/bin/script
   ```

   - You may need to create `~/bin` first: `mkdir ~/bin`

4. Make sure `~/bin` is added to the env variable `PATH`:

   ```bash
   export PATH=$PATH:"$HOME/bin"
   ```

   - **TIP:** Put this `export` line into your `.bash_profile`.

5. Now you can execute `script.py` straight from the command line, by typing `script`. Cool!

## Things to look into

- Python3: `inspect`
- root_pandas
- uproot
- `conda install root-c conda-forge`
- import multiprocessing
- datetime.datetime.now()

## To Be Sorted

df.iloc[num] is faster than df.loc[index]

Can save ONE array to a file in .txt format:
np.savetxt('newfile.txt', myarr) 
- Quick and dirty.
- Allows for easy formatting of array.
- Can save multiple arrays so long as they are the same size.

Read a DF from a csv file:
df = pd.read_csv("path/to/file.csv")
Write DF to csv: