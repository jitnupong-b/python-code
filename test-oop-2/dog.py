class Dog:

    species = "Canis ..." #class attribute ตัวแปรของคลาส

    # name and age คือ instance attribue ตัวแปรของวัตถุจากคลาส
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def description(self):
        return self.name + " is " + str(self.__age) + " years old"

    def speak(self, sound):
        return self.name + " says " + sound

    def birthday(self):
        self.__age = self.__age + 1

buddy = Dog("Buddy", 5)
miles = Dog("Miles", 10)

print("Buddy Details")
print(buddy.name)
# print(buddy.__age)
print(buddy.species)
print(buddy.description())
print(buddy.speak("Hong Hong"))
buddy.birthday()
print(buddy.description())