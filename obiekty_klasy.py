class Czlowiek:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def przedstawSie(self, powitanie="Cześć"):
        return powitanie + ", mam na imię " + self.imie + " lat " + str(self.wiek) + "."


obiekt = Czlowiek("Bartek", 29)
print(obiekt.imie)
print(obiekt.przedstawSie("Witam"))

obiekt2 = Czlowiek("Adam", 52)
obiekt2.imie = "Adam"
print(obiekt2.przedstawSie())
