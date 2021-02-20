def how_many_different_numbers(numbers):
    # Invokes set on numbers, thus returning a set with the unique
    # elements from numbers
    unique_numbers = set(numbers)
    return len(unique_numbers)


print(how_many_different_numbers([1, 2, 3, 1, 2, 3, 4, 1]))