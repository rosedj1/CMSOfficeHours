# A Simple C++ Script

```c++
#include <iostream>
#include <string>

int main() {
    std::string words[4] = {"An", "array", "of", "words."};

    for (int i = 0; i < sizeof(words)/sizeof(words[0]); ++i) {
        std::cout << words[i] << std::endl;
    }
    return 0;
}
```
