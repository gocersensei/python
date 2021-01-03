##
# Display the integers entered by the user in ascending order.
#

# Start with an empty list

data = []

# Read values, adding them to the list, until the user enters 0

num = int(input("Enter an integer (0 to quit): "))
while num != 0:
    data.append(num)
    num = int(input("Enter an integer (0 to quit): "))

# Sort the values

data.sort()

# Display the values in ascending order

print("The values, sorted into ascending order, are: ")

for num in data:
    print(num)