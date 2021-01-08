##
# Compute random but distinct numbers for a lottery ticket.
#
from random import randrange

min_num = 1
max_num = 49
num_nums = 6

# Keep a list of the numbers for the ticket
ticket_nums = []

# Generate num_nums random but distinct numbers

for i in range(num_nums):
    # Generate a number that isn't already on the ticket
    rand = randrange(min_num, max_num + 1)
    while rand in ticket_nums:
        rand = randrange(min_num, max_num + 1)

    # Add the distinct number to the ticket
    ticket_nums.append(rand)

# Sort the numbers into ascending order and display them

ticket_nums.sort()
print("Your numbers are: ", end="")
for n in ticket_nums:
    print(n, end=" ")
print()
