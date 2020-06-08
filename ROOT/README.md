# A Conversation with ROOT

## The ROOT of all ~Evil~ High-Energy Physics Data Analysis

Boot up the ROOT interpreter:
```bash
root -l
```

```c++
// Common variables types:
int

TString

// How to use these variables:
int some_num = 5;
TString some_str = "Text goes here";
some_str.Data();  // Returns "Text goes here".

// Print to the screen.
std::cout << "Hi there. This is text from this script." << std::endl;

// Vectors (arrays).
std::vector<int> vec;
vec.push_back(4);  // Add an element with value 4 to this vector. 
vec[0];            // Return the value of the 0th element (4). 
vec.at(0)          // Another way to access the 0th element.
vec.clear()        // Empty the vector.
vec.size()         // Return the number of elements in vec.

std::vector<TString> years;  // Make a vector of TStrings.
years.push_back("2020");
years.push_back("2021");

TString formatted_txt;
formatted_txt = Form("This is the year: %s", years.at(1))


// for loops
for(int y = 0; y < years.size(); y++) {
    // Do stuff here;
}
```

You can avoid all the `std::` calls by doing:
```
using namespace std;

cout << years.size() << endl;
```

```
// 
```
