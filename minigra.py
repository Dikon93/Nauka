from random import randint
# losowanie przypadkowej liczby
# for i in range(100):
#    print(randint(1, 10))

los = randint(1, 10)
odp = -1
i = 0
print("Zgadnij liczbę z przedziału 1-10")

while odp != los:
    i += 1
    odp = int(input("Podaj liczbę: "))
    if odp > los:
        print("Wylosowana liczba jest mniejsza od Twojej")
    elif odp < los:
        print("Wylosowana liczba jest wieksza od twojej")
print("Brawo! Odgadłes za", i, "razem")
