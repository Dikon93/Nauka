# pozycyjne = przekazujemy po kolei
# nazwane - kolejnosc dowolna posługuje sie nazwą

def calculate_sum(a, b, c=10):
    print("Suma a+b wynosi", a + b + c)
    return a+b+c


result = calculate_sum(2, 8)
print("Wynikiem funkcji jest", result)

result = calculate_sum(a=2, b=8, c=4)
print("Wynikiem funkcji jest", result)
