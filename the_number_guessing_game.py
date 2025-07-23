import random

game_mode = {"easy_mode": 3, "hard_mode": 5}

print("I'm thinking of a number between 1 and 100.")

random_number = random.randint(1, 100)
print(random_number)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


# def easy_mode():
# guess = int(input("Make a guess: "))
# if guess > random_number:
#     print("Too high")
#     game_mode["easy_mode"] -= 1
# elif guess == random_number:
#     print("Correct.")
#     exit
# else:
#     print("Too low.")
# if game_mode["easy_mode"] == 0:
#     print("You loose")
#     exit


while True:
    print(f"You have {game_mode["easy_mode"]} attempts remaining to guess the number.")

    if game_mode["easy_mode"] == 0:
        print("You loose")
        break

    guess = int(input("Make a guess: "))
    if guess > random_number:
        print("Too high")
        game_mode["easy_mode"] -= 1
    elif guess == random_number:
        print("Correct.")
        break
    else:
        print("Too low.")
        game_mode["easy_mode"] -= 1
