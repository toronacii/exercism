def yatch(dice): 
    return 50 if len(set(dice)) == 1 else 0

def repeated(number):
    def inner(dice):
        in_category = number in dice
        return sum(n for n in dice if n == number) if in_category else 0
    return inner

def fullhouse(dice):
    dice_set = set(dice)
    in_category = len(dice_set) == 2

    if not in_category:
        return 0

    a, b = dice_set 
    in_category = set([dice.count(a), dice.count(b)]) == set([2, 3])

    if not in_category:
        return 0

    return sum(dice)

def four_of_kind(dice):

    if fullhouse(dice):
        return 0

    dice_set = set(dice)
    in_category = len(dice_set) in [1, 2]

    if not in_category:
        return 0

    a, b = [*dice_set, 0] if len(dice_set) == 1 else dice_set

    if dice.count(a) >= 4:
        return 4 * a

    return 4 * b

def little_straight(dice):
    return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0

def big_straight(dice):
    return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0



# Score categories.
# Change the values as you see fit.
YACHT = yatch
ONES = repeated(1)
TWOS = repeated(2)
THREES = repeated(3)
FOURS = repeated(4)
FIVES = repeated(5)
SIXES = repeated(6)
FULL_HOUSE = fullhouse
FOUR_OF_A_KIND = four_of_kind
LITTLE_STRAIGHT = little_straight
BIG_STRAIGHT = big_straight
CHOICE = sum


def score(dice, category): return category(dice)
