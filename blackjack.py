import random

card_list = [
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K",
] * 4

cards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": [1, 11],  # As może mieć 1 lub 11
}
#! jesli krupier ma mniej niz 17 pkt w kartach musi ciagnac kolejna karte

# while True:

#     decision = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
#     if decision != "y":
#         break

player_cards = []

for _ in range(2):
    player_cards += random.choice(card_list)

card_score = 0

for card in player_cards:
    card_score += cards.get(card)

computer_firs_card = random.choice(card_list)

print(f"Your cards: {player_cards}, current score: {card_score}")
print(f"Computer`s first card: {computer_firs_card}")

another_card = input("Type 'y' to get another card, type 'n' to pass: ")

if another_card == "y":
    player_cards.append(random.choice(card_list))
else:
    print(f"Your final hand: {player_cards}, final score: {card_score}")
    print()
