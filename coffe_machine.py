machine_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

COFFESS = {
    "espresso": {
        "water": 50,
        "coffee": 18,
        "cost": 1.50,
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "cost": 2.50,
    },
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.00},
}

coffee = input("What would you like? (espresso/latte/cappuccino): ")

if coffee == "off":
    exit()
elif coffee == "report":
    for key, value in machine_resources.items():
        print(f"{key} - {value} ml")
    exit()

coffee_type = COFFESS.get(coffee)

coffee_ingredients = []

for key in coffee_type:
    if key == "cost":
        continue
    elif machine_resources[key] >= COFFESS[coffee][key]:
        pass
    else:
        print(f"Sorry there is not enough {key}")
        exit()

#!add coins
dziesieciogroszowka = int(input("Ile dziesięciogroszówek?"))
dwudziestogroszowka = int(input("Ile dwudziestogroszówek?"))
piedziesieciogroszowka = int(input("Ile piędziesięciogroszówek?"))
zlotowka = int(input("Ile złotówek?"))

pln = {
    "0.10": int(input("Ile dziesięciogroszówek?")),
    "0.20": int(input("Ile dwudziestogroszówek?")),
    "0.50": int(input("Ile piędziesięciogroszówek?")),
    "1": int(input("Ile złotówek?")),
}

pln_total = pln["0.10"] * 0.1 + pln["0.20"] * 0.2 + pln["0.50"] * 0.5 + pln["1"] * 1

machine_resources["money"] = pln_total

#!check money
if pln_total < COFFESS[coffee]["cost"]:
    print(f"Sorry that`s not enough money. {round(pln_total,2)} was refunded ")
