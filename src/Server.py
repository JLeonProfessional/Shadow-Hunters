import socket
from src.Action import Action
from src.StringHelper import *
import json
from src.GameMechanics import *


clients = []
user_ids = []
user_id_client_map = {}


host = '127.0.0.1'
port = 60010

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()





def handle_client_action(action_map, player):
    action = action_map["action"]
    if action == Action.MOVE:
        player.move_player(roll_dice(6), roll_dice(4))
    if action == Action.ATTACK:
        damage = player.calculate_damage(action_map["dice1"], action_map["dice2"])
        target_id = action_map["target"]
        target = None
        for potential_target in range(0, len(players)):
            if players[potential_target].get_player_id() == target_id:
                target = players[potential_target]
        do_combat(player, target, damage)


def receive_client_information(client, information_map):
    actual_map = receive_message(information_map)
    player_id = actual_map["player_id"]
    user_ids.append(player_id)
    user_id_client_map[player_id] = client
    clients.append(client)


def receive_message(message):
    received_message = decode(message)
    message_data = json.loads(received_message)
    return message_data


# def receive_messages_from_client(client):
#     while True:
#         try:
#             message = client.recv(1024)
#             json = recieve_message_as_json(client)
#             print(string_message)
#             broadcastSentMessage(encode(string_message), client)
#         except:
#             handle_exception(client)
#             break

def catch_clients():
    while True:
        client, address = server.accept()
        print(f'New connection from {address}')
        receive_client_information(client, client.recv(1024))


print("Server started")
# catch_clients()


