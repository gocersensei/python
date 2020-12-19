##
# Determine and display the whether an integer entered by the
#user is even or odd...
##

#Read the integer from the user

num = int(input("Enter an integer: "))

#Determine whether it is even or odd by using the
#modulus (remainder) operator

if num % 2 == 1:
    print(num, "is odd.")

else:
    print(num, "is even.")


#Dividing en even number by 2 always results
#in a remainder of 0. Dividing an odd number by
#2 always results in a remainder of 1.