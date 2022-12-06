class Fabia:
    # uzywać __init__ żeby kazda "fabia" miała swoje rzeczy
    def __init__(self, kolor):
        self.kolor = kolor
        self.ilosc_paliwa = 30
        self.spalanie_na_100 = 15

    def zasieg(self):
        zasieg = self.ilosc_paliwa * 100 / self.spalanie_na_100
        return zasieg

    def hamuj(self):
        pass


#fabia = Fabia()
#fabia2 = Fabia()

# print(id(fabia.kolor))
# print(id(fabia2.kolor))
# fabia.bagaznik.append("czapka")
# fabia2.bagaznik.append("hulajnoga ")
# print(fabia.bagaznik)

fabia = Fabia("czerwona")
fabia.ilosc_paliwa += 15
fabia2 = Fabia("biała")

print(fabia.kolor)
print(fabia2.kolor)

print(fabia.zasieg())
print(fabia2.zasieg())
