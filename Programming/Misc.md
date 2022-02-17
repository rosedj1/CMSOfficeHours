# Tips and Tricks with Other Software

- Make reusable, modular, adaptable code. Make each function a strong, independent Lego block.
- [Here's some great programming advice.](https://pythonprinciples.com/blog/getting-unstuck/)

## Skype

```bash
*<words>*           # Make <words> bold.
_<words>_           # Make <words> italic.
~<words>~           # Make <words> strikethrough.
```<words>```       # Make <words> monospace and code-like (can be multiline).
{code}<words>{code} # Make <words> monospace and code-like.
!!<space>           # Make entire message monospace. Beginning message with '!!' and then a space.
@@<space>           # Ignore all special formatting. Begin message with '@@' and then a space.
```

---

## DuckDuckGo Tips and Tricks

*What is DuckDuckGo?*
A search engine like Google, Bing, or Yahoo [but with none of the tracking](https://duckduckgo.com/about).

Search within a website, using a bang (`!`).
Go to the DuckDuckGo search bar and type:

- `!yt cute dogs` : Searches YouTube for "cute dogs"

Useful bangs:

| `bang` | **Website** |
| --- | --- |
| `!di` | Dictionary.com |
| `!t` | Thesaurus.com |
| `!w` | Wikipedia |
| `!eo` | Online Etymology Dictionary |
| `!yt` | YouTube |
| `!stack` | Stack Overflow|
| `!sopy` | Stack Overflow Python |
| `!ddso` | DuckDuckGo Stack Overflow |
| `!wa` | Wolfram Alpha |
| `!reddit` | Reddit |
| `!whitl` | Whitaker's Words: Latin to English. |
| `!whitakers` | Whitaker's Words: English to Latin. |

Pull up useful "Cheat Sheets":

- `cheat sheet Python`
- `cheat sheet bash`
- `cheat sheet C++`

  - Maybe this only works with programming languages?

Immediately pull up a map:

- `italy map`

Instant Timer and Stopwatch:

- `timer`
- `stopwatch`

Generate a QR (quick response) code for any website:

- `qr <website_url>`

### Useful Search Syntax

| Example | Result |
| ------- | ------ |
| `cats dogs` | Results about cats or dogs. |
| `"cats and dogs"` | Results for the **exact term** "cats and dogs". |
| `cats -dogs` | Fewer dogs in results. |
| `cats +dogs` | More dogs in results.  |
| `cats filetype:pdf` | PDFs about cats. Supported types:<br>  `pdf, doc(x), xls(x), ppt(x), html` |
| `dogs site:example.com` | Pages about dogs from `example.com`. |
| `cats -site:example.com` | Pages about cats **excluding** `example.com`.|
| `intitle:dogs` | Page title includes the word "dogs". |
| `inurl:cats` | Page url includes the word "cats". |

---

## Octave

Octave (Poor-Man's MATLAB)

Help at the command line:
help <function>
pwd				# prints the working directory of Octave
cd '<path>'		# change dir to <path>
ls				# list info
load('<datafile>')	# load <datafile> to current Octave session
- then you can type <datafile> to print the data to the shell
who				# shows current initialized variables
whos			# shows variables with more detail!
clear <var>		# de-initializes a variables
clear			# clear ALL variables
save <filename> <var>			# saves <var> into <filename> 
save <filename> <var>	-ascii	# saves <var> into <filename> as human-readable file

Comments: 	%
Assignment operator:	= 
Prevent output from being shown by ending line with: 	;
Exponentiation uses ^

Regular (and matrix!) math:
sqrt(A)
abs(x)
sin(x)
log(x)
log10(x)
exp(x)
[min_val, min_index]	= min(A)		# returns minimum value and index

Some variables are predefined: 	
pi
'Comma-chain' function calls:
a=1, b=2, c=3

Define an array:
A = [1, 2, 3; 4, 5, 6; 7, 8, 9; 10, 11, 12]	# ';' indicates a new row
A(2,3)							# index a matrix

Slicing:
A(:,2)	# grab all elements in each row and 2nd col only
A([1 3],:)	# grab all elements in 1st and 3rd rows
Slice a subset of a matrix:
rows = [2,5]		
cols = [2,3,4]
A(rows, cols)
v(3:end)	# grab all elements from 3rd element to last element

Indices:
[max, ind] = max(v)		# gives you the maximum element and its index in vector v
find( v < 3 )			# return the indices of the elements in v that are < 3
[r,c] = find( A >= 7)		# return the row indices (r) and column indices (c) of A elements >= 7

Append a column to a matrix:
A = [A, [10; 11; 12]]
- can do a similar process for rows

Matrix math is super easy and intuitive:
v = [1;2;3]		# vector
newvec = A * v	# matrix acting on a vector
newmatrix = A * B	# actual matrix multiplication (not element-wise!)

Creating intervals:
5:10				# make a row vector with elements 5-15 spaced by 1
0:0.5:100			# make a row vector from 0 to 100 spaced by 0.5 (so 200 elements)
linspace(6,30,5)	# make a row vector from 6 to 30 evenly spaced, with only 5 elements

Special matrices:
eye(3)		# 3x3 Identity matrix (1's along diagonal)
ones(2,4)		# matrix of all ones (2 rows, 4 cols)
zeros		# matrix of all zeros
rand(3,1)		# 3x1 matrix of uniformly distributed random numbers [0,1]
randn		# normally distributed random numbers
randi		# uniformly distributed random integers
diag(1:4)		# makes a diagonal matrix whose elements are 1-4
magic(4)		# create a 4x4 magic square

Inverse of a matrix:
pinv(A)	
- 'pseudoinverse', can still give reasonable answers even when working on singular matrices (ones without an inverse!)
inv(A)
Transpose a matrix:
A'
Flip a matrix over a horizontal axis:
flipud(A)		#'flip up-down'

Combine matrices (concatenation):
[A; B]	# vertically stack A on B

Other matrix methods:
mean(A)		# averages all the values in matrix A
sum(v)		# sums all elements in v
prod(v)		# product of all elements in v
floor(v) 		# round all elements in v down to nearest int
ceil(v)		# round all elements in v up to nearest int
length(v)		# number of elements in vector v (or larger dimension of a matrix)
[m,n] = size(A)	# stores size of matrix in m,n. m gives rows
size(A,2)			# return number of columns in A
reshape(v,3,4)		# turn vector v in into a 3x4 matrix (WARNING! Reshaping happens downward before rightward!)
reshape(v,2,[ ])	# number of cols is automatically taken care of
A(:)				# turn matrix A into col vector
max(A,[ ],2)		# find max elements in each row of A
max(A(:))			# find the absolute maximum element in A

Plotting:
plot(X,Y)			# make a line plot. X is an array of x-vals, Y is an array of y-valsf
plot(x,y, 'm--s')	# magenta, dashed line with square markers
plot(X,Y,'rx','MarkerSize',10)	# use red crosses as markers with size 10
scatter(X,Y)		# make a scatter plot
bar(X,Y, 'yellow')	# make a yellow bar graph
hist(v,50)			# make a histogram out of all the values stored in vector v with 50 bins
imagesc(A)		# make a heatmap out of A
imagesc(A), colorbar, colormap gray		# make heatmap, add a colorbar, and make grayscale
surf(X,Y,Z)		# make a 3-D surface plot
Pretty up your plots:
xlabel('<words>')
ylabel('<words>')
title('<words>')
legend('<words>')
grid			(?)
annotation	(?)

Multiple plots on same figure:
plot(<blah>)
hold on
plot(<more blah>)

Additional plot commands:
figure(2)					# create a second figure (canvas) for plotting
subplot(1,2,1)				# create a canvas with 2 axes (1x2) and access the first axes
axis([0.5 1 -2 1])			# change the axes: [<xmin> <xmax> <ymin> <ymax>]
print -dpng 'myplot.png'		# save plot as png file
clf						# clear figure
close					# closes entire plot
close all					# closes all plots

Boolean arrays:
myarr = [4,6,5,1,2]
ind = myarr > 2					# make array of indices whose elements > 2
so then: ind ==> [1,1,1,0,0]
myarr(<array of bools>)				# select only the elements of myarr of the corresponding index

Element-wise multiply/divide/exponentiate:
.*  ./  .^
v1 = [4,6,8]
v2 = [2,3,2]
v1 ./ v2  ==> gives [2,2,4]

Make a functional relationship:
x = -2:0.1:2
y = 3*x.^2 - 6*x + 4	

Some statistical methods for matrices:
std
cov
prod
sum
cumprod
median
var
corrcoef

Logical Operators:
result = 25 > & <= 20	# can directly test the truth of a statement. returns a bool
~=	# not equal to
|	# or

Control Statements:
--- if/else statements
if hours <= 1
	fee = 0;
elseif hours > 1 & hours < 7
	fee = 5*(hours-1);
else
	fee = 35;
end

--- for loop:
for k = 1:99
	balance(k+1) = (1+r)*balance(k)
end
endfor?
- can also use break and continue

--- while loop:
while <condition>
	<do stuff>;
end

Functions:
Many in-built functions:
ode45
contourc
mldivide
fminsearch	# finds a minimum of a function(???)

Make your own functions:
function <val1> = functionName(<arguments>)
	<val1> = <do stuff>
end

Return multiple values:
function [out1,out2] = functionName(<arguments>)
	if r == 1
		s = n;
	else
		s = (1-r^n)/(1-r);
	end 
end

- If you store a function in a file, the file name must match function name!
- Also you must 'cd <path/to/functiondir>'
- Add the path to function using: addpath('<path/to/functiondir>')

Make quick "anonymous" functions:
f = @(x) x^3 - 2*x + 1
Call it with f(6)

To call one function which calls another function, use a 'handle':
xmin = fminsearch(@cos,3)

Change the command prompt:
PS1('<new_prompt>')

Printing to screen:
fprintf('<words>')		# prints <words>
fprintf('words' ...
	    'and words\n')	# prints 'words and words' on the same line (tidies up code)
fprintf(' x = [%.0f %.0f], y = %.0f \n', [X(1:10,:) y(1:10,:)]')
What is the difference between fprintf and sprintf?

a = pi
disp(a)				# prints '3.1416' (instead of 'ans = 3.1416')
b = 'hi'				# can store strings in variables too
disp(sprintf('%0.2f', a))	# print a to 2 decimal places

format long			# all floats printed to 14 decimal places
format short			# all floats printed to 4 decimal places (Octave starts out in short format)

Miscellanea:
pause				# pauses current code and waits for standard input
clear; close all; clc		# good to put at beginning of script
rand_ind = randperm(10)	# make random permutation from 1 to 10
reshape
resize

## R Lang
Used to model, transform, visualize, and communicate data

Use Tidyverse

## SQL Lang (Structured Query Language):
Used to manipulate databases and extract data
RDBMS = Relational DataBase Management System

DataFrame/Spreadsheet --> Table
row --> "record"
col --> "field"

A database holds 1 or more tables.

## Neat Commenting Styles

```
Neat commenting styles:

@@@@@@@@@@@@@@@@@@@@@
@ IMPORTANT MESSAGE @
@@@@@@@@@@@@@@@@@@@@@

ccccccccccccccccccccccccc
c		message			c
ccccccccccccccccccccccccc

-*-*-*-*-* title *-*-*-*-*-

#________________________|

============
  My Title
============

// ============ Initialize Variables ============= //
// ------------ other title ------------
```

## Fortran

1.0d0	# 'd' means 'times 10^' and indicates that the number has double precision

## Overleaf

Comment multiple highlighted lines:
Cmd+/

## HTML

HTML Lang
(Used for styling pages, similar to CSS)

library(gapminder)
library(dplyr)

gapminder
Most datasets in R are data frames (spreadsheet-like objects)
- some dataframes are called tibbles
- rows are called observations
- cols are called variables

You can select only certain observations of your tibble:
filter()
gapminder %>%
  filter(year == 2007)
- The '%>%' is called a "pipe". It says you want to filter. 
You can specify multiple conditions:
filter (year == 2007, country == "United States")

New verb: arrange
- sorts a table based on a variable, in ascending order
- Useful for finding the extreme values in a dataset
gapminder %>%
  arrange(gdpPercap)
Sort in descending order:
arrange(desc(gdpPercap))
Finally, combine verbs:
filter(year == 2007) %>%
arrange(desc(gdpPercap))

New verb: mutate
- modify the values in a variable
mutate(pop = pop / 1000) 
- can also create new variables
mutate(gpd = gdpPercap * pop)
- does not permanently change the old tibble; creates a new one

## macOS Tips and Tricks

### PDFs

While using **Preview**, press `Cmd + Option + 2` to view all pages of your PDF.

- You can **drag and drop** these pages into *other* PDFs or into **other programs**, like Keynote for your presentations!
- You can also **rearrange** the pages or delete them from the PDF.

### Keyboard Shortcuts

| Function | Shortcut |
| --- | --- |
| Paste without formatting. | `Cmd + Shift + Opt + V` |
| Lock your screen. | `Cmd + Ctrl + Q` |
| Force quit an app. | `Cmd + Opt + Esc` |

Find more [here](https://support.apple.com/en-us/HT201236).

### Terminal Shortcuts

```bash
Cmd+up          # Go to last shell prompt.
Cmd+Shift+right # Go to next terminal tab.
Cmd+right       # Go to next terminal window.
```

Comment multiple highlighted lines:
Cmd+/

Equivalent to Alt: fn+Opt

### Keynote Tricks

JAKE: Turn into a table:

| Shortcut | Effect |
| --- | --- |
| Cmd+Shift+V | Insert image. |
| Cmd+Ctrl+Space | Insert special char. |
| Cmd+Opt+E | Enter LaTeX equation. |

[All Keynote LaTeX commands.](https://support.apple.com/en-us/HT202501)

\mathrm{}    # Normal font.
{\it your text here}    # Italic text
\text{}    # This may give normal font, but it is bold?

## VNC Viewer

1. Connect to an lxplus machine:
to check if any screen is open  type : screen -ls

2. Open new screen:  `screen -S screen_name`  (any name you want to give)
3. In the screen write:

```bash
k5reauth -x -f pagsh
aklog
```

Go to bash and do:

4. write: `vncserver -geometry 1368x768 :0` (screen number)

5. after getting your screen number:

```bash
k5reauth -x -f pagsh
aklog
```

- Press : `ctrl+a   d`

to go inside screen : screen -x

6. in bashrc: `alias vnc='ssh -L abcd:localhost:abcd -N -f -l your_username lxplusYYY.cern.ch'`

lxplus YYY : machine number
abcd : 4-digit number, the last number (d) -> screen number

7. Install tigervnc-viewer

1. In local terminal type : vnc
2. Open Tigervnc-viewer : ready to go

errors: vnc already open and thus showing end of stream
Solution:
ps aux | grep ssh   : will show all connection
kill -9 process_number : kill that running process if exists

Note : If the screen is closed for some reason, either the system connection timedout, you have to make a new screen and a new connection 

To kill old screen : go to the machine 
 open screen : screen -x 
 and kill screen Press : ctrl+a   k

## Good Coding Practices

