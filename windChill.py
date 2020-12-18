##
#Compute the wind chill index for a given air temperature
#and wind speed
#

WC_OFFSET = 13.12
WC_FACTOR1 = 0.6215
WC_FACTOR2 = -11.37
WC_FACTOR3 = 0.3965
WC_EXPONENT = 0.16

#Computing wind chill requires several numeric constants
#that were determined by scientists and medical experts

#Read the air temperature and wind speed from the user

temp = float(input("Enter the air temperature (degree Celsius): "))
speed = float(input("Enter the wind speed (kilometers per hour): "))

#Compute the wind chill index

wci = WC_OFFSET +\
    WC_FACTOR1 * temp +\
    WC_FACTOR2 * speed ** WC_EXPONENT +\
    WC_FACTOR3 * temp * speed ** WC_EXPONENT

#Display the result rounded to the closest integer
print("The wind chill index is ", round(wci))

