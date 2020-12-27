##
# Find the maximum of 100 random integers, counting the number
# of times the maximum value is updated during the process
#

from random import randrange

NUM_ITEMS = 100

#Generate the first number and display it

mx_value = randrange(1, NUM_ITEMS + 1)
print(mx_value)

#Count the number of updates

num_updates = 0

# For each of the remaining numbers

for i in range(1, NUM_ITEMS):
    #Generate a new random number
    current = randrange(1, NUM_ITEMS + 1)

    # If the generated number is the largest one we have
    # seen so far
    if current > mx_value:
        # Update the maximum and count the update
        mx_value = current
        num_updates = num_updates + 1
        #Display the number, noting that an update occured
        print(current, "<== Update")
    else:
        #Display the number
        print(current)
# Display the summary results
print("The maximum value found was ", mx_value)
print("The maximum value was updated", num_updates, "times")