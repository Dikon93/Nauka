from oblicz_brutto import oblicz_brutto


netto = float(input("Jaka jest stawka  netto? "))
vat = float(input("Jaka jest stawka vat?"))

brutto = oblicz_brutto(netto, vat)

print(f"Wartość brutto wynosi {brutto} ")
