import random

game_mode = {"easy_mode": 10, "hard_mode": 5}

print("I'm thinking of a number between 1 and 100.")

random_number = random.randint(1, 100)
print(random_number)

game = True


def easy_game():
    global game

    print(f"You have {game_mode["easy_mode"]} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if game_mode["easy_mode"] == 0:
        print("You loose")
        game = False
    elif guess > random_number:
        print("Too high")
        game_mode["easy_mode"] -= 1
    elif guess == random_number:
        print("Correct.")
        game = False
    else:
        print("Too low.")
        game_mode["easy_mode"] -= 1


def hard_game():
    global game
    print(f"You have {game_mode["hard_mode"]} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if game_mode["hard_mode"] <= 0:
        print("You loose")
        game = False
    elif guess > random_number:
        print("Too high")
        game_mode["hard_mode"] -= 1
    elif guess == random_number:
        print("Correct.")
        game = False
    else:
        print("Too low.")
        game_mode["hard_mode"] -= 1


difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

while game:

    match difficulty:
        case "easy":
            easy_game()
        case "hard":
            hard_game()
        case _:
            print("error")
            break
