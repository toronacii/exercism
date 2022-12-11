def annotate(minefield: list[str]):
    # Function body starts here
    _minefield = __get_valid_minefield(minefield)

    for i, j, mines in __get_items(minefield):
        row = _minefield[i]
        _minefield[i] = f'{row[:j]}{mines}{row[j + 1:]}'

    return _minefield


def __get_valid_minefield(minefield: list[str]):
    for row in minefield:

        invalid_len = len(row) != len(minefield[0])
        invalid_chars = row.replace('*', '').strip() != ''

        if invalid_len or invalid_chars:
            raise ValueError('The board is invalid with current input.')

    return minefield.copy()


def __get_items(minefield: list[str]):
    for i, _ in enumerate(minefield):
        for j, letter in enumerate(minefield[i]):
            if letter == ' ':
                mines = len([
                    item for item in __get_neighbours(minefield, i, j)
                    if item == '*'
                ])

                if mines > 0:
                    yield i, j, mines


def __get_neighbours(minefield: list[str], i: int, j: int):
    for _i, _j in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        x = _i + i
        y = _j + j

        if x >= 0 and x < len(minefield) and y >= 0 and y < len(minefield[0]):
            yield minefield[x][y]
