def decorator(func):
    def wraper():
        print("------------")
        func()
        print("------------")
    return wraper


def hello():
    print("Hello world")


hello = decorator(hello)
hello()


@decorator
def witaj():
    print("Witaj Świecie")


witaj()
