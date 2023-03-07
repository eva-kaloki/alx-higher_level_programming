#!/usr/bin/python3

# This program checks if a character is lowercase or not
def islower(c):
    " " "
    Checks if a given character is lowercase .
    
    Arguments:
    c -- the character to check

    Returns:
    True if c is lowercase, False otherwise
    " " "
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
