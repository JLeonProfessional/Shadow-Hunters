import unittest
from src.Client import *
from src.Action import Action


class TestStringMethods(unittest.TestCase):

    def test_create_move_action(self):
        action = create_move_action()
        self.assertEqual(action["action"], Action.MOVE)



