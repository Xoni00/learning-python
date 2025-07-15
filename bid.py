auction = {}
print("Welcome to the secret auction program.")


def auction_game():
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: "))
    auction[name] = bid


game = True

while game:
    auction_game()
    decision = input("Are there other biders? Type 'yes' or 'no'\n")
    if decision == "yes":
        print("\n")
    else:
        game = False


max_key = max(auction, key=auction.get)
max_value = auction[max_key]

print(f"The winner is {max_key} with the bid of ${max_value}")
