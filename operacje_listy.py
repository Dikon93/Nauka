lista = [10, 20, 32, 40, 53, 56, 87]

# domyślnie zwraca true albo false
if all([i % 2 == 0 for i in lista]):
    print("Wszystkie parzyste")
# którakolwiek jest warunkiem
if any([i % 2 == 0 for i in lista]):
    print("Chociaz jeden jest parzysta")
# tworzy "pary" i numeruje argumenty
for i in enumerate(lista):
    print(i[0]+1, "-", i[1])
