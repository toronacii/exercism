OPERATIONS = ['jump', 'close your eyes', 'double blink', 'wink']


def commands(binary_str):

    result = []
    for index, char in enumerate(binary_str[1::]):
        if char == '1':
            result.insert(0, OPERATIONS[index])

    if (binary_str[0] == '1'):
        result.reverse()

    return result
