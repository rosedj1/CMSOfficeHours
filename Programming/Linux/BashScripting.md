# Bash Scripting

You can string together many Bash commands into a script.
Thus, Bash is like other programming languages (Python, Java, C++, etc.).

[Arrays](https://www.tutorialkart.com/bash-shell-scripting/bash-array/)

## For loops

```bash
for num in {15..60..5};  # Start from 15, end at 60, increment by 5.
    do echo $num;
done
```

```bash
$#  # number of arguments passed to script
$@  # the arguments themselves which were passed to script
$?  # return statement of last command: 0 is successful
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

## If/then statements

```bash
if [[ ! -x <path/to/file> ]]; then
    <cmds>
fi

while true; do
    <cmds>
done
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
