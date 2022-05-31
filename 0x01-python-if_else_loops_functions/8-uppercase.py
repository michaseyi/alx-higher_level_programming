#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print("{}".format(chr(ord(c) - (ord('a') - ord('A'))) if c >=
              'a' and c <= 'z' else c), end="")
    print()
