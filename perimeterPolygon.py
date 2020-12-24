##
# Compute the perimeter of a polygon. The user will enter
# a blank line for the x-coordinate to indicate that all of
# the points have been entered
#

from math import sqrt

#Store the perimeter of the polygon

perimeter = 0

#Read the coordinate of the first point

first_x = float(input("Enter the x part of the coordinate: "))
first_y = float(input("Enter the y part of the coordinate: "))

#Provide initial values for prev_x and prev_y
prev_x = first_x
prev_y = first_y

#Read the remaining coordinates
line = input("Enter the x part of the coordinate (blank to quit): ")
while line != "":
    #Convert the x part to a number and read the y part
    x = float(line)
    y = float(input("Enter the y part of the coordinate: "))

    #Compute the distance to the previous point and add it to the
    #perimeter
    dist= sqrt((prev_x - x) ** 2 + (prev_y - y) ** 2)
    perimeter = perimeter + dist

    #Set up prev_x and prev_y for the next loop iteration
    prev_x = x
    prev_y = y

    #Read the x part of the coordinate
    line = input("Enter the x part of the coordinate (blank to quit): ")

#Compute the distance from the last point to the first point and
#add it to the perimeter

dist = sqrt((first_x - x) ** 2 + (first_y - y) **2)
perimeter = perimeter + dist

#Display the result
print("The perimeter of that polygon is", perimeter)