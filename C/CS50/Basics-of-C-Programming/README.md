# The Basics of C Programming
### The Simplest C Program
**File Name:** _simp.c_
**Description:** Hello World in C

**Notes:**
- `#include <stdio.h>` includes the "standard I/O" library into the program. The Standard I/O library allows reading stndarding input (from keyboard) and write standard output (to screen), process text files from disk, etc.
- `int main()` declares the main function. Every C program must have a function named main. Execution starts at the first line of main.
- `{ }` denote code blocks.
- `printf` allows sending output to standard out. The format string is in quotes. Format strings allow string literals ("text") and symbols ("/n"), and placeholders ("%s").
- `return 0;` causes the function to return error code 0 (no error) to the shell that started its execution.

![diagram](http://s.hswstatic.com/gif/c-compile.gif)

**Reference:** [http://computer.howstuffworks.com/c2.htm](http://computer.howstuffworks.com/c2.htm)



### Variables and Printf
**File Name:** add.c
**Description:** Declares variables, performs arithmatic, and passing them as arguments to ``printf`` using placeholders.

**Notes:**
- `int a, b, c;` declares three integer variables named **a**, **b**, and **c**.
- The `%d` placeholders are replaced with values based on their ordinal positions and the positions of the subsequently passed arguments to printf.
- `scanf` accepts input in the same types of formatted strings as `printf` does.
- The **&** (address operator) returns the address of a variable. Scanf accepts variables with the address operator to assign input to the variable.

![add.c](http://s.hswstatic.com/gif/c-exec.gif)

**Reference:** [http://computer.howstuffworks.com/c5.htm](http://computer.howstuffworks.com/c5.htm)