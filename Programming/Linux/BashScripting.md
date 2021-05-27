# Bash Scripting

You can put many Bash commands together into a script.
Thus, Bash is like other programming languages (Python, Java, C++, etc.).

[Arrays](https://www.tutorialkart.com/bash-shell-scripting/bash-array/)

## Control Flow

```bash
############################
#--- if/then statements ---#
############################
FILE=/home/jake/myfile.txt
if test -f "${FILE}"; then  # -f checks if it's an actual file (versus a dir).
    echo "${FILE} exists."
fi

# Another example:
if [ ! -e "${FILE}" ]; then  # Can also use double square brackets.
    echo "${FILE} does not exist."
else
    echo "You betcha, don'tcha know."
fi

# You can be really fancy:
test -f /etc/resolv.con && echo "$FILE exists." || echo "$FILE doesn't exist."
# The part after the `&&` executes if true, `||` executes if false.

###################
#--- for loops ---#
###################
# for loops:
for num in {15..60..5}; do  # Start from 15, end at 60, increment by 5.
    echo $num;
done

#####################
#--- while loops ---#
#####################
while true; do
    <cmds>
done
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

### Useful flags

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

### Truth testing

```bash
[ "a" = "a" ]  # Tests if the 2 strings are equal. If true, exit status = 0.
```

### Helpful bash variables

```bash
$#  # number of arguments passed to script
$@  # the arguments themselves which were passed to script
$?  # return statement of last command: 0 is successful (usually).
```
