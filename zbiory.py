liczby1 = {0, 1, 2, 4}
slowa = set(["a", "b", "c"])

print(liczby1)
print(slowa)

liczby1.add(5)
print(liczby1)
liczby1.remove(0)
print(liczby1)
liczby1.add(5)
print(liczby1)

print(1 in liczby1)
liczby1 = {0, 1, 2, 3, 4}
liczby2 = {3, 4, 5, 6}
# suma
print(liczby1 | liczby2)
# częsci współne
print(liczby1 & liczby2)
# odejmowanie
print(liczby1 - liczby2)
# róznica symetryczna
print(liczby1 ^ liczby2)
