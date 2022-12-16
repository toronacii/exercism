def is_triangle(callback):
    return lambda sides: sum(sides) > 2 * max(sides) and callback(sides)

@is_triangle
def equilateral(sides):
    return len(set(sides)) == 1

@is_triangle
def isosceles(sides):
    return len(set(sides)) < 3

@is_triangle
def scalene(sides):
    return len(set(sides)) == 3