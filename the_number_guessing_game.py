import random

game_mode = {"easy_mode": 10, "hard_mode": 5}

print("I'm thinking of a number between 1 and 100.")

random_number = random.randint(1, 100)
print(random_number)


def easy_game():
    print(f"You have {game_mode["easy_mode"]} attempts remaining to guess the number.")

    if game_mode["easy_mode"] == 0:
        print("You loose")
    guess = int(input("Make a guess: "))
    if guess > random_number:
        print("Too high")
        game_mode["easy_mode"] -= 1
    elif guess == random_number:
        print("Correct.")
    else:
        print("Too low.")
        game_mode["easy_mode"] -= 1


def hard_game():
    print(f"You have {game_mode["hard_mode"]} attempts remaining to guess the number.")

    if game_mode["hard_mode"] == 0:
        print("You loose")
    guess = int(input("Make a guess: "))
    if guess > random_number:
        print("Too high")
        game_mode["hard_mode"] -= 1
    elif guess == random_number:
        print("Correct.")
    else:
        print("Too low.")
        game_mode["hard_mode"] -= 1


while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    match difficulty:
        case "easy":
            easy_game()
        case "hard":
            hard_game()
