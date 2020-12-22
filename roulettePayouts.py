##
#Display the bets that pay out in a roulette simulation
#

from random import randrange

#simulate spinning the wheel, using 37 to represent 00
value = randrange(0,38)

if value == 37:
    print("The spin resulted in 00...")
else:
    print("The spin resulted in %d..."%value)

#Display the payout for a single number

if value == 37:
    print("Pay 00")
else:
    print("Pay", value)

#Display the color payout
#The first line in the condition checks for 1,3,5,7,9
#The second line in the condition checks for 12,14,16,18
#The third line in the condition checks for 19,21,23,25,27
#The fourth line in the condition checks for 30,32,34,36

if value % 2 == 1 and value >= 1 and value <= 9 or \
    value % 2 == 0 and value >= 12 and value <= 18 or \
    value % 2 == 1 and value >= 19 and value <= 27 or \
    value % 2 == 0 and value >= 30 and value <= 36:
    print("Pay Red")

elif value == 0 or value == 37:
    pass
else:
    print("Pay Black")

#Display the odd vs. even payout

if value >= 1 and value <= 36:
    if value % 2 == 1:
        print("Pay Odd")
    else:
        print("Pay Even")

#Display the lower number vs. upper number payout
if value >= 1 and value <= 18:
    print("Pay 1 to 18")
elif value >= 19 and value <= 36:
    print("Pay 19 to 36")
