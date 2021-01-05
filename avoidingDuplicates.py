#
# Read a collection of words entered by the user. Display each word
# entered by the user only once, in the same order that the words
# were entered.
#

# Begin reading words into a list

words = []
word = input("Enter a word (Blank line to quit): ")
while word != "":
    # Only add the word to the list if
    # it is not already present in it
    if word not in words:
        words.append(word)

    # Read the next word from the user
    word = input("Enter a word (blank line to quit): ")

# Display the unique words
for word in words:
    print(word)
