import random

SCORE_LIMIT = 21

deck = [
    "2",
    # "3",
    # "4",
    # "5",
    # "6",
    # "7",
    # "8",
    # "9",
    # "10",
    # "J",
    # "Q",
    # "K",
    "A",
]

CARD_SCORE = {
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
    "A1": 1,
    "A11": 11,  # As może mieć 1 lub 11
}


def result():
    if another_card == "n" and card_score > computer_card_score:
        print(f"Your final hand: {player_cards}, final score: {card_score}")
        print(
            f"Computer's final hand: {computer_cards}, final score: {computer_card_score}"
        )
        print("You win")
    elif card_score == computer_card_score:
        print(f"Your final hand: {player_cards}, final score: {card_score}")
        print(
            f"Computer's final hand: {computer_cards}, final score: {computer_card_score}"
        )
        print("draw")
    elif computer_card_score == 21:
        print(f"Your final hand: {player_cards}, final score: {card_score}")
        print(
            f"Computer's final hand: {computer_cards}, final score: {computer_card_score}"
        )
        print("Computer has a Blackjack, You loose")
    else:
        print(f"Your final hand: {player_cards}, final score: {card_score}")
        print(
            f"Computer's final hand: {computer_cards}, final score: {computer_card_score}"
        )
        print("You loose")


#! jesli krupier ma mniej niz 17 pkt w kartach musi ciagnac kolejna karte
decision = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if decision != "y":
    exit

#! player first cards
player_cards = []

for idx in range(2):
    random_card = random.choice(deck)
    if random_card == "A":
        match input("As 1 or 11?"):
            case "1":
                player_cards.append("A1")
            case "11":
                player_cards.append("A11")
            case _:
                print("error")
        # player_cards.append(random_card)


#! Computer cards and cards score
computer_cards = []
for idx in range(2):
    computer_cards.append(random.choice(deck))

computer_card_score = 0

for card in computer_cards:
    computer_card_score += CARD_SCORE.get(card)

while True:
    #! player cards score

    card_score = 0

    for card in player_cards:
        card_score += CARD_SCORE.get(card)

    if card_score > SCORE_LIMIT:
        print(f"Your final hand: {player_cards}, final score: {card_score}")
        print(
            f"Computer's final hand: {computer_cards}, final score: {computer_card_score}"
        )
        print("You went over. You loose")
        break

    print(f"Your cards: {player_cards}, current score: {card_score}")

    if computer_card_score == SCORE_LIMIT:
        print(
            f"Computer's have a BlackJack!{computer_cards}, score: {computer_card_score}"
        )
    else:
        print(f"Computer`s first card: {computer_cards[0]}")

    #! draw another card
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    if another_card == "y" and card_score < SCORE_LIMIT:
        player_cards.append(random.choice(deck))
    else:
        result()
        break
