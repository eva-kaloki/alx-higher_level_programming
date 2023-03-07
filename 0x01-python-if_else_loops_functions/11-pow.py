#!/usr/bin/python3

# Compute a to the power of b
def pow(a, b):
    # Initialize the result to 1
    result = 1
    # Multiply a by itself b times
    for i in range(b):
        result *= a
    # Return the result
    return result

