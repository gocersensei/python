# The operator module provides functions that implement all
# built-in operators.
import operator


def calc(to_solve):

    # Yes, functions can be the values in a dict!
    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  # You can choose between truediv, which returns a float, as with the “/”
                  # operator, or floordiv, which returns an integer, as with the “//” operator.
                  '/': operator.truediv,
                  '**': operator.pow,
                  '%': operator.mod}
    # Splits the line, assigning via unpacking
    op, first_s, second_s = to_solve.split()
    first = int(first_s)
    second = int(second_s)

    # Calls the function retrieved via operator, passing “first”
    # and “second” as arguments
    return operations[op](first, second)

print(calc('+ 2 3'))