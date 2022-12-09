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


def value(colors: list[str]):
    color1, color2, *_ = colors

    return COLORS.index(color1) * 10 + COLORS.index(color2)
