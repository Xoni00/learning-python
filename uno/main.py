from cards import AVAILABLE_CARDS

import random

COLORS = ["red", "yellow", "green", "blue", "black"]


def cards(color, value, kind):
    card = {
        "color": color,
        "value": value,
        "kind": kind,
    }
    return card


deck = []


#! number zero cards
deck.append(cards("red", 0, None))
deck.append(cards("yellow", 0, None))
deck.append(cards("green", 0, None))
deck.append(cards("blue", 0, None))

#! 1-9 cards
for i in range(1, 10):
    for _ in range(2):
        deck.append(cards("red", i, None))
        deck.append(cards("yellow", i, None))
        deck.append(cards("green", i, None))
        deck.append(cards("blue", i, None))

#! stop cards
for i in range(2):
    deck.append(cards("red", None, "stop"))
    deck.append(cards("yellow", None, "stop"))
    deck.append(cards("green", None, "stop"))
    deck.append(cards("blue", None, "stop"))

#! change direction icards
for i in range(2):
    deck.append(cards("red", None, "change_direction"))
    deck.append(cards("yellow", None, "change_direction"))
    deck.append(cards("green", None, "change_direction"))
    deck.append(cards("blue", None, "change_direction"))

#! +2 cards
for i in range(2):
    deck.append(cards("red", None, "+2"))
    deck.append(cards("yellow", None, "+2"))
    deck.append(cards("green", None, "+2"))
    deck.append(cards("blue", None, "+2"))

#! +4 cards
deck.append(cards("red", None, "+4"))
deck.append(cards("yellow", None, "+4"))
deck.append(cards("green", None, "+4"))
deck.append(cards("blue", None, "+4"))

#! change color cards
deck.append(cards("red", None, "change_color"))
deck.append(cards("yellow", None, "change_color"))
deck.append(cards("green", None, "change_color"))
deck.append(cards("blue", None, "change_color"))

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
                deck.pop(i)

    # if card["value"] is not None:
    #     return f"{card["color"].capitalize()} {card["value"]}"
    # else:
    #     return f"{card["color"].capitalize()} {card["kind"]}"
    break
