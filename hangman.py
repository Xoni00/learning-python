import random


word_list = [
    "gwóźdź",
    "ogień",
    "algorytm",
    "cisza",
    "grzyb",
    "kod",
    "próżnia",
    "błysk",
    "rytuał",
    "wiatrak",
    "chciwość",
    "świt",
    "rekurencja",
    "portal",
    "czaszka",
    "pokusa",
    "równowaga",
    "klątwa",
    "przestrzeń",
    "pamięć",
]

random_word = random.choice(word_list)
# ? print("".join(random_word))

#!zamiana liter na "_"
placeholder = []
for _ in random_word:
    placeholder += "_"
print(*placeholder)


life = 6
#! sprawdzanie czy litera jest w słowie
while life > 0:
    guess = str(input("guess a letter: "))
    if guess not in random_word:
        life -= 1
        print(f"źle, pozostało {life} żyć")
        print(*placeholder)
    else:
        for i in range(len(random_word)):
            if guess == random_word[i]:
                placeholder[i] = guess
        print("".join(placeholder))
    if "".join(placeholder) == random_word:
        print("wygrałeś")
        break
else:
    print(f"Przegrałeś zgadywane słowo to: {random_word} ")
