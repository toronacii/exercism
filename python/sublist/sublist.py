"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
UNEQUAL = 'UNEQUAL'
EQUAL = 'EQUAL'
SUPERLIST = 'SUPERLIST'
SUBLIST = 'SUBLIST'


def sublist(list_one: list[int], list_two: list[int]):
    if list_one == list_two:
        return EQUAL

    if is_superlist(list_one, list_two):
        return SUPERLIST

    if is_superlist(list_two, list_one):
        return SUBLIST

    return UNEQUAL


def is_superlist(list_one: list[int], list_two: list[int]):
    for i in range(len(list_one) - len(list_two) + 1):
        if not list_two or list_two == list_one[i: i + len(list_two)]:
            return True
    return False
