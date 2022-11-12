import re
# "r" zabezpiecza od słowka raw czyli ignoruje znaki tabulacji itd
wzor = r"banan"
tekst = r"gruszkabananjabłko"

print(re.match(wzor, tekst))
# musi być w konkretnej kolejnosci
if re.match(r".*" + wzor + r".*", tekst):
    # ".*" znaki specjalne które umozliwiaja dowolny tekst z przodu i z tyłu
    print("Dopasowano")
else:
    print("Niedopasowano!")
# szuka w całym tekscie
if re.search(wzor, tekst):
    print("Dopasowano")
else:
    print("Niedopasowano!")
# wyszukuje wszystkie wyszukania wzoru a nie tylko true i false
print(re.findall(wzor, tekst))

dopasowanie = re.search(wzor, tekst)
if dopasowanie:
    # wyswietla grupe z wzorem
    print(dopasowanie.group())
    # wzkazuje indeks gdzie sie zaczyna dane słowo z wzoru
    print(dopasowanie.start())
    # wzkazuje indeks gdzie sie kończy dane słowo ze wzoru
    print(dopasowanie.end())
    # wzkazuje jednoczesnie początek i koniec jako "krotka"
    print(dopasowanie.span())
# sub podmienia dane wyrazenie na inne
tekst2 = re.sub(wzor, r"jagoda", tekst)
print(tekst2)
