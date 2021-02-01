with open("elements.txt") as myfile:
    head = [next(myfile) for x in range(10)]
print(head)