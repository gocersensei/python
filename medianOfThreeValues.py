##
# Compute and display the median of three values entered by
# the user. This program includes two implementations of the median
# function that demonstrate different techniques for computing the
# median of three values
#

## Compute the median of three values using if statements
# @param a the first value
# @param b the second value
# @param c the third value
# @return the median of values a,b and c

def median(a,b,c):
    if a < b and b  < c or a > b and b > c:
        return b
    if b < a and a < c or b > a and a > c:
        return a
    if c < a and b < c or c > a and b > c:
        return c

## Compete the median of three values using the min and max
# functions and a little bit of arithmetic
# @param a the first value
# @param b the second value
# @param c the third value
# @return the median of values a, b and c
#
def alternateMedian(a,b,c):
    return a + b + c - min(a,b,c) - max(a,b,c)

# Display the median of three values entered by the user
def main():
    x = float(input("Enter the first value: "))
    y = float(input("Enter the second value: "))
    z = float(input("Enter the third value: "))

    print("The median value is:", median(x,y,z))
    print("Using the alternative method, it is", alternateMedian(x,y,z))
#Call the main function
main()