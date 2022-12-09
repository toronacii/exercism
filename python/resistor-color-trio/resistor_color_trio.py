COLORS = [
    'black',
    'brown',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'grey',
    'white'
]


def get_total(colors: list[str]):
    color1, color2, color3 = colors
    base = 10 ** COLORS.index(color3)

    total = (COLORS.index(color1) * 10 + COLORS.index(color2)) * base
    return total


def label(colors: list[str]):
    total = get_total(colors)

    if (total < 1000):
        return f'{total} ohms'

    return f'{total // 1000} kiloohms'
