import re

# ^ - początek $- koniec

# walidacja maila

if re.match(r"^([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9\.-]+[A-Za-z0-9])@([A-Za-z0-9]+|[A-Za-z0-9][A-Za-z0-9-\.]+[A-Za-z0-9])\.[A-Za-z0-9]+$", "dikon93@gmail.com"):

    print("Prawidłowy")
else:
    print("Nie prawidłowy")
