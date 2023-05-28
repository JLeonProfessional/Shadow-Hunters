import unittest
from src.ClientMechanics import *
from src.Action import Action


class TestStringMethods(unittest.TestCase):

    def test_create_move_action(self):
        action = create_move_action()
        self.assertEqual(action["action"], Action.MOVE.value)

    def test_create_attack_action(self):
        action = create_attack_action(12)
        self.assertEqual(action["action"], Action.ATTACK.value)
        self.assertEqual(action["target"], 12)
        self.assertEqual(action["dice1"], 6)
        self.assertEqual(action["dice2"], 4)
