# Determine whether or not a license plate is valid. Valid
# license plate either consists of:
# 1. Three letters followed by three numbers, or
# 2. Four numbers followed by three numbers

# Read the plate from the user
plate = input("Enter the license plate: ")

# Check the status of the plate and display it. It is necessary
# to check each of the 6 characters for an older style plate,
# or each of the 7 characters for a newer style plate.

if len(plate) == 6 and "Z" >= plate[0] >= "A" <= plate[1] <= "Z" and \
        "A" <= plate[2] <= "Z" and \
        "O" <= plate[3] <= "9" and \
        "O" <= plate[4] <= "9" and \
        "O" <= plate[5] <= "9":
    print("The plate is a valid older style plate.")

elif len(plate) == 7 and "0" <= plate[0] <= "9" and \
        "0" <= plate[1] <= "9" and \
        "0" <= plate[2] <= "9" and \
        "0" <= plate[3] <= "9" and \
        "A" <= plate[4] <= "Z" and \
        "A" <= plate[5] <= "Z" and \
        "A" <= plate[6] <= "Z":
    print("The plate is a valid newer style plate.")

else:
    print("The plate is not valid.")
