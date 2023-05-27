import random
from src.Player import Player
from src.Location import Location
from src.Action import Action

location1 = []
location2 = []
location3 = []
players = []


def initialize_game(number_of_players):
    for player in range(0, number_of_players):
        players.append(Player(10))
    place_locations()


def place_locations():
    unplaced_locations = [
        Location.GREEN,
        Location.PURPLE,
        Location.WHITE,
        Location.BLACK,
        Location.WOODS,
        Location.ALTAR,
    ]

    location1.append(unplaced_locations.pop(random.randint(0, 5)))
    location1.append(unplaced_locations.pop(random.randint(0, 4)))
    location2.append(unplaced_locations.pop(random.randint(0, 3)))
    location2.append(unplaced_locations.pop(random.randint(0, 2)))
    location3.append(unplaced_locations.pop(random.randint(0, 1)))
    location3.append(unplaced_locations.pop(0))


def roll_dice(dice_sides):
    return random.randint(1, dice_sides)


def get_local_locations(location):
    local_locations = []
    for card in location:
        for value in card.value:
            local_locations.append(value)
    return local_locations


def do_combat(attacking_player, defending_player, damage):
    if valid_target(attacking_player, defending_player):
        defending_player.set_health(defending_player.get_health() + damage)


def valid_target(player1, player2):
    """
    :param player1
    :type player1: Player
    :param player2
    :type player2: Player
    """
    valid_locations1 = get_local_locations(location1)
    valid_locations2 = get_local_locations(location2)
    valid_locations3 = get_local_locations(location3)

    current_location = player1.get_location()
    if current_location in valid_locations1:
        return player2.get_location() in valid_locations1
    if current_location in valid_locations2:
        return player2.get_location() in valid_locations2
    if current_location in valid_locations3:
        return player2.get_location() in valid_locations3


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





