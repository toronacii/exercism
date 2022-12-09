def is_palindrome(number: int):
    string = str(number)
    return string == string[::-1]


def factors(palindrome: int, min: int, max: int):
    pairs = set()
    for number in range(min, max + 1):
        res, rem = divmod(palindrome, number)
        if rem == 0 and (min <= res <= max):
            pairs.add((number, res))
    return pairs


def palindrome_factors(min: int, max: int, products_range: list[int]):
    pairs = set()
    for number in products_range:
        if is_palindrome(number):
            pairs = factors(number, min, max)
            if pairs:
                return number, pairs
    return None, pairs


def validate(min: int, max: int):
    if min > max:
        raise ValueError("min must be <= max")


def largest(max_factor: int, min_factor=0):
    validate(min_factor, max_factor)
    start = max_factor ** 2
    stop = min_factor ** 2 - 1
    products_range = range(start, stop, -1)
    return palindrome_factors(min_factor, max_factor, products_range)


def smallest(max_factor, min_factor=0):
    validate(min_factor, max_factor)
    start = min_factor ** 2
    stop = max_factor ** 2
    products_range = range(start, stop)
    return palindrome_factors(min_factor, max_factor, products_range)
