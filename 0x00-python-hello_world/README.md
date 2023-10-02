# 0x00 Python

## for pthon scripts:
- All your files should end with a new line
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- The first line of all your files should be exactly #!/usr/bin/python3
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable

## for shell scripts:
- All your scripts should be exactly two lines long (wc -l file should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly #!/bin/bash
- All your files must be executable

## for C scripts:
- All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options -Wall -Werror -Wextra -pedantic -std=gnu89
- All your files should end with a new line
- Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
- You are not allowed to use global variables
- No more than 5 functions per file
- All your header files should be include guarded*

# TASKS

Task 0:

[0. Run Python file](0-run)
Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE

Task 1:
[1. Run inline](1-run_inline)
Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE

Task 2:
[2. Hello, print](2-print.py)
Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

Use the function print

Task 3:
[3. Print integer](3-print_number.py)
Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

Task 4:
[4. Print float](4-print_float.py)
complete the [source code](https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py) in order to print the float stored in the variable number with a precision of 2 digits.

Task 5:
[5. Print string](5-print_string.py)
Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

Task 6:
[6. Play with strings](6-concat.py)
Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py) to print Welcome to Holberton School!

Task 7:
[7. Copy - Cut - Paste](7-edges.py)
Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py)

Task 8:
[8. Create a new sentence](8-concat_edges.py)
Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py) to print object-oriented programming with Python, followed by a new line.

Task 9:
[9. Easter Egg](9-easter_egg.py)
Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)

Task 10:
[10. Linked list cycle](10-check_cycle.c), (lists.h)
Write a function in C that checks if a singly linked list has a cycle in it.

Prototype: int check_cycle(listint_t *list);
Return: 0 if there is no cycle, 1 if there is a cycle
Requirements:

Only these functions are allowed: write, printf, putchar, puts, malloc, free

Task 11:
[11. Hello, write](100-write.py)
Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.

Use the function write from the sys module
You are not allowed to use print
Your script should print to stderr
Your script should exit with the status code 1

Task 12:
[12. Compile](101-compile)
Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable $PYFILE

The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)

Task 13:
[13. ByteCode -> Python #1](102-magic_calculation.py)
Write the Python function def magic_calculation(a, b): that does exactly the same as the provided  Python bytecode:
