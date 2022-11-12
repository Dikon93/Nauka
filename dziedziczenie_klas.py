class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    def voice(self):
        print("HAU HAU")


dog = Dog("Reksio", 10)
print(dog.name)
print(dog.age)
dog.voice()


class Wolf(Dog):
    def getVoice(self):
        print("Jestem wilkiem, ")
        super().voice()


class Cat(Animal):
    def getvoice(self):
        print("MIAU MIAU")


cat = Cat("Bury", 8)
cat.getvoice()

wolf = Wolf("Geralt", 55)
wolf.getVoice()
