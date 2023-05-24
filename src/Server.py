import random
from enum import Enum


class Location(Enum):
    GREEN = [2, 3]
    PURPLE = [4,5]
    WHITE = [6]
    BLACK = [8]
    WOODS = [9]
    ALTAR = [10]


def roll_dice(dice_sides):
    return random.randint(1, dice_sides)








