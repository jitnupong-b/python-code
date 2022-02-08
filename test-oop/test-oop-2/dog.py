class Dog:
    # ตัวแปรของคลาส
    species = "Canis familiaris"

    def __init__(self, name, age):
        # ตัวแปรของทุกวัตถุจากคลาส
        self.name = name
        self.__age = age

    def description(self):
        return self.name + " is " + str(self.__age) + " years old"

    def speak(self, message):
        return self.name +  " says " + message

    def walk(self, destination):
        return self.name + " is walking to "  + destination

    def getAge(self):
        return self.__age
    
    def birthday(self):
        self.__age = self.__age + 1

buddy = Dog("Buddy", 5) #create object from Dog Class
# เข้าถึงตัวแปรของวัตถุจากคลาส เพื่ออ่านข้อมูล
print(buddy.name) 
# check misconcepts
buddy.__age = 25

print(buddy.__age)
print(buddy.getAge())
print(buddy.species)
print(buddy.description())
print(buddy.speak("Hong Hong!"))

buddy.birthday()
print(buddy.description())

print("")
milo = Dog("Milo", 2)
milo.__age = 5
print(milo.__age)
print(milo.getAge())

# เข้าถึงตัวแปรของวัตถุจากคลาส เพื่อเขียนข้อมูล
""" buddy.name = "Milo"
print(buddy.name)
buddy.__age = -5
print(buddy.__age)
buddy.species = "Homosapients"
print(buddy.species) """