##
# Generate and display a random password containing between
# 7 and 10 characters
#

from random import randint

SHORTEST = 7
LONGEST = 10
MIN_ASCII = 33
MAX_ASCII = 126

## Generate a random password
# @return a string containing a random password

def randomPassword():
    #Select a random length for the password
    randomLength = randint(SHORTEST, LONGEST)

    # Generate an appropriate number of random characters, adding
    # each one to the end of result
    result =""
    for i in range(randomLength):
        randomChar = chr(randint(MIN_ASCII, MAX_ASCII))
        result = result + randomChar

    # Return the random password
    return result

# Generate and display a random password

def main():
    print("Your random password is: ", randomPassword())

# Call the main function only if the module is not imported

if __name__ == "__main__":
    main()

##
# The chr function takes an ASCII code as its parameter.
# It returns a string containing the character with that
# ASCII code as its result
#
