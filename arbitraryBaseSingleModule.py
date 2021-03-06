import sys

digits = '0123456789ABCDEF'


def base_check(base):
    if base < 2 or base > 16:
        return False
    return True


def convert_base_10(number, base):
    n_str = str(number)
    value_10 = 0
    for i, n in zip(range(len(n_str)), n_str[::-1]):
        n_digit = digits.index(n)
        value_10 += n_digit * (base ** i)
    return value_10


def convert_base_n(number, new_base):
    value = ''
    while number != 0:
        remainder = number % new_base
        value = digits[remainder] + value
        number = number // new_base
    return value


def digit_check(number, base):
    for i in str(number):
        if i > str(base - 1):
            return False
    return True


if __name__ == '__main__':

    number = int(input("Type the number: "))
    base = int(input("Type the base the number is on: "))
    new_base = int(input("Type the base to convert: "))

    if not base_check(base):
        print("The current base is outside [2,16]. Exiting...")
        sys.exit(1)

    if not base_check(new_base):
        print("The new base is outside [2,16]. Exiting...")
        sys.exit(2)

    if not digit_check(number, base):
        print("The number you entered cannot be in base %d" % base)
        sys.exit(3)

    n = convert_base_10(number, base)

    if new_base == 10:
        print(n)
    else:
        n = convert_base_n(n, new_base)
        print(n)