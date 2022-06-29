#!/usr/bin/bash
gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC  -I/usr/include/python3.8 103-python.c


python3 test.py