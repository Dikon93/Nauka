plik = open("analiza_tekstu.txt", "r")
tekst = plik.read()
plik.close()


def policz(txt, znak):
    licznik = 0
    for z in txt:
        if z == znak:
            licznik += 1
    return licznik


print(policz(tekst, "a") + policz(tekst, "A"))
print(policz(tekst.lower(), "a"))

for z in "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż":
    ile = policz(tekst.lower(), z)
    procent = 100 * ile / len(tekst)
    print("{0} - {1}- {2} %".format(z.upper(), ile, round(procent, 2)))
