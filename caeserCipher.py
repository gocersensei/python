##
#Implement a Caesar cipher that shifts all of the letters
#in a message by an amount provided by the user. Use a
## negative shift value to decode a message

# Read the message and shift the amount from the user

message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

#Process each character, constructing a new message
new_message = ""

for ch in message:
    if ch >= "a" and ch <= "z":
        #process a lowercase letter by determining
        #its position in the alphabet (0-25), computing its
        #new position, and adding it to the new message.
        pos = ord(ch) - ord("a")
        pos = (pos + shift) % 26
        new_char = chr(pos + ord("a"))
        new_message = new_message + new_char
    elif ch >= "A" and ch <= "Z":
        #process an uppercase letter by determining its position
        #in the alphabet (0-25), computing its new position, and
        #adding it to the new message
        pos = ord(ch) - ord("A")
        pos = (pos + shift) % 26
        new_char = chr(pos + ord("A"))
        new_message = new_message + new_char
    else:
        #If the character is not a letter then copy it into
        #the new message
        new_message = new_message + ch

#Display the shifted message
print("The shifted message is", new_message)
