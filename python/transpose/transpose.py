def transpose(lines: str):
    _lines = lines.split('\n')

    if len(_lines) < 2:
        return '\n'.join(lines)

    lines = []

    i = 0
    while (True):
        line = ''

        with_char = False
        virtual_spaces = 0

        for word in _lines:
            if i >= len(word):
                virtual_spaces += 1
            else:
                line += virtual_spaces * ' ' + word[i]
                virtual_spaces = 0
                with_char = True

        if not with_char:
            break

        lines.append(line)
        i += 1

    return '\n'.join(lines)
