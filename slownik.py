# klucz:wartość "klucza"

slownik = {1: "Poniedziałek", 2: "Wtorek", 7: "Niedziela"}

print(slownik[1])
print(slownik[7])
# dodawanie wartości do słownika poprzez przypisanie
slownik[3] = "Środa"
slownik[4] = False
slownik[5] = 5
print(slownik)
# można dodawać dowolny typ danych
slownik["a"] = 1
print(slownik["a"])
print(slownik)
# funkacja get moze podac albo coś co jest, a jak nie ma to daje to co w cudzysłowie
print(slownik.get(8, "Inny dzień"))

print("\n Pętla: ")
# domyslnie pętla "l" iteruje po kluczach
# jak sie doda .values to wtedy do wartościach
for l in slownik.values():
    print(l)

print("_____________________")
# usuwanie elementów .pop
print(slownik.pop(1))
print(slownik)
