from src.Player import *
import unittest


class PlayerTest(unittest.TestCase):

    def test_calculate_damage(self):
        player = Player()
        damage = player.calculate_damage(6, 4)
        self.assertEqual(2, damage)

        damage = player.calculate_damage(3, 3)
        self.assertEqual(0, damage)

        damage = player.calculate_damage(1, 4)
        self.assertEqual(3, damage)



