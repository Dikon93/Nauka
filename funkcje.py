def funkcja_test():
    print("Funkcja...")


funkcja_test()


def dodaj(x):
    print(x+1)


dodaj(2)


def dodaj(x, y=1):
    # jak dasz y=1 to domyslnie jest jeden chyba ze podasz inny
    print(x+y)


dodaj(2, 5)
# pamietać zeby nie przeciązyć funkcji
dodaj(2)

# zamiast print mozna uzyć return i wtedy mozna to wyrzucic poza funkcje bez pokazywania w konsoli
