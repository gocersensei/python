##
# Convert a number from one base to another. Both the source
# and the destination base must be between 2 and 16.
#
#
from hex_digit import *

# Convert a number from base 10 to base n
# @param num the base 10 number to convert
# @param new_base the base to convert to
# @return the string of digits in new_base


def dec2n(num, new_base):
    # generate the representation of num in base new_base, storing it in result
    result = ""
    q = num

    # Perform the body of the loop once
    r = q % new_base
    result = int2hex(r) + result
    q = q // new_base

    # Continue looping until q == 0
    while q > 0:
        r = q % new_base
        result = int2hex(r) + result
        q = q // new_base

    return result

# Convert a number from base b to base 10
# @param num the base b number, stored in a string
# @param b the base of the number to convert
# @return the base 10 number


def n2dec(num, b):
    decimal = 0

    # process each digit in the base b number
    for i in range(len(num)):
        decimal = decimal * b
        decimal = decimal + hex2int(num[i])

    # return the result
    return decimal

# Convert a number between two arbitrary bases


def main():
    # Read the number from the user
    from_base = int(input("Enter the base to convert from: "))
    from_num = input("Enter a sequence of digits in that base: ")

    # Convert to base 10 and display the result
    dec = n2dec(from_num, from_base)
    print("That's %d in base 10." % dec)

    # Convert to a new base and display the result
    to_base = int(input("Enter the base to convert to: "))
    to_num = dec2n(dec, to_base)
    print("That's %s in base %d." % (to_num, to_base))


if __name__ == '__main__':
    main()
