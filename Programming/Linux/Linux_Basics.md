# Basics of Linux

The philosophy: **small, sharp tools**

Bash is the "**B**ourne-**a**gain **sh**ell". 
It is the standard interpreter on most Linux distributions .

## Must know Bash commands

```bash
ls     # List files. Useful flags: ls -lhtra
pwd    # Print Working Directory. Shows you where you are.
cd <path/to/files>  # Change Directory. This is how you move around.
cd ..  # Go up a dir.
cd -   # Go back to previous dir.
mv <source> <dest>  # Move or rename a file.
cp <source> <dest>  # Copy source to destination.
mkdir <newdir>  # Make newdir.
```

## Resources

- [Here's a friendly Linux Tutorial](https://ryanstutorials.net/linuxtutorial/commandline.php)
that I used to learn Linux.
- Tutorials from [Linux.com](https://www.linux.com/training-tutorials/).

## Some Bash magic

```bash
!        # This is the 'bang' operator, an iconic part of bash.
!$       # The argument of the last command. Try: `cd !$`
!!       # Execute the last command from history. Try: `sudo !!`
!cp      # Run the last `cp` command from your history.
!cat:p   # Print the last `cp` command you used to stdout, add that command to history, do not execute.
^ls^rm   # Replace `ls` in the last command with `rm`
$?    # The return value from last cmd (0=success).
history  # Check your history; displays command numbers.
!<cmd_num>  # execute command number <cmd_num>
<space>cmd # will not add 'cmd' to history!
```

### Control statements

```bash
if [[ ! -x <path/to/file> ]]; then
    <cmds>
fi

while true; do
    <cmds>
done
```

#### Useful flags

| Flag | What it do |
| ---- | ---------- |
| `! EXPRESSION` | The EXPRESSION is false. |
| `-n STRING` | The length of STRING is greater than zero. |
| `-z STRING` | The length of STRING is zero (ie it is empty). |
| `STRING1 = STRING2` | STRING1 is equal to STRING2 |
| `INTEGER1 -eq INTEGER2` | INTEGER1 is numerically equal to INTEGER2 (also: `-gt`, `-lt`)|
| `-d FILE` |  FILE is a directory. |
| `-e FILE` |  FILE exists. |
| `-r FILE` |  FILE has read permission. |
| `-s FILE` |  FILE has size greater than zero (i.e. is not empty). |
| `-w FILE` |  FILE has write permission. |
| `-x FILE` |  FILE has execute permission. |

##### Truth testing

```bash
[ "a" = "a" ]  # Tests if the 2 strings are equal. If true, exit status = 0.
```

Redirect the output and errors to log.txt:
cmd 2>&1 log.txt
Redirect the output and errors to both log.txt and the screen simultaneously:
cmd 2>&1 | tee log.txt


bash batch expansion
cp /etc/rc.conf{,-old}	# will make copy of 'rc.conf' called 'rc.conf-old'
mkdir newdir{1,2,3}		# will make newdir1, newdir2, newdir3
- it's as if the filepath "gets distributed" over the braces
- this is a good way to mv files and make backups

Difference between 'source' and 'export':
source <script.sh> 			# effectively the same as: . <script.sh>; executes script in current shell
export VAR=value			# saves value as a new environmental VAR available to child processes

computer cluster: 
folders aren’t contained on just one computer, 
but network mounts can make it look like they are

If a file path begins with / 
- this is an absolute path ("root")
- relative paths use: ./

server uses a "load balancer"
- puts each user on a variety of nodes to balance the load of resource usage

man -k <word>
- shows you the 

> is the redirection operator
| is the pipe operator

e.g.,
ls -l | grep Apr > somefile.txt
- piping the output of ls into the grep command
command-name 2> errors.txt

command1 > out.txt 2> err.txt

cmd 2>&1 | tee log.txt

scp					#
scp <source> <dest>	# the remote <source> or <dest> should be of the form: user@server:/path/to/file
scp -r 
history				# shows you all previous commands you’ve entered
more					# prints to stdout the entire file(?)
less					# prints to temporary shell, not to stdout
wc						# word count, useful flags: -l -w
sort	[-nN] [-r]			# usually sorts alphabetically, sort by number size with -n, -r is reverse search
uniq					# returns unique values 
diff <file1> <file2>		#	see the differences between <file1> and <file2>; 
						'<' indicates <file1>; '>' indicates <file2>
diff -r <dir1> <dir2>	# compares differences between all files in <dir1> and <dir2>

top -n 1 -b | grep chenguan		# see system summary and running processes; -n flag is iterations; -b is batch mode
								can grep to see a user's processes
free 	[-g]				# displays the amount of free and used memory in the system; -g to make it more readable
read [-s] [-p] [<prompt>] <var>	# stores user input into <var>; -s=silent text, -p=prompt becomes <prompt>
cut -d' ' -f2-4			# use whitespace as delimiter, and cut (print to screen) only fields (columns) 2 through 4
cat <file1> | tee [-a] <file2>		# tee will append the stdout to both a file and to stdout (it piplines the info into a 'T' shape)
ln -s <file> <link_name>	# creates a symbolic link (a reference) between <file> and <link_name>
- If you modify <link_name> then you WILL MODIFY <file>!
- Except for 'rm'; deleting <link_name> does NOT delete <file>
file <>
printf			# appears to just be a fancier and more reliable echo


Less common, but possibly helpful commands:
uname -a			# look at your Linux kernel architecture, server, etc.
uname -n			# find out what node you're on
ldd --version		# Check the glibc version.
env					# print all your environmental variables to stdout
gdb					# GNU DeBugger (not sure how this works yet)
basename <filepath> 	# strips <filepath> of directory part of name and suffix
- basename /usr/bin/sort 		# returns: 'sort'
- basename include/stdio.h .h	# returns: stdio
date					# prints the date
whoami      # Prints your username.

cat /etc/*-release    # Find out what distribution of Linux you're running


Timestamp things:
date +%F-%T	# gives 2019-07-17-20:10:16

Less important but still really cool commands!
say [-v] [name] "<phrase>"		# 
write	 <user>					# start a chat with <user> on your server
    - You are immediately put into "write mode". Now you can send messages back and forth.
    - Press 'Ctrl+C' or 'Esc' to exit write mode.
mesg [y|n]					# allow [y] people to send you messages using 'write' or not [n]
Command line language translator:
https://www.ostechnix.com/use-google-translate-commandline-linux/

Defining Functions:
function <func_name> {
	<cmd1>;
	<cmd2>; ...
}

Can be one liners:
function cdl { cd $1; ls; }
	cdl mydir		# cd into mydir and then ls
____________________
grep (global regular expression print)
grep   <string>   <files_to_be_searched>

grep -E -r "*<word>*" ./* 	# search the contents of every file for *<word>*, recursively starting from ./*
- equivalent to doing: egrep

rsync <file> <destination>
#rsync -av <file> <destination>

ps aux | grep <task>		# see active processes

____________________
GNU screen! (a terminal multiplexer)
- Start a persistent remote terminal
- That way, you won't lose your work if you get disconnected
- After making a new screen, you should do: `source ~/.bash_profile` to get your normal settings
screen -S <screen_name>	# start a bash environment session ("screen")
ctrl+a, then Esc			# enters "copy/scrollback mode", which lets you scroll! 
- navigate copy mode using Vim commands!
- Hit `Enter` to highlight text. Hit `Enter` again to copy it. Paste with Ctrl+a, then `]`
- Hit `q` or `Esc` to exit copy mode.
ctrl+a, then d				# detach from the session (remember though that it's still active!)
screen -ls				# see what sessions are active
screen -r <name>			# reattach to active session (instead of <name> can also use: <screen_pid>)
exit						# terminate session
kill <screen_pid>			# kill frozen screen session
ctrl+a then s				# split screens horizontally
ctrl+a then v				# split screens vertically
ctrl+a then Tab			# switch between split screen regions
ctrl+a then c				# begins a virtual window in a blank screen session
ctrl+a then "				# see list of all active windows inside session

tmux (terminal multiplexer)
Nice for splitting the terminal into multiple screens.
All commands start with: 	Ctrl+b
Tmux reads from your config file: ~/.tmux.conf
# Shell commands:
tmux							# Start a new session.
tmux kill-session -t <name>		# Kill session <name>.
tmux new -s <name>				# Name the tmux session.
tmux ls							# List all running sessions.
tmux attach-session -t <name>	# Reattach to session <name>.
# Inside tmux commands:
Ctrl+b, ?			# Show all commands.
Ctrl+b, d			# Detach from session.
Ctrl+b, c			# Create a new window, with a shell.
Ctrl+b, w			# Choose window from a list.
Ctrl+b, 2			# Switch to window number 2.
Ctrl+b, ,			# Rename the current window. 
Ctrl+b, %			# Split current pane vertically.
Ctrl+b, "			# Split current pane horizontally.
Ctrl+b, o			# Go to next pane.
Ctrl+b, ;			# Toggle between panes.
Ctrl+b, {			# Move current pane left.
Ctrl+b, }			# Move current pane right.
Ctrl+b, x			# Close current pane.
exit				# Permanently close the session.

____________________

wget <url>	# download whatever url from the web
wget -r --no-parent -A.pdf http://tier2.ihepa.ufl.edu/~rosedj1/DarkZ/MG5vsJHUGen_bestkinematics_GENlevel_WITHfidcuts/
- Downloads recursively, without looking at parent directories, and globbing all .pdf

tar -cf <tarball> foo bar				# create <tarball> using files foo and bar
tar -xf <tarball>					# unzip all of <tarball>
tar -xvf <tarball> <file1> <file2>		# untar specific files from tarball
- x=extract, v=verbose, f=file, 

Memory usage
du 				# "disk usage"; good for find which files or dirs are taking up the most space
du -h <dir>		# print size of <dir> in human-readable format 
du -sh ./			# sums up the total of current workspace and all subdirs

df -h				# "disk filesystem", shows usage of memory on entire filesystem 

```bash
find
find ./ -name "*plots*"								# find all files with name plots in this dir and subsequent dir
find /<path> -mtime +180 -size +1G					# find files with mod times >180 days and size>1GB
find . -type d -exec touch '{}/__init__.py' \;				# create (touch) a __init__.py file in every dir and subsequent dir
find . -type f -printf '%s\t%p\n' | sort -nr | head -n 30		# find the 30 biggest files in your working area, sorted 
find . -type f -printf '%T@ %p\n' | sort -n | tail -20 | cut -f2- -d" "		# find the 20 most recently modified files
find . -name "*.css" -exec sed -i -r 's/MASS/mass/g' {} \;	# use sed on every found file (the {} indicates a found file)
find ~/src/ -newer main.css							# find files newer than main.css

locate
locate -i <file_to_be_found>		# searches computer's database. -i flag means case insensitive
```

Copy multiple files from remote server to local:
scp <username>@<host>:/path/to/files/\{file1, file2, file3\} .

Mount a remote disk on your local system:
sshfs <UN@remote_host> <local/dir>
Unmount when finished:
umount <local/dir>

***Learn more about these commands:
rcp
set
set -e 			# exit on first error?
set -u 			# catch unset variables?

Use a specific interpreter to execute a file:
#!/usr/bin/env python

Environment variables can be modified using 'export':
export VARIABLE=value
export PYTHONPATH=${PYTHONPATH}:</path/to/modules>	# appending ':</path/to/modules>' to PYTHONPATH env var
Interesting env vars:
SHELL			# hopefully bash
HOSTNAME		# host
SCRAM_ARCH		# cmssw architecture
USER			# You!
PWD				# current working dir
PS1				# bash prompt
LS_COLORS		# colors you see when you do 'ls'
MAIL
EDITOR

Customize your prompt (you can even add a command to be executed INSIDE the prompt):
PS1="[\d \t] `uptime` \u@\h\n\w\$ "

Prompt settings:
* A bell character: \a
* The date, in “Weekday Month Date” format (e.g., “Tue May 26”): \d
* The format is passed to strftime(3) and the result is inserted into the prompt string; an empty format results in a locale-specific time representation. The braces are required: \D{format}
* An escape character: \e
* The hostname, up to the first ‘.’: \h
* The hostname: \H
* The number of jobs currently managed by the shell: \j
* The basename of the shell’s terminal device name: \l
* A newline: \n
* A carriage return: \r
* The name of the shell, the basename of $0 (the portion following the final slash): \s
* The time, in 24-hour HH:MM:SS format: \t
* The time, in 12-hour HH:MM:SS format: \T
* The time, in 12-hour am/pm format: \@
* The time, in 24-hour HH:MM format: \A
* The username of the current user: \u
* The version of Bash (e.g., 2.00): \v
* The release of Bash, version + patchlevel (e.g., 2.00.0): \V
* The current working directory, with $HOME abbreviated with a tilde (uses the $PROMPT_DIRTRIM variable): \w
* The basename of $PWD, with $HOME abbreviated with a tilde: \W
* The history number of this command: \!
* The command number of this command: \#
* If the effective uid is 0, #, otherwise $: \$
* The character whose ASCII code is the octal value nnn: \nnn
* A backslash: \\
* Begin a sequence of non-printing characters. This could be used to embed a terminal control sequence into the prompt: \[
* End a sequence of non-printing characters: \]
FINISH GETTING THE REST OF THESE PROMPT SETTINGS! 
e.g. colors


open plots while ssh'ed:
display 
eog <png>		# quickly open png files

sleep 7			# make the shell sleep for 7 seconds

### Sexy Bash Tricks

Quickly rename a bunch of files in a dir:

```bash
for file in *.pdf;
    do mv "$file" "${file/.pdf/_standardsel.pdf}";  # ${file/replace_this/with_this}
done
```

Make a bunch of dir's quickly:
mkdir newdir{1..20}							# make newdir1, newdir2, ..., newdir20

iterate over floats:
for k in $(seq 0 0.2 1); do echo "$k"; done		# seq <start> <interval> <stop>
- seq has all kinds of flags for formatting!

Check if a dir exists. If it doesn't, then make it:
[ -d possibledir ] || mkdir possibledir
- The LHS checks if the directory is there. If it is, bash returns 1 and the OR statement ('||') is satisfied. Else, mkdir

Timestamp things:
function timestampit { date +"%y%m%d_%H%M%S"; }	

Terminal Shortcuts:
Ctrl-A			# quickly go to BEGINNING of line in terminal
Ctrl-E			# quickly go to END of line in terminal
Ctrl-W			# delete whole WORD behind cursor
Ctrl-U			# delete whole LINE BEHIND cursor
Ctrl-K			# delete whole LINE AFTER cursorCtrl-R, then <cmd>	# reverse-search your command history for <cmd>
Option-Left		# move quickly to the next word to the left
Cmd-Right		# switch between terminal WINDOWS
Cmd-Shift-Right	# switch between terminal TABS within window

alias				# check your aliases
alias <newalias>="<command>"	# add <newalias> to 

time ./<script.sh>	# time how long a script takes to run
- this will send three times to stdout: real, user, sys (real = actual run time)

Background Jobs:
<cmd> &			# runs <cmd> in a background subshell
fg				# bring a background process to foreground
jobs				# see list of all background processes
Ctrl+Z			# pause current job and return to shell
Ctrl+S			# pause a job, but DON'T return to shell
Ctrl+Q			# resume paused job in foreground
bg				# resume current job in background
(sleep 3 && echo 'I just woke up') >/tmp/output.txt &		# group commands and redirect stdout!
- here the '&&' means to do the second command ONLY IF the first command was successful

Learn more about nohup:
nohup ./gridpack_generation_patched06032014.sh tt 1nd > tt.log &




.bash_profile is executed for login shells, while .bashrc is executed for interactive non-login shells.

Execute shell script in current shell, instead of forking into a subshell:
. ./<script.sh>			# note: dot space dot forward-slash
- N.B. this is nearly the same as doing: source <script.sh>

watch -n 10 '<cmd>'	# repeats <cmd> every 10 seconds
- default is 2 seconds

##########################
sed 	# stream editor
echo "1e-2" | sed "s#^+*[^e]#&.000000#;s#.*e-#&0#"		# makes 1e-2 become 1.000000e-02
			sed "s#^[0-9]*[^e]#&.000000#;s#.*e-#&0#"		# equivalently

sed, in place, on a Mac:
sed -i '' -e "s|STORAGESITE|${storageSiteGEN}|g" DELETEFILE.txt 

Strip python/bash comments from a file:
sed -i -e   's/#.*$//g'  -e   '/^$/d'  <file>		# the '-e' executes another instance of sed, like piping. '-i' is "in place" so it modifies <file>
____________________
Check to see if some command succeeded:
(N.B. a command returns 0 if it succeeds!)
some_command
if [ $? -eq 0 ]; then
    echo OK
else
    echo FAIL
fi

awk
An extremely powerful file-processing language

General format:
awk 'BEGIN{begincmds} {cmd_applied_to_each_line} END{endcmds}' <file>

Sum up the second column in a file, and specifying the delimiter of columns as a comma:
awk -F','  '{sum+=$2} END{print sum}' bigfiles.txt 



Study this code below and see if syntax is useful:
# if rnum allows, multiply by 10 to avoid multiple runs                                                      
# with the same seed across the workflow                                                                     
run_random_start=$(($rnum*10))                                                                               
# otherwise don't change the seed and increase number of events as 10000 if n_evt<50000 or n_evt/9 otherwise 
if [  $run_random_start -gt "89999990" ]; then                                                               
    run_random_start=$rnum                                                                                   
    max_events_per_iteration=$(( $nevt > 10000*9 ? ($nevt / 9) + ($nevt % 9 > 0) : 10000 ))                  
fi                                                                                                           



You can "divide out" strings:
MG="MG5_aMC_v2.6.0.tar.gz"
MG_EXT=".tar.gz"
echo ${MG%$MG_EXT}
- Prints: MG5_aMC_v2.6.0		# so effectively MG has been "divided by" MG_EXT


Need to learn about:
tr "." "_"			# translates all "." chars into "_" (used with piping)
perl -ne 'print if /pattern1/ xor /pattern2/'

What does this do?
model=HAHM_variablesw_v3_UFO.tar.gz
if [[ $model = *[!\ ]* ]]; then...

Bash Scripting
$# 		# number of arguments passed to script
$@		# the arguments themselves which were passed to script
$?		# return statement of last command: 0 is successful