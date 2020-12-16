#Write a program that reads a positive integer, n, from the user and then displays the
#sum of all of the integers from 1 to n. The sum of the first n positive integers can be
#computed using the formula:

##
#Compute the sum of the first n positive integers
#

#Read input from the user

n = int(input("Enter a positive integer: "))

#Compute the sum

sm = n* (n+1) / 2

#Display the result
print("The sum of the first", n, "positive integers is ", sm)