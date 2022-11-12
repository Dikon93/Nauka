lista = list(range(10))

# kazda liczbe z listy pomnóż razy 2
nowa = [i * 2 for i in lista]
# do kazdej liczby parzystej dodaj 2
nowa2 = [i + 2 for i in lista if i % 2 == 0]

print("Lista:", lista)
print("Nowa: ", nowa)
print("Nowsza: ", nowa2)
