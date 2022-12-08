def get_aliquot(number: int):
    if number <= 0:
        raise ValueError(
            "Classification is only possible for positive integers.")

    return sum(
        divisor
        for divisor in range(1, number // 2 + 1)
        if number % divisor == 0
    )


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    aliquot = get_aliquot(number)

    if aliquot < number:
        return 'deficient'
    if aliquot == number:
        return 'perfect'

    return 'abundant'
