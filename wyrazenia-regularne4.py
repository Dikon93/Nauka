import re

# walidacja schematu


# (?P<>x)- grupa nazwana
# <> nazywa sie grupy tak
# (?:xx) grupa nienazwana

# uzycie "(!|\.)" umozliwia zakonczenie "kropka"
# znak | oznacza "lub"
wynik = re.match(
    r"^((?:He)(?P<pierwszy>ll)o)( Wor(ld))+(!|\.)$", "Hello World")

if wynik:
    print("Dopasowano")
    print(wynik.group())
    print(wynik.group(0))
    print(wynik.group(1))
    print(wynik.group(2))
    print(wynik.group(3))
    print(wynik.groups())
    print(wynik.group("pierwszy"))


else:
    print("Nie dopasowano")

print("_____________________")
