##
# Display a list of items so that they are separated by commas
# and the word "and" appears between the final two item.
#

# Format a list of items so that they are separated by commas and "and"
# @param items the list of items to format
# @return a string containing the items with the desired formatting
#

def format_list(items):
    # Handle list of 0 and 1 items as special cases
    if len(items) == 0:
        return "<empty>"
    if len(items) == 1:
        return str(items[0])

    # Loop over all of the items in the list except the last two
    result = ""
    for i in range(0, len(items) - 2):
        result = result + str(items[i]) + ", "

    # Add the second last and last items to the result, separated by "and"
    result = result + str(items[len(items) - 2]) + " and "
    result = result + str(items[len(items) - 1])

    # return result
    return result


def main():
    # Read items from the user until a blank line is entered
    items = []
    line = input("Enter an item (blank to quit): ")
    while line != "":
        items.append(line)
        line = input("Enter an item (blank to quit): ")

    # Format and display the items
    print("The items are %s. " % format_list(items))


# Call the main function
main()
