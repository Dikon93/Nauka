print("Kolejność: ")
# używamy tylko nawiasów okrągłych
print((2+2)*2)

print("\nDzielenie: ")
print(5/2)

# dzielenie - liczba całkowita tylko
print(5//2)

print("\nMnożenie: ")
print(2*3)

print("\nPotęgowanie: ")
print(2**3)

print("\nSkrócone operatory:")
x = 5
x = x+1
print(x)

x += 1
print(x)
# x++ to BŁąd !

print("\nKonwersja typów:")
a = input("Podaj 1 liczbę: ")
b = input("Podaj 2 liczbe: ")
# konwersja na intiger(liczby całkowite) albo float(liczby z przecinkami[oddzielamy kropką a nie przecinkiem]) str-zmiana na liczby

print(int(a)+int(b))

y = 2
z = 2
print(str(y) + str(z))
del y
print(str(y) + str(z))
