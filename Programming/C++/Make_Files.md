## `make` (<-- does this show markdown?) and Make Files

Requires a file called either "makefile" or "Makefile"
Put this inside:
say_hello:
        echo "Hello World"
Write, quit, and then use the command: `make`
The output will be:
echo "Hello World"
Hello World

Here, the echo command is called the recipe.
The function name "say_hello" is called the target.
The entire function, with its recipe and prerequisites, is called a rule.

You can suppress some of the output by putting '@' in front of the recipe.
say_hello:
        @echo "Hello World"

This is an example of a phony target (function) since "say_hello" is not a file. 

By default, make will only call the first target in the makefile.
This is called the default goal.
If you want to call other targets, put:
all: say_hello <other_targets>

say_hello:
        @echo "Hello World"

generate:
        @echo "Creating empty text files..."
        touch file-{1..10}.txt

clean:
        @echo "Cleaning up..."
        rm *.txt

You can define variables just like in Bash: