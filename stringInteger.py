##
# Determine whether or not a string entered by the user
# is an integer.
#

## Determine if a string contains valid representation
# of an integer
# @param s the string to check
# @return True if s represents an integer. False otherwise.

def isInteger(s):
    # Remove whitespace from the beginning and end of the string

    s = s.strip()

    # Determine if the remaining characters form a valid integer

    if (s[0] == "+" or s[0] == "-") and s[1:].isdigit():
        return True
    if s.isdigit():
        return True
    return False

# Demonstrate the isInteger function
def main():
    s = input("Enter a string: ")
    if isInteger(s):
        print("That string represents an integer.")
    else:
        print("That string does not represent an integer.")

# Only call the main function when this file has not been imported

if __name__ == "__main__":
    main()

# The isdigit method returns true if and only
# if the string is at least one character in length
# and all of the characters in the string are digits.

# The __name__ variable is automatically assigned a value by Python
# when the program starts running. It contains "__main__" when
# the file is executed directly by Python. It contains the
# name of the module when the file is imported into another program.

