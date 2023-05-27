from src.Server import *
from src.Player import *
from src.Location import Location
from src.Action import Action
import unittest


class PlayerTest(unittest.TestCase):

    def tearDown(self) -> None:
        location1.clear()
        location2.clear()
        location3.clear()
        players.clear()

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

    def test_valid_target_middle(self):
        location1.append(Location.GREEN)
        location1.append(Location.PURPLE)

        location2.append(Location.WHITE)
        location2.append(Location.BLACK)

        location3.append(Location.WOODS)
        location3.append(Location.ALTAR)

        player1 = Player(10)
        player1.set_location(Location.GREEN.value[0])

        player2 = Player(10)
        player2.set_location(Location.NONE.value[0])

        self.assertFalse(valid_target(player1, player2))
        self.assertFalse(valid_target(player2, player1))

    def test_combat_simulation_must_be_valid(self):
        player1 = Player(10)
        player2 = Player(10)

        do_combat(player1, player2, 2)

        self.assertEqual(0, player2.get_health())
        self.assertTrue(player2.is_alive())

        location1.append(Location.GREEN)
        location1.append(Location.PURPLE)
        player1.set_location(Location.GREEN.value[0])
        player2.set_location(Location.PURPLE.value[0])

        do_combat(player1, player2, 2)

        self.assertEqual(2, player2.get_health())
        self.assertTrue(player2.is_alive())

        do_combat(player1, player2, 8)

        self.assertEqual(10, player2.get_health())
        self.assertFalse(player2.is_alive())

    def test_initialize_game(self):
        initialize_game(2)

        self.assertEqual(2, len(players))
        player1 = players[0]
        self.assertEqual(-1, player1.get_location())
        self.assertEqual(0, player1.get_health())
        self.assertEqual(10, player1.get_max_health())

        player2 = players[1]
        self.assertEqual(-1, player2.get_location())
        self.assertEqual(0, player2.get_health())
        self.assertEqual(10, player2.get_max_health())

        self.assertTrue(Location.GREEN in location1 or Location.GREEN in location2 or Location.GREEN in location3)
        self.assertTrue(Location.PURPLE in location1 or Location.PURPLE in location2 or Location.PURPLE in location3)
        self.assertTrue(Location.WHITE in location1 or Location.WHITE in location2 or Location.WHITE in location3)
        self.assertTrue(Location.BLACK in location1 or Location.BLACK in location2 or Location.BLACK in location3)
        self.assertTrue(Location.WOODS in location1 or Location.WOODS in location2 or Location.WOODS in location3)
        self.assertTrue(Location.GREEN in location1 or Location.GREEN in location2 or Location.GREEN in location3)

    def test_handle_client_action_move(self):
        player = Player(10)

        action_map = {
            "action": Action.MOVE
        }
        handle_client_action(action_map, player)
        self.assertTrue(player.get_location() != Location.NONE.value[0])

    def test_handle_client_action_attack(self):

        place_locations()
        player = Player(10)
        player.set_player_id(0)
        player.set_location(Location.GREEN.value[0])

        player2 = Player(10)
        player2.set_player_id(1)
        player2.set_location(Location.GREEN.value[0])

        players.append(player)
        players.append(player2)
        action_map = {
            "action": Action.ATTACK,
            "target": player2.get_player_id(),
            "dice1": 6,
            "dice2": 4
        }
        handle_client_action(action_map, player)
        self.assertTrue(player.get_location() != Location.NONE.value[0])
        self.assertTrue(player2.get_health() > 0)

