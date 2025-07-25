import random

DATA = {
    "Facebook": 55000000,
    "Disney": 41000000,
    "Telegram": 67000000,
    "Signal": 34000000,
    "Instagram": 49000000,
    "Google": 80000000,
    "Netflix": 32000000,
    "Apple": 43000000,
    "Amazon": 52000000,
    "YouTube": 60000000,
}

score = 0


while True:
    print(f"Actuall score: {score}")

    first_key = random.choice(list(DATA))
    print(f"Compare A: {first_key}: {DATA[first_key]}")

    second_key = random.choice(list(DATA))
    print(f"Compare B: {second_key}: {DATA[second_key]}")

    guess = input("Who has more Users? Type 'A' or 'B'").lower()

    is_a_correct = guess == "a" and DATA[first_key] > DATA[second_key]
    is_b_correct = guess == "b" and DATA[first_key] < DATA[second_key]

    if is_a_correct or is_b_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    elif DATA[first_key] == DATA[second_key]:
        print("Draw")
    else:
        print(f"Sorry that's wrong. Final score: {score}")
        score = 0
        break
    print("\n" * 2)
