from src.Server import handle_client_action, receive_client_information, players, user_id_client_map, receive_message, \
    clients, user_ids
import socket
import json
from src.Action import Action
from src.Player import Player
from src.GameMechanics import place_locations
from src.Location import *
from src.StringHelper import *
import unittest


class PlayerTest(unittest.TestCase):

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

    def test_receive_client_information(self):
        user_information_map = {
            "player_id": 12
        }
        json_dump = encode(json.dumps(user_information_map))
        client = socket.socket
        receive_client_information(client, json_dump)
        self.assertEqual(1, len(clients))
        self.assertEqual(1, len(user_id_client_map))
        self.assertEqual(client, user_id_client_map[12])
        self.assertEqual(1, len(user_ids))
        self.assertEqual(12, user_ids[0])

    def test_receive_message(self):
        action_map = {
            "action": Action.ATTACK.value,
            "target": 12,
            "dice1": 6,
            "dice2": 4
        }
        dump_json = json.dumps(action_map)
        incoming_json = bytes(dump_json, encoding="utf-8")

        decoded_map = receive_message(incoming_json)
        self.assertTrue(Action.ATTACK, decoded_map["action"])
        self.assertTrue(12, decoded_map["target"])
        self.assertTrue(6, decoded_map["dice1"])
        self.assertTrue(4, decoded_map["dice2"])



