class Test:
    # wykonywanie jest ZAWSZE na końcu nie ważne gdzie jest wpisane w kodzie.
    def __del__(self):
        print("Żegnaj")


obj = Test()
obj2 = obj
lista = [obj2]
del obj
del obj2
del lista[0]


print("Koniec")
