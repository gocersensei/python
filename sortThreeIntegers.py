##
# Sort 3 values entered by the user into increasing order.
##

# Read the numbers from the user, naming them a, b and c

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

mn = min(a, b, c)  # minimum value
mx = max(a, b, c)  # maximum value
md = a + b + c - mn - mx  # the middle value

# Display the result

print("The numbers in sorted order are:")
print(" ", mn)
print(" ", md)
print(" ", mx)

# Since min and max are the name of functions in Python
# we shouldn't use those names for variables. Instead we
# use variables named mn and mx to hold the minimum and
# maximum values respectively.
##
