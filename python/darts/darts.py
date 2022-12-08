INNER = (1, 10)
MIDDLE = (5, 5)
OUTER = (10, 1)


def score(x: float, y: float):
    d = (x ** 2 + y ** 2) ** 0.5

    return next((
        score
        for radius, score in [INNER, MIDDLE, OUTER]
        if d <= radius
    ), 0)
