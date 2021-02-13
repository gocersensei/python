def mysum(*items):
    # In Python, everything is considered “True” in an
    # “if,” except for “None,” “False,” 0, and empty
    # collections. So if the tuple “items” is empty,
    # we’ll just return an empty tuple.
    if not items:
        return items
    output = items[0]

    # We’re assuming that the elements of “items” can be added together.

    for item in items[1:]:
        output += item
    return output


print(mysum())
print(mysum(10, 20, 30, 40))
print(mysum('a', 'b', 'c', 'd'))
print(mysum([10, 20, 30], [40, 50, 60], [70, 80]))
