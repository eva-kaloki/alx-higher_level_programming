# This program prints numbers from 0 to 99, separated by a comma and space, in ascending order
for i in range(100):
    if i < 99:
        print("{:02d}, ".format(i), end="")
    else:
        print("{:02d}".format(i))
