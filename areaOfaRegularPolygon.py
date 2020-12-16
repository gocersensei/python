#A polygon is regular if its sides are all the same length and the angles between all of
#the adjacent sides are equal. The area of a regular polygon can be computed using
#the following formula, where s is the length of a side and n is the number of sides:
#Write a program that reads s and n from the user and then displays the area of a
#regular polygon constructed from these values.

##
#Compute the area of a regular polygon
##
from math import tan,pi

#Read input from the user

s=float(input("Enter the length of each side of the polygon: "))
n= int(input("Enter the number of sides: "))

#Compute the area of the polygon

area = (n*s**2) / (4 * tan(pi /n))

#Display the result

print("The are of the polygon is ", area)