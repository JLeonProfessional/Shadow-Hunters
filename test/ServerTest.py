from src.Server import *
import unittest


class PlayerTest(unittest.TestCase):

    def test_calculate_damage(self):
        self.assertTrue(0 < roll_dice(6) < 7, 'Dice did not roll correctly')
        self.assertTrue(0 < roll_dice(4) < 5, 'Dice did not roll correctly')



