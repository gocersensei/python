# This program multiplies two numbers
# Testing my github connection
while True:
    try:
        x = int(input('enter a number'))
    except ValueError:
        print('Sorry,not a number')
        continue
    else:
        break

while True:
    try:
        y = int(input('enter a number'))
    except ValueError:
        print("Sorry, not a number")
        continue
    else:
        a = float(x)
        b = float(y)
        c = x * y
        print('the result', c)
    break
