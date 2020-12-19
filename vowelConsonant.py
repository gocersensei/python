##
# Determine if a letter is a vowel or a consonant
##

#Read a letter from the user
letter = input("Enter a letter of the alphabet: ")

#Classify the letter and report the result

if letter == "a" or letter == "e" or \
    letter == "i" or letter == "o" or \
    letter == "u":
    print("It`s a vowel.")
elif letter == "y":
    print("Sometimes it`s a vowel...Sometimes it`s a consonant.")
else:
    print("It`s a consonant")

##
# This version of the program only works for lowercase letters.
# You can add support for uppercase letters by including
# additional comparisons that follow the same pattern.
##