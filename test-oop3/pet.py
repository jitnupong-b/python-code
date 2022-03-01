class Pet:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age


class Dog(Pet):

    def __init__(self, name, age, breed):
        Pet.__init__(self, name, age)
        self.__breed = breed

    def getBreed(self):
        return self.__breed

    def setBreed(self, breed):
        self.__breed = breed

    def calculateHumanAge(self):
        return int(Pet.getAge(self)) * 7


class Cat(Pet):

    def __init__(self, name, age, breed) -> None:
        Pet.__init__(self, name, age)
        self.__breed = breed

    def getBreed(self):
        return self.__breed

    def setBreed(self, breed):
        self.__breed = breed

    def calculateHumanAge(self):
        if Pet.getAge(self) == 1:
            return 15
        elif Pet.getAge(self) == 2:
            return 24
        elif Pet.getAge(self) >= 3 and Pet.getAge(self) <= 10:
            ageDiff = Pet.getAge(self) - 2
            return 24 + (ageDiff * 4)
        else:
            ageDiff = Pet.getAge(self) - 10
            return 60 + (ageDiff * 4)

print('---- Dog Demo ----')
myDog = Dog('Sally', 2, 'Hound')
print("This dog name", myDog.getName())
print("He/she is", myDog.getBreed())
print("He/she is", myDog.getAge(), "years old. He/she is",
      myDog.calculateHumanAge(), "years old, if he/she is human.")

print('\n---- Cat Demo ----')
myCat = Cat('Garfield', 5, 'Thai Srisawad')
print("This cat name", myCat.getName(), ".")
print("He/she is", myCat.getBreed(), ".")
print("He/she is", myCat.getAge(), "years old. He/she is",
      myCat.calculateHumanAge(), "years old, if he/she is human.")
