##
# Determine the name of a triangle from the lengths of its sides
##

# Read the side lengths from the user

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Determine the triangle's name

if side1 == side2 and side2 == side3:
    name = "equilateral"
elif side1 == side2 or side2 == side3 or \
        side3 == side1:
    name = "isoceles"
else:
    name = "scalene"

# Display the triangle`s name
print("That`s a", name, "triangle")

# We could also check that side1 is equal to side3 as part
# of the condition for an equilateral triangle.
# However, that comparison isn`t necessary because
# the == operator is transitive.
