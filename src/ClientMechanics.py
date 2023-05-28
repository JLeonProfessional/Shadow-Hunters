from src.Action import Action


def create_move_action():
    action_map = {
        "action": Action.MOVE.value
    }
    return action_map


def create_attack_action(player_id):
    action_map = {
        "action": Action.ATTACK.value,
        "target": player_id,
        "dice1": 6,
        "dice2": 4
    }
    return action_map