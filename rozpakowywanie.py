a, b = (2, 5)

# rozpakowywanie krotki
print(a)
print(b)

x = 10
y = 20

x, y = y, x

print("x:", x)
print("y:", y)

# *przejmuje wartosci pozostałe
start, *wszystko, koniec = (1, 2, 3, 4, 5, 6, 7)
print(start)
print("Wszystko:", wszystko)
print(koniec)
