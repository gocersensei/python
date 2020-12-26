##
# Compute the greatest common divisor of two positive integers
# using a while loop.
#

# Read two positive integers from the user

n = int(input("Enter a positive integer: "))
m = int(input("Enter a positive integer: "))

# Initialize d to the smaller of n and m

d = min(n, m)

# Use a while loop to find the greatest common divisor of n and m
while n % d != 0 or m % d != 0:
    d = d - 1

# Report the result
print("The greatest common divisor of", n, "and", m, "is", d)
