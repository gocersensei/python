mylist = []
while True:
    s = input("Enter a String:")
    s = s.lower()
    if s:
        mylist.append(s)
    else:
        break
newlist = []
for item in mylist:
    if item not in newlist:
        newlist.append(item)

print("\nOriginal List")
for i in mylist:
    print(i)

print("\nList after Removing Duplicates")
for i in newlist:
    print(i)