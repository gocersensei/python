value = input("Enter a Number: ")
total = 0

# Read numbers from users until blank.
while value != "":
    try:
        # Convert value to number.
        num = float(value)
        total += num
        print("Current Total :", total)

    # Raise Exception if not a number.
    except valueError:
        if value == '':
            break
        else:
            print(num, 'is an invalid  number')


# Display the Total.
print("The Total is:", total)
