##
# Perform run-length encoding on a string or a list using recursion.
#
# Perform run-length encoding on a string or a list
# @param data the string or list to encode
# @return a list where the elements at even positions are data values and the elements at odd
# positions are counts of the number of times that the data value ahead of it should be
# replicated

def encode(data):
    # If data is empty then no encoding work is necessary
    if len(data) == 0:
        return []

    # Find the index of the first item that is not the same as the item at position 0 in data
    index = 1
    while index < len(data) and data[index] == data[index - 1]:
        index = index + 1
    # Encode the current character group
    current = [data[0], index]
    # Use recursion to process the characters from index to the end of the string
    return current + encode(data[index: len(data)])


# Demonstrate the encode function
def main():
    # Read a string from the user
    s = input("Enter some characters: ")
    # Display the result
    print("When those characters are run-length encoded," \
          "the result is:", encode(s))


# Call the main function
main()
