def is_armstrong_number(number):
    digits = decompose(number)
    exp = len(digits)

    return number == sum(digit ** exp for digit in digits)

def decompose(number):
    digits = []
    while number:
        digits = [number % 10] + digits
        number //= 10
    return digits
