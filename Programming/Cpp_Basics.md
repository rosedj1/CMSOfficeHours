# C++ Language

## A Simple C++ Script

```c++
// This code is contained in a file called: helloworld.C
// C++ scripts usually have one of these extensions: `.cpp, .cxx, .C, .cc`

#include <iostream>
 
int main()
{
    std::cout << "Hello, world!" << std::endl;
    return 0;
}
```

Compile your C++ script using the **GNU compiler** (`g++`):

```bash
g++ helloworld.C -o helloworld.exe
```

In your terminal, you can run the compiled code within the **executable**:

```bash
./helloworld.exe
# Prints: Hello, world!
```

## Printing Output

There are two main ways to print to the screen:

1. `cout`
2. `printf`

```cpp
cout << "How many words to print? " << words_tot << endl;

// `printf` allows you to use 'format specifiers' ('%' formats the output).
printf("Dad is %d years old.\n", 65);
// More examples.
printf("%s \n", "A string");
printf("Chars: %c %c \n", 'a', 65);
printf("Decimals: %d %ld \n", 1977, 650000L);
printf("Pad left with blanks: %4d \n", 123);  // 'Pad left with blanks:  123'
printf("Pad left with zeros: %06d \n", 123);  // 'Pad left with zeros: 000123'
printf("Some different radices: %d %x %o %#x %#o \n", 100, 100, 100, 100, 100);
printf("floats: %4.2f %+.0e %E \n", 3.1416, 3.1416, 3.1416);
// 'floats: 3.14 +3e+00 3.141600E+00'
printf("Width trick: %*d\n", 5, 10);  // 'Width trick:    10'
```

<!-- ### Specifiers
https://www.cplusplus.com/reference/cstdio/printf/
	specifiers
length	d i	u o x X	f F e E g G a A	c	s	p	n
(none)	int	unsigned int	double	int	char*	void*	int*
hh	signed char	unsigned char					signed char*
h	short int	unsigned short int					short int*
l	long int	unsigned long int		wint_t	wchar_t*		long int*
ll	long long int	unsigned long long int					long long int*
j	intmax_t	uintmax_t					intmax_t*
z	size_t	size_t					size_t*
t	ptrdiff_t	ptrdiff_t					ptrdiff_t*
L			long double				 -->

## Arrays

```cpp
// Initialize array of ints:
int myarr[] = {4, 6, 8, 9};
// Determine size of a C++ array:
int arr_len = sizeof(myarr)/sizeof(*myarr);
// VECTORS ARE BETTER THAN ARRAYS! # more flexibility!
```

## Vectors

Similar to arrays, but dynamically sized.

```cpp
#include <vector>

vector<int> vec(3);        // Looks like: { 0, 0, 0 }
vector<double> my_vector;  // Instantiates an empty vector.

// Some vector methods:
vec.push_back(2);  // Append 2 at the end of vec.
vec[0];            // Index vec, just like arrays. Returns `2`.
vec;               // Show all entries in vec.
vec.size();        // Number of elements in vec.
vec.begin();       // Return an iterator.

// Sort a vector:
vector<double> vec = {2.0, 1.0}
std::sort(vec.begin(), vec.end())  // After: { 1.0000000, 2.0000000 }
```

### Iterate over a vector

```cpp
vector<int> nums = {1, 2, 3};
for (auto & num : nums) {
    cout << num << " squared = " << num * num << endl;
}
```

### Other ways to play with vectors

Access last element of vector: `vec[vec.size()-1]`

Make a pointer to the vector (...but the vector *is* a pointer...):

```cpp
vector<type> * vecPtr = &vec  // Initialize pointer to point to address of vec.
*vecPtr                       // Return the 

std::vector<int> *lep_ecalDriven;
if (lep_ecalDriven->size() > 0) {
               lep1 = (*lep_ecalDriven)[L1];
               lep2 = (*lep_ecalDriven)[L2];
               }

// Good way to slice a pointer vector?
std::vector<int> *lep_id;
unsigned int L1 = passLepIndex[0];
unsigned int L2 = passLepIndex[1];
int idL1 = (*lep_id)[L1];
int idL2 = (*lep_id)[L2];
```

## Sets

```cpp
TString runlumievent = "xyz";
std::set<TString> runlumieventSet;
if (runlumieventSet.find(runlumievent)==runlumieventSet.end()) {
    // I think this means that the set could NOT find runlumievent in the set
    // (because the iterator got to the end).
    runlumieventSet.insert(runlumievent);
}
```

## Control Flow

```c++
{ statement1; statement2; ... }

//--- If/then conditionals: ---//
if(condition) statement;

if (condition) {
    statement1;
    statement2; ...
} else if {
    statementX;
}
//--------------------------------------------------------------------------//

// While loops:
while(condition) statement;  // May not execute statement.

do statement while(condition);  // Used for executing statement at least once.
//--------------------------------------------------------------------------//

// For loops:
for(init_expr; cont_expr; incr_expr) statement;

break;

continue;
//--------------------------------------------------------------------------//
```

## Docstrings

[Comment your code using Doxygen](https://en.wikipedia.org/wiki/Doxygen#Example_code). Like this:

```cpp
/**
 * @file
 * @author  John Doe <jdoe@example.com>
 * @version 1.0
 *
 * @section LICENSE
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; either version 2 of
 * the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * General Public License for more details at
 * https://www.gnu.org/copyleft/gpl.html
 *
 * @section DESCRIPTION
 *
 * The time class represents a moment of time.
 */

class Time {

    public:

       /**
        * Constructor that sets the time to a given value.
        *
        * @param timemillis is a number of milliseconds
        *        passed since Jan 1, 1970.
        */
       Time (int timemillis) {
           // the code
       }

       /**
        * Get the current time.
        *
        * @return A time object set to the current time.
        */
       static Time now () {
           // the code
       }
};
```

## Derived Types

[Basic c++ types found here.](https://www.tutorialspoint.com/cplusplus/cpp_data_types.htm)

For every type, there are some _derived types_:
reference, pointer, and array types:

| **Derived Type** | ***What is it?*** |
|---|---|
| variable | An association between a name and an object. |
| reference | An alias for an object. |
| pointer | An object that refers to another object. |
| array | A linear sequence of objects of the same type |

### Keywords

| **Keyword** | ***Means what?*** |
|---|---|
| `static` | The value is shared between all instances of the class. |
| `const` | The value doesn't change. |

## Other Notes

### Enumeration

Use `enum` to assign names to `int`s:

```cpp
enum Animal {
    // If you do not initialize an enumerator, it starts at 0.
    Animal_Alpaca = -9,  // Assigned value is -9.
    Animal_Tiger,        // Assigned value is -8.
    Animal_Lion,         // Assigned value is -7.
    Animal_Kangaroo = 5, // Assigned value is 5.
    Animal_Zebra,        // Assigned value is 6.
} ;
```

This increases the readability and efficiency of your code.

### Casting

Casting turns one data type into another:

```cpp
Double_t n_bins = round((m4mu_max - m4mu_min) / bin_width);
Int_t n_bins_in_fitrange = static_cast<Int_t>(n_bins);  // Cast to an Int_t.
```

## Unorganized Stuff Below

A header file (file that has extension `.h`) simply defines functions.
Header files are placed at the beginning of the script to let your script know
which functions exist:

```c++
#include "TFile.h"
#include "TMath.h"
#include <TTreeReader.h>
#include <iostream>
```

Difference between quotes vs. angled brackets:

- angled brackets : header file that **comes with the compiler**
- double quotes : header file that is **user-defined**
- [Learn more about header files here.](https://www.learncpp.com/cpp-tutorial/header-files/)

Standard library header files:

- `<iostream>`

## Make Files and `make`

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
