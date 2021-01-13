##
# Determine all of the prime numbers from 2 to some limit entered
# by the user using the Sieve of Eratosthenes.
#

# Read the limit from the user
limit = int(input("Generate all primes up to what limit? "))

# Generate all of the numbers from 0 to limit
nums = []
for i in range(0, limit + 1):
    nums.append(i)

# "Cross out" 1 by replacing it with a 0
nums[1] = 0

# Cross out all of the multiples of each prime number that we discover
p = 2
while p < limit:
    # Cross out all multiples of p (but not p itself)
    for i in range(p * 2, limit + 1, p):
        nums[i] = 0

    # Find the next number that is not crossed out
    p = p + 1
    while p < limit and nums[p] == 0:
        p = p + 1

# Display the result
print("The primes up to", limit, "are:")
for i in nums:
    if nums[i] != 0:
        print(i)
