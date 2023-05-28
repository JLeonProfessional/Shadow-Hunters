import json
import socket
import threading
from ClientMechanics import *

from src.StringHelper import *


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 60010

username = ""
user_id = 12

def start_client():
    client.connect((host, port))
    user_information_map = {
        "player_id": 12
    }
    message_json = json.dumps(user_information_map)
    print(message_json)
    client.sendall(bytes(message_json, encoding="utf-8"))


def receive():
    while True:
        try:
            message = decode(client.recv(1024))
        except:
            return False


def write():
    while True:
        choice = input("action")
        action_map = {}
        if choice == "move":
            action_map = create_move_action()
        elif choice == "attack":
            action_map = create_attack_action(12)
        message_json = json.dumps(action_map)
        print(message_json)
        client.sendall(bytes(message_json, encoding="utf-8"))


start_client()

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()


