#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if chr(i) in "qe":
        continue
    print("{}".format(chr(i)), end="")
