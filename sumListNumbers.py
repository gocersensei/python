#
# Compete the sum of numbers entered by the user,
# ignoring non-numeric input
#

# Read the first line of input from the user
line = input("Enter a number: ")
total = 0

# Keep reading until the user enters a blank line
while line != "":
    try:
        # Try and convert the line to a number
        num = float(line)
        # If the conversion succeeds then add it to the total and display it
        total = total + num
        print("The total is now", total)

    except ValueError:
        # Display an error message before going on to read the next value
        print("That wasn't a number.")

    # Read the next number
    line = input("Enter a number: ")

# Display the total
print("The grand total is", total)
