from enum import Enum
from src.Location import Location


class Alignment(Enum):
    NEUTRAL = 0
    SHADOW = 1
    HUNTER = 2


class Player:
    location = Location.NONE.value[0]
    health = 0
    max_health = -1
    alignment = Alignment.NEUTRAL

    def __init__(self, max_health):
        self.max_health = max_health

    def calculate_damage(self, dice1, dice2):
        return abs(dice1 - dice2)

    def move_player(self, dice1, dice2):
        self.set_location(dice1 + dice2)

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_health(self):
        return self.health

    def set_health(self, health):
        self.health = health

    def get_max_health(self):
        return self.max_health

    def set_max_health(self, max_health):
        self.max_health = max_health

    def is_alive(self):
        return self.health < self.max_health





