def funkcja(x):
    return x*x


zmienna = funkcja
print(zmienna(5))


def funkcja2(f1, x):
    return f1(x) * x

# podanie funkcji w innej funkcji


print(funkcja2(funkcja, 5))

# rekurencja


def silnia(x):
    if x <= 1:
        return 1
    else:
        return x*silnia(x-1)


print(silnia(5))
