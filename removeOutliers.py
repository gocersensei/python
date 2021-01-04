#
# Remove the outliers from a data set.
#

# Remove the outliers from a list of data
# @param data the list of data values to process
# @param num_outliers the number of smallest and largest values to remove
# @ return a new copy of data where the values are sorted into ascending
# order and the smallest and largest values have been removed.

def remove_outliers(data, num_outliers):
    # Create a new copy of the list that is in sorted order
    retval = sorted(data)

    # Remove num_outliers largest values
    for i in range(num_outliers):
        retval.pop()

    # Remove num_outliers smallest values
    for i in range(num_outliers):
        retval.pop(0)

    # Return the result
    return retval


# Read data from the user, and remove the two largest and two smallest values
def main():
    # Read values from the user until a blank line is entered
    values = []
    s = input("Enter a value (blank line to quit): ")
    while s != "":
        num = float(s)
        values.append(num)
        s = input("Enter a value (blank line to quit): ")

    # Display the result or an appropriate error message
    if len(values) < 4:
        print("You didn't enter enough values.")

    else:
        print("With the outliers removed: ", remove_outliers(values, 2))
        print("The original data: ", values)


# Call the main function
main()
