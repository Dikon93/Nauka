import re

if re.match ("^[Kk]o.$", "kot"):
    print("Dopasowano")
else:
    print("Nie dopasowano")

# ^ wymusza ze od tego ma sie zaczynać.
# jesli ^ jest w przedziale to neguje je
# $ wymusza ze na tym znaku ma sie konczyć.
# [xX]lub[A-Z]lub[A-Za-z] klasa znaków wiec kazdy z tego bedzie pasował
