def is_valid(isbn: str):
    isbn = isbn.replace('-', '')

    if len(isbn) != 10:
        return False

    digits = isbn[:-1]
    validator = isbn[-1]

    if not digits.isdigit() or (validator != 'X' and not validator.isdigit()):
        return False

    result = 0
    for i in range(0, 10):
        value = '10' if i == 9 and validator == 'X' else isbn[i]
        result += int(value) * (10 - i)

    return result % 11 == 0
