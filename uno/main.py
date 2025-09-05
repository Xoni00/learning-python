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

random.shuffle(deck)

players = []

table = []


def create_player(name):
    return {"name": name, "hand": []}


def start_table():
    for card in deck:
        if card["type"] == "number":
            table.append(card)
            break
        else:
            first_card = deck.pop(0)
            deck.append(first_card)
    print(create_formatted_card(table[0]))


def create_formatted_card(card):
    return f"{card["color"].capitalize()} {card["value"]}"


random.shuffle(deck)

qty_players = int(input("How many players? "))

for name in range(qty_players):
    player_name = input(f"Player_{name + 1} name: ")
    players.append(create_player(player_name))

    for player in players:
        for card in range(7):
            player["hand"].append(deck[card])
            deck.pop(card)

start_table()


#! podzielic widok graczy, funkcja na wyciaganie kart i rzucanie ich do table potem stworzenie logiki gry
