##
# Convert a number from Decimal (base 10) to Binary (base 2)
#

NEW_BASE = 2

# Read the number to convert from the user
num = int(input("Enter a non-negative integer: "))

# Generate the binary representation of num
# storing it in result
result = ""
q = num

# Perform the body of the loop once
r = q % NEW_BASE
result = str(r) + result
q = q // NEW_BASE

# Keep on looping until q == 0
while q > 0 :
    r = q % NEW_BASE
    result = str(r) + result
    q = q // NEW_BASE

# Display the result
print(num, "in Decimal is", result, "in Binary")