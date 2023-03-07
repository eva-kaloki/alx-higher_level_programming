#!/usr/bin/python3
# This program prints numbers from 0 to 99, separated by a comma and space, in ascending order
for num in range(0, 99):
    print('{:02d}, '.format(num), end='')
print('99')
