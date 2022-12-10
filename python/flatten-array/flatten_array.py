def flatten(iterable: list):
    return list(__flatten(iterable))


def __flatten(iterable):
    for item in iterable:
        if __is_iterable(item):
            yield from __flatten(item)
        elif item is not None:
            yield item


def __is_iterable(item):
    return isinstance(item, (list, tuple))
