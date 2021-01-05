def hex2int(hexa):
    H = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    h = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    decimal = 0

    while True:
        for i in hexa:
            if (i in h) or (i in H):
                continue
            else:
                print("You just entered something unrecognizable as a hexadecimal number")
                hexa = input("Enter a number in hexadecimal format: ")
                break
        else:
            break

    for i in range(len(hexa)):

        exp = len(hexa) - i - 1
        if hexa[i] in h:
            value = h.index(hexa[i])
        elif hexa[i] in H:
            value = h.index(hexa[i])
        decimal = decimal + value * 16 ** exp

    return decimal


def int2hex(inter):
    while True:
        try:
            inter = int(inter)
        except ValueError:
            print("You have just entered something not recognizable as a whole number")
            inter = input("Enter a positive number between 0 and 15: ")
            continue
        else:
            inter = int(inter)
            break
    h = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    return h[inter]
