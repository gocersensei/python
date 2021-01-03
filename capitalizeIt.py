##
# Improve the capitalization of a string by replacing "i"
# with "I" and by capitalizing the first letter of each sentence
#

# Capitalize the appropriate characters in a string
# @param s the string that needs capitalization
# @return a new string with the capitalization improved

def capitalize(s):
    # Correct the capitalization for i
    result = s.replace(" i ", " I ")

    # Capitalize the first character of the string
    if len(s) > 0:
        result = result[0].upper() + result[1: len(result)]

    # Capitalize the first letter that follows a ".","!" or "?"
    pos = 0
    while pos < len(s):
        if result[pos] == "." or result[pos] == "!" or result[pos] == "?":
            # Move past the ".", "!" or "?"
            pos = pos + 1

            # Move past any spaces
            while pos < len(s) and result[pos] == " ":
                pos = pos + 1

            # If we have reached the end of the string then
            # replace the current character with its upper
            # equivalent

            if pos < len(s):
                result = result[0: pos] + result[pos].upper() + result[pos + 1: len(result)]

        # Move to the next character
        pos = pos + 1

    return result


# Demonstrate the capitalize function

def main():
    s = input("Enter some text: ")
    capitalized = capitalize(s)
    print("It is capitalized as:", capitalized)


# Call the main function
main()
