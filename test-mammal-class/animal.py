class Mammal:

    def __init__(self, species):
        self.__specise = species

    def showSpecies(self):
        print("Species", self.__specise)

    def makeNoise(self):
        print("Grrrrr")

class Dog(Mammal):

    def __init__(self):
        Mammal.__init__(self, 'Dog')

    # ใช้คุณสมบัติ polymorphism
    def makeNoise(self):
        print("Hong Hong!")

class Cat(Mammal):

    def __init__(self):
        Mammal.__init__(self, 'Cat')

    def makeNoise(self):
        print("Meow Meow")