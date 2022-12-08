def get_aliquot(number: int):

    if number == 1:
        return 0

    aliquot = 1
    to = number // 2 + 1

    for divisor in range(2, to):
        if number % divisor == 0:
            aliquot += divisor

    return aliquot


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError(
            "Classification is only possible for positive integers.")

    aliquot = get_aliquot(number)

    if aliquot < number:
        return 'deficient'
    if aliquot == number:
        return 'perfect'

    return 'abundant'
