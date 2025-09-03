from cards import AVAILABLE_CARDS
import copy

import random


def cards(color, value, kind):
    card = {
        "color": color,
        "value": value,
        "kind": kind,
    }
    return card


deck = copy.deepcopy(AVAILABLE_CARDS)

players = []


def create_player(name):
    return {"name": name, "hand": []}


while True:

    random.shuffle(deck)

    qty_players = int(input("How many players? "))

    for name in range(qty_players):
        player_name = input(f"Player_{name + 1} name: ")
        players.append(create_player(player_name))

        for player in players:
            for card in range(7):
                player["hand"].append(deck[card])
                deck.pop(card)

    print(len(deck))

    break
