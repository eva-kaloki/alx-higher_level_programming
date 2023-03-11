#!/usr/bin/python3
# define a function named print_list_integer that takes a single parameter my_list
def print_list_integer(my_list=[]):

    # iterate over each element in my_list
    for element in my_list:
        # print each integer element in the list using string formatting
        print("{:d}" .format(element))


# create a list of integers
my_list = [1, 2, 3, 4, 5]

# call the print_list_integer and pass my_list as an argument
print_list_integer(my_list)
