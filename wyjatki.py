x = 12
y = 2

try:
    lista = [3]
    print(lista[0])
    print(x + 4)
    print(x/y)
    print("Linijka po ")
# wyrzuca pierwszy bład i zakańcza program
except (ZeroDivisionError, TypeError):
    print("Wystapił 1 z 2 błędów")
except:
    print("Inny bład")
# koncowo wykona sie wszysto i wyrzuci wyjatek
finally:
    print("Finnaly: Wykonam i tak wszystko")

print("Dalsze instrukcje programu...")
