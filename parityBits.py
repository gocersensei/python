##
# Compute even parity for sets of 8 bits entered by the user.
#

# Read the first line of input
line = input("Enter 8 bits: ")

#Continue looping until a blank line is entered
while line != "":
    #Ensure that the line has a total of 8 zeros and ones
    #and exaxtly 8 characters
    if line.count("0") + line.count("1") != 8 or len(line) != 8:
        #Display an appropriate error message
        print("That wasn't 8 bits...Try again.")
    else:
        #Count the number of ones
        ones = line.count("1")

        #Display the parity bit
        if ones % 2 == 0:
            print("The parity bit should be 0.")
        else:
            print("The parity bit should be 1.")

    #Read the next line of input
    line = input ("Enter 8 bits: ")

#The count method returns the number of times that the string
#provided as a parameter occurs in the string on which the method
#is invoked.