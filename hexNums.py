def hex_output():
    decnum = 0
    hexnum = input('Enter a hex number to convert: ')

    # reversed returns a new iterable, which returns another iterable’s
    # elements in reverse order. By invoking enumerate on the
    # output from reversed, we get each element of hexnum, one at
    # a time, along with its index,starting with 0.

    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 ** power)
    print(decnum)


hex_output()

# FFFF3 1048563