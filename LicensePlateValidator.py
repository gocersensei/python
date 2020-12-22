## Determine whether or not a license plate is valid. Avalid
#license plate either consists of:
#1. Three letters followed by three numbers, or
#2. Four numbers followed by three numbers

#Read the plate from the user
plate = input("Enter the license plate: ")

#Check the status of the plate and display it. It is necessary
#to check each of the 6 characters for an older style plate,
#or each of the 7 characters for a newer style plate.

if len(plate) == 6 and plate[0] >= "A" and plate[0] <= "Z" and \
    plate[1] >= "A" and plate[1] <= "Z" and \
    plate[2] >= "A" and plate[2] <= "Z" and \
    plate[3] >= "O" and plate[3] <= "9" and \
    plate[4] >= "O" and plate[4] <= "9" and \
    plate[5] >= "O" and plate[5] <= "9" :
        print("The plate is a valid older style plate.")

elif len(plate) == 7 and plate[0] >= "0" and plate[0] <= "9" and \
    plate[1] >= "0" and plate[1] <= "9" and \
    plate[2] >= "0" and plate[2] <= "9" and \
    plate[3] >= "0" and plate[3] <= "9" and \
    plate[4] >= "A" and plate[4] <= "Z" and \
    plate[5] >= "A" and plate[5] <= "Z" and \
    plate[6] >= "A" and plate[6] <= "Z":
        print("The plate is a valid newer style plate.")

else:
    print("The plate is not valid.")


