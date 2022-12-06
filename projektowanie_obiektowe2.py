class Fabia():
    def hamuj(self):
        print("Hamuje !!")

    def skrecaj(self, strona):
        # dodanie do strony '=x' gdzie x to wartosc domyslna
        print(f"Skręcam w {strona}")

    def ilosc_paliwa(self):
        return "10 litrów"

    def info(self):
        # przy dawaniu parametrów ZAWSZE self jest pierwszy
        print(self)

    def __str__(self):
        return "Bartek"

    def __init__(self):
        print("fabia jest spoko")


moja_fabia = Fabia()
twoja_fabia = Fabia()
moja_fabia.hamuj()
# moja_fabia.skrecaj("prawo")
# ilosc_paliwa = moja_fabia.ilosc_paliwa()
# print(ilosc_paliwa)

# self to uchwyt do instancji a nie do clasy - wiec jest uchwytem samym w sobie
moja_fabia.info()
# "moja fabia" a 'twoja fabia' to to ROŻNE fabie - obie to fabie ale ROŻNE
twoja_fabia.info()

print(moja_fabia)
