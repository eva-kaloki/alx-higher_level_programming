#!/usr/bin/python3

# Prints the ASCII alphabet in lowercase without a new line
for i in range(97, 123):
    if chr(i) not in "eq":
        print(f"{chr(i)}", end="")
