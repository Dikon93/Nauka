class KontoBankowe:
    __stan = 0

    # ustawiamy właściwość

    @property
    def stan_konta(self):
        return self.__stan

    @stan_konta.getter
    def stan_konta(self):
        return "Stan Konta: " + str(self.__stan) + "zł"

    @stan_konta.setter
    def stan_konta(self, value):
        self.__stan += value


konto = KontoBankowe()
print(konto.stan_konta)

konto.stan_konta = 50
print(konto.stan_konta)
konto.stan_konta = 150
print(konto.stan_konta)
konto.stan_konta = 450
print(konto.stan_konta)
konto.stan_konta = -750
print(konto.stan_konta)
