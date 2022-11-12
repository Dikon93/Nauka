krotka = (2, 4, 8, 16, 32, 64, 128)
print(krotka[0])
print(krotka)

# liczy ile elementów jest w tanym miejscu
print("Elementów: ", krotka.count(2))
# pokazuje ktory index ma dana wartość
print("Index: ", krotka.index(64))

print("\n Wycinki: ")
# utwórz kolekcje od 0 do 3 wartosci
print(krotka[0:3])
# utworzenie kolekcji od końca (z minusem)
print(krotka[-4:-1])
# skok wycinka x:y:z x- początkowy(moze być pusty bedzie od początku) y- końcowy(moze być pusty wiec bedzie do końca -z parametr skoku
print(krotka[::2])

# jesli z będzie na minusie to odwracamy kolejność
