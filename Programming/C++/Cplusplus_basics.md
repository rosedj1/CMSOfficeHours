# C++ Language

## Resources

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

## Control Flow

```c++
{ statement1; statement2; ... }

if(condition) statement;

if (condition) {
    statement1;
    statement2; ...
} else if {
    statementX;
}

while(condition) statement;  // May not execute statement.

do statement while(condition);  // Used for executing statement at least once.

for(init_expr; cont_expr; incr_expr) statement;

break;

continue;
```

## Derived Types

[Basic c++ types found here.](https://www.tutorialspoint.com/cplusplus/cpp_data_types.htm)

For every type, there are some _derived types_: reference, pointer and array types:

- **variable** : an association between a name and an object.
- **reference** : an alias for an object.
- **pointer** : an object that refers to another object.
- **array** : a linear sequence of objects of the same type

## A Simple C++ Script

```c++
#include <iostream>
 
int main()
{
    std::cout << "Hello, world!";
    return 0;
}
```

C++ files usually have one of these extensions: 
.cpp, .cxx, .C, .cc
Use the GNU compiler (g++) to compile your C++ script:
g++ <c++_script>.cpp -o <name_of_new_executable>

To determine size of a C++ array:
int myarr[] = {4, 6, 8, 9};
sizeof(myarr)/sizeof(*myarr)
VECTORS ARE BETTER THAN ARRAYS! # more flexibility!

### Vectors

Similar to arrays, but dynamically sized.

```cpp
#include <vector>
vector<int> vec;   // Doesn't have to be `int`; could be any type.
vec.push_back(2);  // Append 2 at the end of vec.
vec[0];            // Index vec, just like arrays. Returns `2`.
vec;               // Show all entries in vec.
vec.size();        // Number of elements in vec.
vec.begin();       // Return an iterator.
// Sort a vector:
vector<double> vec = {2.0, 1.0}
std::sort(vec.begin(), vec.end())  // After: { 1.0000000, 2.0000000 }
```

#### Other ways to play wth vectors

Access last element of vector: `vec[vec.size()-1]`

Make a pointer to the array (...but the vector *is* a pointer...):
```cpp
vector<type> * vecPtr = &vec  // Initialize pointer to point to address of vec.
*vecPtr                       // Return the 
```

std::vector<int> *lep_ecalDriven;
if (lep_ecalDriven->size() > 0) {
               lep1 = (*lep_ecalDriven)[L1];
               lep2 = (*lep_ecalDriven)[L2];
               }

Good way to slice a pointer vector?
std::vector<int> *lep_id;
unsigned int L1 = passLepIndex[0];
unsigned int L2 = passLepIndex[1];
int idL1 = (*lep_id)[L1];
int idL2 = (*lep_id)[L2];

## Other Notes

### Casting: turn one data type into another

```cpp
Double_t n_bins = round((m4mu_max - m4mu_min) / bin_width);
Int_t n_bins_in_fitrange = static_cast<Int_t>(n_bins);  // Cast to an Int_t.
```

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