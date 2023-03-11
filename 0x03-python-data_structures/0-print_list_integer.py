#!/usr/bin/python3
# define a function named print_list_integer that takes a single parameter my_list
def print_list_integer(my_list=[]):
    # iterate over each element in my_list
    for element in my_list:
        # print each integer element in the list using string formatting
        print("{:d}" .format(element))
