#!/usr/bin/python3
# This function takes a string as an argument and prints the uppercase version of the string followed by a new line.
def uppercase(s):
    for i in s:
        if ord(i) >= 97 and ord(i) <= 122:
            print(chr(ord(i) - 32), end="")
        else:
            print(i, end="")
    print()

