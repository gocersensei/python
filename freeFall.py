#Compute the speed of an object when it hits the ground after being dropped.

from math import sqrt

#Define a constant for the acceleration due to gravity in m/s**2

GRAVITY = 9.8

#Read the height from which the object is dropped

d= float (input("Height from which the pbject is dropped (in meters): "))

#Compute the final velocity

vf = sqrt(2*GRAVITY*d)

#Display the result
print("It will hit the ground at %2f m/s." % vf)



