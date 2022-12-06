def oblicz_pensje(*args, base: float) -> float:
    pensja = base
    for arg in args:
        pensja = pensja + (pensja * arg)

    return pensja


print(oblicz_pensje(0.1, 0.25, 0.3, base=1000))
print(oblicz_pensje(0.1, base=1000))
