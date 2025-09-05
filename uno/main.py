from cards import AVAILABLE_CARDS
import copy

import random


deck = copy.deepcopy(AVAILABLE_CARDS)
random.shuffle(deck)

players = []
table = []


def create_card(color, value, kind):
    return {
        "color": color,
        "value": value,
        "kind": kind,
    }


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


def print_table():
    formatted_cards = []

    for card in table:
        formatted_cards.append(create_formatted_card(card))

    print(",".join(formatted_cards))


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
print_table()


#! podzielic widok graczy, funkcja na wyciaganie kart i rzucanie ich do table potem stworzenie logiki gry
