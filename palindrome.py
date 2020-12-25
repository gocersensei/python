##
# Determine whether or not a string entered by the user is a
# palindrome.
#

# Read the input from the user
line = input("Enter a string: ")

#Assume that it is a palindrom until we can prove otherwise
is_palindrome = True

#Check the characters, starting from the ends until
#the middle is reached

for i in range(0, len(line) //2):
    #If the characters don't match then mark
    #that the string is not a palindrome
    if line[i] != line[len(line)-i-1]:
        is_palindrome = False

    #Display a meaningful output message
if is_palindrome:
    print(line, "is a palindrome")
else:
    print(line, "is not a palindrome")