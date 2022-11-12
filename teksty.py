from cgi import test


plik = open("test.txt", "a")
if plik.writable():
    # \n znak nowej lini
    plik.write(input("Wpisz tekst:") + "\n")
 # zamykanie pliku zeby zwolnić pamięć
plik.close()

plik = open("test.txt", "r")
# sprawdzanie czy wgl mozna sczytać
if plik.readable:
    print("Zawartosc pliku:")
    # sczytywanie zawatosci pliku kazde w jednej lini
    tekst = plik.read()
    print(tekst)
    # lista z pliku .readlines()
    tekst_lista = plik.readlines()
    print(tekst_lista)
    # wywwietlanie jako iteracja
    for l in plik:
        print(l)
