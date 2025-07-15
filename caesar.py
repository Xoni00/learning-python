letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']




def caesar():
    if selection == 'encode':
        encode()
    else:
        decode()


def encode():
    coded_phrase = ''
    for character in phrase:
        letters.index(character)
        if character != ' ':
            a = (letters.index(character) + shift_number) % 26
            coded_phrase += letters[a]
    
    print(f"Here's the encoded results: {coded_phrase}")
    

        
    
def decode():
    coded_phrase = ''
    
    for i in phrase:
        letters.index(i)
        a = (letters.index(i) - shift_number) % 26
        coded_phrase += letters[a]
    
    print(f"Here's the decoded results: {coded_phrase}")
    
loop = True

while loop:
    selection = input("type 'encode' to encrypt, type 'decode' to decrypt: ")

    phrase = input("type your message: \n").lower()

    shift_number = int(input("Type shift number: \n"))
    caesar()
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no' ")
    if restart == 'no':
        loop = False

#! lista słow
#! potrzebujemy randomizacje -> import random 
#! wypluwa nam randomowe słowa w postaci _ _ _ _ _ ...
#! pokazuje ilosc żyć
#! pobiera litere od użytkownika i sprawdza czy litera jest w słowie
#! jesli tak zamienia _ na litere jesli nie odejmuje nam 1 życie 
#! po straceniu zyc konczymy gre. jesli zgadniemy wszystkie litery wygrywamy 







#! mamy talie 52 kart podzielona na różne numery, akcje i 4 kolory
#! kazdy gracz musi dostac 5 kart
#! pierwsza karta na stole idzie z talii na stole 
#! gracze dostaja karty z góry przetasowanej talii -> 
