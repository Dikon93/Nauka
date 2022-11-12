def funkcja(f, liczba):
    return f(liczba)


print(funkcja(lambda x: x*x, 3))


def kwadrat(x):
    return x*x


print(kwadrat(5))
wyn = (lambda x: x*x)(4)
print(wyn)


def lam(x): return x*x


print(lam(6))
