def append(list1, list2):
    list1 += list2
    return list1


def concat(lists):
    return foldl(
        lambda r, l: r + l,
        lists,
        []
    )


def filter(function, list):
    return [
        item
        for item in list
        if function(item)
    ]


def length(list: list):
    return sum(1 for _ in list)


def map(function, list):
    return [
        function(item)
        for item in list
    ]


def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial


def foldr(function, list, initial):
    for item in list[::-1]:
        initial = function(item, initial)
    return initial


def reverse(list):
    return list[::-1]
