def sieve(num):
    """
    This function uses sieve of eratosthenes algorithm to compute
    a list of prime numbers within a range.
    @param: Integer - num
    @return: List of integers.
    """

    # Initialize state variables.
    prime_num = list()
    p = 2

    # Create a list of booleans the size of num.
    prime_bol = [True for i in range(num + 1)]

    while (p * p <= num):

        # Go through the list Switching non prime numbers position to False.
        if (prime_bol[p] == True):

            for i in range(p * 2, num + 1, p):
                prime_bol[i] = False
        p += 1

    prime_bol[0] = False
    prime_bol[1] = False

    # Populate prime_num based on the values of prime_bol.
    for p in range(num + 1):
        if prime_bol[p]:
            prime_num.append(p)
    return prime_num


def main():
    # Request input from user and get prime numbers up to the input.
    i = 1
    primes = sieve(int(input("Enter an integer: ")))
    print("\nThe primes are: ")

    for prime in primes:
        print(f'{prime}')
        i += 1

    print(f'\nTotal number of primes: {i}')


if __name__ == '__main__':
    main()