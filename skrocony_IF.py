print("prawda") if 5 > 6 else print("nieprawda")

print("prawda") if 5 > 3 else print("nieprawda")

a = "parzysta" if 10 % 2 else "Nieparzysta"
print(a)

for i in range(10):
    if i > 5:
        continue
else:
    print("Koniec")
    print("_________")

    # else wykona sie tylko gdy bedzie kontynuowało sie a nie bedzie "Break"

try:
    a = 5/5
except ZeroDivisionError:
    print("Błąd")
else:
    print("Koncówka")
finally:
    print("Zawsze koniec")
