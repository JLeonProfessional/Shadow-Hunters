import socket
from src.StringHelper import *
from src.Action import Action


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 60010


def start_client():
    client.connect((host, port))


def receive():
    while True:
        try:
            message = decode(client.recv(1024))
        except:
            return False


def create_move_action():
    action_map = {
        "action": Action.MOVE
    }
    return action_map


def create_move_attack(player_id):
    action_map = {
        "action": Action.ATTACK,
        "target": player_id,
        "dice1": 6,
        "dice2": 4
    }
    return action_map


