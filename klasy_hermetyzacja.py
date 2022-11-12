class Test:
    __lista = []

    def dodaj(self, arg):
        self.__lista.append(arg)

    def zdejmij(self):
        if len(self.__lista) > 0:
            return self.__lista.pop(len(self.__lista) - 1)
        else:
            return


obj = Test()
obj.dodaj("A")
obj.dodaj("B")
obj.dodaj("C")
print(obj.zdejmij())

# aby ukryć zmienne dodaj '_'
# aby sie odnieśc do takiej zmiennej wystarczy wiedzieć ze ma '_'
# aby ukryć podwójnie zmienne dodaj '__'
# aby odnieść sie do podwójnie ukrytej zmiennej opórcz wiedzy ze ma '__' trzeba odnieśc sie do "_'klasa'__zmienna" python ufa swoim uzytkownikom
