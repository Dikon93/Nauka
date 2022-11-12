def gen():
    i = 0
    while i < 5:
        # działa jak return ale nie przerywa funkcji
        yield i
        i += 1


for i in gen():
    print(i)

print(list(gen()))


def parzyste(x):
    i = 0
    while i <= x:
        if i % 2 == 0:
            yield i
        i += 1


for i in parzyste(16):
    print(i)

print(list(parzyste(30)))
