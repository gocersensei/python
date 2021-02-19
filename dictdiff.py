def dictdiff(first, second):
    output = {}

    all_keys = first.keys() | second.keys()
    # Gets all keys from both first and second, without repeats

    for key in all_keys:
        if first.get(key) != second.get(key):
            output[key] = [first.get(key),
                           second.get(key)]

            # Takes advantage of the fact
            # that dict.get returns None
            # when a key doesn’t exist
    return output


d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'd': 4}
print(dictdiff(d1, d2))