# Basics of Bash

The philosophy of Unix: **small, sharp tools**

MUST KNOW Bash commands:

ls					# list most contents in current directory
ls -a					# list all contents (including hidden files) in current dir
ls -l 					# list contents in a long format (just more detailed way)
pwd
cd <path/to/files>
cd ..
cd -					# go back to previous dir
cp <source> <dest>
mkdir <newdir>


Here's a [Linux Tutorial](https://ryanstutorials.net/linuxtutorial/commandline.php).

Some Bash magic:

!    # this is the 'bang' operator, an iconic part of bash
!!    # execute the last command from history
!$    # means the argument of the last command
cd !$    # cd's into the last command's argument; e.g.
!cat    # run the last cat command from your history that used cat
!cat:p    # print the last cat command you used to stdout; also adds that command to your history
^ls^rm			# if the last command used 'ls', it copies the command, replaces 
sudo !!			# run last command with sudo privileges
history			# check your history; displays command numbers
!<cmd_num>		# execute command number <cmd_num>
it with 'rm' and executes the new command
<space> command # will not add 'command' to history!

Redirect the output and errors to log.txt:
cmd 2>&1 log.txt
Redirect the output and errors to both log.txt and the screen simultaneously:
cmd 2>&1 | tee log.txt