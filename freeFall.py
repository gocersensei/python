#Create a program that determines how quickly an object is traveling when it hits the
#ground. The user will enter the height from which the object is dropped in meters (m).
#Because the object is dropped its initial speed is 0m/s. Assume that the acceleration
#due to gravity is 9.8m/s2. You can use the formula vf = vi2 + 2ad to compute the
#final speed, vf , when the initial speed, vi, acceleration, a, and distance, d, are known.

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