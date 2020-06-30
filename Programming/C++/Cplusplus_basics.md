# C++ Language

## Control Flow

```c++
{ statement1; statement2; ... }

if(condition) statement;

if(condition) {
    statement1;
    statement2; ...
}
else statementX;

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

Vectors:
Similar to arrays, but dynamically sized

```c++
#include <vector>
vector<type> vecName;
vecName.push_back(value);		# append value at the end of vecName
vecName[index];				# index vecName, just like arrays
vecName;					# show all entries in vecName
vecName.size();				# number of elements in vecName
```

Access last element of vector:
vecName[vecName.size()-1]

make a pointer to the array: (PROBABLY UNNECESSARY)
vector<type> * vecPtr = &vecName	# initialize pointer to point to address of vecName
*vecPtr							# 

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