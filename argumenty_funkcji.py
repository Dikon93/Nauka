def funkcja(arg1, arg2="World", *args, **kwargs):
    print(arg1, arg2, args, len(args), kwargs)
    for x in args:
        print(x)
        for x in kwargs.values():
            print(x)

# *args oznacza nieograniczona ilość argumentów nienazwanych (tu sie robi krotka)
# kwargs oznacza argumenty nazwane (tu sie robi zbiór)

# (KROTKA- nie da sie edytowac) {zbiór argumentów oznaczonych - mozna je edytować}


funkcja("Hello")
funkcja("Hi", "YT")

funkcja("Hi", "YT", "!", ":D", autor="Bartek", rok=2022)
