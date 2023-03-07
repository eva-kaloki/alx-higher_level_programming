# This program generates and prints all possible combinations of two digits in ascending order, following the given constraints.
for i in range(0, 10):
    for j in range(i+1, 10):
        if i == 8 and j == 9:
            print("{:02d}{:d}".format(i, j))
        else:
            print("{:02d}{:d}, ".format(i, j), end="")
