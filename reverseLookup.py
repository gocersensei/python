##
# Conduct a reverse lookup on a dictionary, finding all of
# the keys that map to the provided value.
#

# Conduct a reverse lookup on a dictionary
# @param data the dictionary to perform the reverse lookup on
# @param value the value to search for in the dictionary
# @return a list (possibly empty) of keys from data that map to value

def reverseLookup(data, value):
    # Construct a list of the keys that map to value
    keys = []

    # Check each key in data:
    for key in data:
        if data[key] == value:
            keys.append(key)

    # Return the list of keys
    return keys


# Demonstrate the reverseLookup function
def main():
    # A dictionary mapping 4 French words to their English
    # equivalents
    frEn = {"le": "the", "la": "the", "livre": "book", "pomme": "apple"}

    # Demonstrate the reverseLookup function with 3 cases: One that
    # returns mutiple keys, one that returns one key, and one that
    # returns no keys.

    print("The french words for 'the' are: ", reverseLookup(frEn, "the"))
    print("Expected: ['le', 'la']")
    print()
    print("The french word for 'apple' is: ", reverseLookup(frEn, "apple"))
    print("Expected: ['pomme']")
    print()
    print("The french word for 'asdf' is: ", reverseLookup(frEn, "asdf"))
    print("Expected: []")


# Only call the main function if this file has not been imported
if __name__ == "__main__":
    main()
