def rebase(input_base, digits, output_base):

    if input_base < 2:
        raise ValueError('input base must be >= 2')

    if output_base < 2:
        raise ValueError('output base must be >= 2')

    if not all(d in range(0, input_base) for d in digits):
        raise ValueError('all digits must satisfy 0 <= d < input base')

    base_10 = to_base_10(input_base, digits)

    if base_10 == 0:
        return [0]

    result = to_base(base_10, output_base)
    return result


def to_base_10(input_base, digits):
    return sum(
        digit * input_base ** (len(digits) - i - 1)
        for i, digit in enumerate(digits)
    )


def to_base(number: int, base: int):
    result = []
    while (number > 0):
        result.insert(0, number % base)
        number = number // base
    return result
