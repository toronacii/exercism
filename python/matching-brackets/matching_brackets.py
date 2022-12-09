SYMBOLS = {
    '[': ']',
    '{': '}',
    '(': ')',
}


def is_paired(input_string):
    next_close = ''
    stack = []
    open_symbols = list(SYMBOLS.keys())
    close_symbols = list(SYMBOLS.values())

    chars = [char for char in input_string if char in open_symbols + close_symbols]

    for char in chars:
        if char in open_symbols:
            stack.insert(0, char)
            next_close = SYMBOLS[char]

        else:
            if char != next_close:
                return False

            stack.pop(0)
            next_close = '' if len(stack) == 0 else SYMBOLS[stack[0]]

    return len(stack) == 0
