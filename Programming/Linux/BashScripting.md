# Bash Scripting

You can put many Bash commands together into a script.
Thus, Bash is like other programming languages (Python, Java, C++, etc.).

## Control Flow

```bash
############################
#--- if/then statements ---#
############################
FILE=/home/jake/myfile.txt
if test -f "${FILE}"; then  # -f checks if it's an actual file (versus a dir).
    echo "${FILE} exists."
fi

# One liner:
if cond; then cmd1; else cmd2; fi

# See if previous command succeeded (`returns 0`):
<some_command>
if [ $? -eq 0 ]; then
    echo "Command succeeded"
else
    echo "FAILED"
fi

# Another example:
if [ ! -e "${myfile}" ]; then  # Can also use double square brackets.
    echo "File does not exist."
elif [ -s "${myfile}" ]; then
    echo "File exists and is not empty."
else
    echo "This should never be printed."
fi

# Yet another example:
overwrite=true
if [ ! -e "myfile.txt" ] || test overwrite; then
    echo -n > "myfile.txt"
fi

(sleep 3 && echo 'I just woke up') >/tmp/output.txt &  # group commands and redirect stdout!

# Get fancy: if cmd1 is true, then cmd2 executes, otherwise cmd3.
cmd1 && cmd2 || cmd3
# E.g.
test -f /etc/resolv.con && echo "$FILE exists." || echo "$FILE doesn't exist."

###################
#--- for loops ---#
###################
# for loops:
for num in {15..60..5}; do  # Start from 15, end at 60, increment by 5.
    echo $num;
done

#############################
#--- Looping over arrays ---#
#############################
# Method 1:
directories="firstone/ secondone/ thirdone/"
for d in $directories; do
    echo $d
done

# Method 2:
files=( file1.txt )
files+=( file2.txt )
files+=( file3.txt )
for f in "${files[@]}"; do
    echo $f
done

# Method 3:
distro=("redhat" "debian" "gentoo")
## Get length of $distro array.
len=${#distro[@]}  # Can also use `*` instead of `@`.
## Use bash for loop.
for (( i=0; i<$len; i++ )); do
    echo "${distro[$i]}"
done

#####################
#--- while loops ---#
#####################
num=5
while [ $num -lt 10 ]; do
    # `lt` means "less than".
    # You also have: `gt`, `ge`, `eq`, `ne`
    # Increment num by 1 using "arithmetic expansion".
    (( num = num + 1 ))
    # Other ways to increment:
    # ((num++))
    # ((++num))
    # let "num+=1" 
    # let "num++"
    # let "++num"
done

#########################
#--- case statements ---#
#########################
b=4; c=8; d=9
case "$b" in
 5) a=$c ;; # If b is 5, then a=8.
 6) a=1 ;;  # If b is 6, then a=1.
 *) a=$d ;; # Otherwise, a=9.
esac
```

### Useful flags for truth testing

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

```bash
[ "a" = "a" ]  # Tests if the 2 strings are equal. If true, exit status = 0.
```

## Functions

```bash
function <func_name> {
    <cmd1>;
    <cmd2>;
    ...
}

# Functions can be one liners:
function cdl { cd $1; ls; }
    cdl mydir  # cd into mydir and then ls
```

### Helpful bash variables

```bash
$#  # number of arguments passed to script
$@  # Positional parameters passed to script as separate words: $1, $2, etc.
$*  # Positional parameters passed to script as ONE word (whitespace->IFS).
$?  # return statement of last command: 0 is successful (usually).
```

## Learn More About

[Powerful shell parameter expansion](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Shell-Parameter-Expansion)

[Arrays](https://www.tutorialkart.com/bash-shell-scripting/bash-array/)

[Bash's control flow](https://stackoverflow.com/questions/19670061/bash-if-false-returns-true-instead-of-false-why)

In Bash, a command will return an integer result
(typically `0` on success and `1` on failure).
Bash's `if` statement uses the *result from a command* to decide how to proceed:

if true; then

(`true` is a command! Weird, I know.)
