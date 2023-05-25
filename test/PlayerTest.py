from src.Player import *
from src.Location import Location
import unittest


class PlayerTest(unittest.TestCase):

    def test_calculate_damage(self):
        player = Player(10)
        damage = player.calculate_damage(6, 4)
        self.assertEqual(2, damage)

        damage = player.calculate_damage(3, 3)
        self.assertEqual(0, damage)

        damage = player.calculate_damage(1, 4)
        self.assertEqual(3, damage)

    def test_move_player(self):
        player = Player(10)
        player.move_player(1, 1)
        self.assertTrue(player.get_location() in Location.GREEN.value)

        player.move_player(2, 1)
        self.assertTrue(player.get_location() in Location.GREEN.value)

        player.move_player(2, 2)
        self.assertTrue(player.get_location() in Location.PURPLE.value)

        player.move_player(2, 3)
        self.assertTrue(player.get_location() in Location.PURPLE.value)

        player.move_player(3, 3)
        self.assertTrue(player.get_location() in Location.WHITE.value)

        player.move_player(5, 3)
        self.assertTrue(player.get_location() in Location.BLACK.value)

        player.move_player(5, 4)
        self.assertTrue(player.get_location() in Location.WOODS.value)

        player.move_player(6, 4)
        self.assertTrue(player.get_location() in Location.ALTAR.value)



