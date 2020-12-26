##
# Display a multiplication table for 1 times 1 through
# 10 times 10
#

MIN = 1
MAX = 10

# Display the top row of labels

print("    ", end="")
for i in range(MIN, MAX + 1):
    print("%4d" % i, end="")
print()

# Display the table

for i in range(MIN, MAX + 1):
    print("%4d" % i, end="")
    for j in range(MIN, MAX + 1):
        print("%4d" % (i * j), end="")
    print()
