# VIM: Vi IMproved

Vim is a powerful, ubiquitous text editor found on nearly every Linux machine.
You can make macros, edit multiple files at once, and so much more with this tiny program.

## Getting started

vim <file1>		# open <file1> in Vim

Command Mode:
You start Vim in Command Mode

```bash
Esc     # return to Command Mode
:q(!)   # (force) quit Vim; return to your shell
i       # puts you in Insert Mode; let's you type regularly
Ctrl+V  # puts you in Visual Block Mode
I (A)   # moves cursor to beginning (end) of line, then puts you in Insert Mode [capital 'i']
:w      # write to file (save)
:wq     # write, then quit
```

Movement in Command Mode:
h,j,k,l	# move cursor: left, down, up, right
W,w		
E,e
B,b
%		# brace match; i.e. if cursor is on '{', then jumps to corresponding '}'
$
^
0
f
t
gg,G		# go to top (bottom) of page
ge
* (#)		# search for word under cursor forwards (backwards)
Deletions:
d
c
s
r

Blocks:
a
i

>		
<
Ex:  >i{		# indent '>' all text inside '{' block

# =============================
SUBSTITUTIONS:
:%s/thisword/thatword/g		# search for thisword and substitute in thatword, globally
:s/ <\thisword\> / thatword/	# replace thisword (exactly matching), with thatword
# =============================
MARKS:
m<char>		# set a mark (checkpoint) wherever the cursor is. This is mark <char>
`<char>		# recall to mark <char>
'<char>		# recall to mark <char>, at beginning of line
:marks		# look at all your marks

Tips:
y'<char>		# yank all text from current cursor position to mark <char>
lower case registers are local marks
UPPER case registers are GLOBAL marks (these allow you to easily move between different files)

### Folds

Collapse your functions for readability.

```bash
zf<movement>      # folds whatever lines the cursor touches during <movement>
za                # opens the fold if closed; closes the fold if open
zo                # opens fold
zc                # closes fold
:<num1>,<num2>fo  # fold code from line <num1> to line <num2>
```

Add this to .vimrc if you want to save folds:
autocmd BufWinLeave *.* mkview
autocmd BufWinEnter *.* silent loadview

### TABS

Put code into different tabs to stay organized.
:tabedit <file1>		# opens <file1> in new tab
gt (gT)				# go to next (previous) tab
3gt					# go to 3rd tab
:tabfirst(last)			# go to first (last) tab
:tabclose				# close current tab
:tabonly				# close all other tabs except this one
:tabs				# see all open tabs
vim -p <file1> <file2>	# open <file1> <file2> in different tabs

# =============================
SESSIONS:
Vim can also save and restore tab sessions!
:mksession <allmytabs.vim>		# stores current session of tabs in <allmytabs.vim> file
vim -S <allmytabs.vim>			# open the session called <allmytabs.vim>
:source <allmytabs.vim>			# open <allmytabs.vim> from command/normal mode
:mks!						# overwrite session with tabs currently open


# =============================
MACROS:
q<char>		# begins "recording" your commands; stores them in register <char>
@<char>		# replay macro stored in register <char>


# =============================
Window Splitting:
:split <file2>		# split window horizontally and load <file2>
:vsplit <file2> 		# split window vertically and load <file2>
Ctrl+W, uparrow	# move cursor up one window
Ctrl+W, Ctrl+W	# move cursor to next window (cycle)
Ctrl+W |			# maximize window horizontally
Ctrl+W _			# maximize window vertically
Ctrl+W = 			# make all windows equal size
Ctrl+W [N] +		# increase window height by N
Ctrl+W [N] -		# decrease window height by N
Ctrl+W [N] >		# increase window width by N
Ctrl+W [N] <		# decrease window width by N
:close			# close current window (but :q should work too)

Native file explorer:
:Explore (:Ex)	# open file explorer (short-hand)
:Sexplore		# horizontal split
:Vexplore		# vertical split
:Vexplore!		# vertical split, with file explorer on right side instead of left
:Texplore		# open explorer in another tab

# =============================
Cute Tricks
:112,168norm! <consecutive_cmds>	# execute <consecutive_cmds> between L112-168 as if in normal mode
- Example:   :10,16norm! c3E"New text I want to enter"
- If you need to enter an Esc character while typing this command, hit Ctrl+V
- similar to executing a macro, but doesn't take up a register, and has flexibility!
Powerful:
:24,48norm!@k	# apply macro stored in reg k to lines 24-48

The '=' means equalize all lines (indent):
=i{		# autoindents code which is inside a block of '{'

Autocomplete in Insert Mode:
Ctrl+N

Modify a file on a remote server:
vim scp://remoteuser@remote_IP_or_hostname/relative/path/of/file


Consider using Vim-LaTeX!
http://vim-latex.sourceforge.net/index.php?subject=download&title=Download

Read another file into your current file:

```bash
:r /path/to/file
:r !head -55 /path/to/file       # Read in the first 55 lines:
:r !sed -n 10,15p /path/to/file  # Read in only lines 10-15:
:put =readfile('/path/to/file')[10:15]  # Another way to read in lines.
```
