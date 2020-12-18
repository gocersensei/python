##
#Compute the amount of energy needed to heat of water, and
#the cost of doing so.
##

#Define constants for the specific heat capacity of water and
#the price of electricity

WATER_HEAT_CAPACITY = 4.186
ELECTRICITY_PRICE = 8.9
J_TO_KWH = 2.777e-7

# Python allows numbers to be written in scientific notation by
#placing the coefficient to the left of an e and the exponent
#to its rights. As a result, 2.77*10to the power of -7 is
#written as 2.777e-7

#Read the volume from the user
volume = float(input("Enter the amount of water in milliliters: "))
d_temp = float(input("Enter the temperature increase (degrees Celcius): "))

#Compute the energy in Joules
q = volume * d_temp * WATER_HEAT_CAPACITY

#Display the result in Joules
print("That will require %d Joules of energy." % q)

#Compute the cost
kwh = q * J_TO_KWH
cost = kwh * ELECTRICITY_PRICE

#Display the cost
print("That much energy will cost %.2f cents." % cost)


##
# Because water has a density of 1 gram per milliliter grams and milliliters can be
# used interchangeably. Prompting the user for milliliters makes the program easier
# to use because most people think about the volume of water in a coffee cup, not
# its mass.
##
