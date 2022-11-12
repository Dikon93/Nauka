def dzielenie(x, y):
    # jesli warunek jest fałszywy to przechodzi dalej
    assert y != 0, "y było równe 0"
    # jesli jest prawdziwy to anuluje
    if y == 0:
        # wyrzucenie błędu, nadanie własnej etykiety i przerwanie programu
        raise ZeroDivisionError("Dzielenie przez zero")
    print(x/y)


# wyrzucenie błedu bez przerywania programu
try:
    dzielenie(2, 0)
except ZeroDivisionError:
    print("Błąd dzielenia przez 0")
    raise
