from enum import Enum


class Alignment(Enum):
    NEUTRAL = 0
    SHADOW = 1
    HUNTER = 2


class Player:
    location = 0
    health = 0
    alignment = Alignment.NEUTRAL

    def __init__(self, health):
        self.health = health

    def calculate_damage(self, dice1, dice2):
        return abs(dice1 - dice2)

    def move_player(self, dice1, dice2):
        self.set_location(dice1 + dice2)

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_health(self):
        return self.location

    def set_health(self, location):
        self.location = location






