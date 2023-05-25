from src.Server import *
from src.Player import *
from src.Location import Location
import unittest


class PlayerTest(unittest.TestCase):

    def test_calculate_damage(self):
        self.assertTrue(0 < roll_dice(6) < 7, 'Dice did not roll correctly')
        self.assertTrue(0 < roll_dice(4) < 5, 'Dice did not roll correctly')

    def test_place_locations(self):
        self.assertFalse(Location.GREEN in location1 or Location.GREEN in location2 or Location.GREEN in location3)
        self.assertFalse(Location.PURPLE in location1 or Location.PURPLE in location2 or Location.PURPLE in location3)
        self.assertFalse(Location.WHITE in location1 or Location.WHITE in location2 or Location.WHITE in location3)
        self.assertFalse(Location.BLACK in location1 or Location.BLACK in location2 or Location.BLACK in location3)
        self.assertFalse(Location.WOODS in location1 or Location.WOODS in location2 or Location.WOODS in location3)
        self.assertFalse(Location.GREEN in location1 or Location.GREEN in location2 or Location.GREEN in location3)

        place_locations()

        self.assertTrue(Location.GREEN in location1 or Location.GREEN in location2 or Location.GREEN in location3)
        self.assertTrue(Location.PURPLE in location1 or Location.PURPLE in location2 or Location.PURPLE in location3)
        self.assertTrue(Location.WHITE in location1 or Location.WHITE in location2 or Location.WHITE in location3)
        self.assertTrue(Location.BLACK in location1 or Location.BLACK in location2 or Location.BLACK in location3)
        self.assertTrue(Location.WOODS in location1 or Location.WOODS in location2 or Location.WOODS in location3)
        self.assertTrue(Location.GREEN in location1 or Location.GREEN in location2 or Location.GREEN in location3)

        location1.clear()
        location2.clear()
        location3.clear()

    def test_get_local_locations(self):
        test_location = [Location.GREEN, Location.PURPLE]
        self.assertEqual([2,3,4,5], get_local_locations(test_location))

        test_location2 = [Location.WHITE, Location.BLACK]
        self.assertEqual([6,8], get_local_locations(test_location2))

    def test_valid_target(self):

        location1.append(Location.GREEN)
        location1.append(Location.PURPLE)

        location2.append(Location.WHITE)
        location2.append(Location.BLACK)

        location3.append(Location.WOODS)
        location3.append(Location.ALTAR)

        player1 = Player(10)
        player1.set_location(Location.GREEN.value[0])

        player2 = Player(10)
        player2.set_location(Location.GREEN.value[1])

        self.assertTrue(valid_target(player1, player2))

        player2.set_location(Location.PURPLE.value[0])
        self.assertTrue(valid_target(player1, player2))

        player3 = Player(10)
        player3.set_location(Location.WHITE.value[0])
        self.assertFalse(valid_target(player1, player3))

        player1.set_location(Location.WHITE.value[0])
        player2.set_location(Location.WHITE.value[0])
        self.assertTrue(valid_target(player1, player2))

        player1.set_location(Location.WOODS.value[0])
        player2.set_location(Location.WOODS.value[0])
        self.assertTrue(valid_target(player1, player2))

        location1.clear()
        location2.clear()
        location3.clear()

