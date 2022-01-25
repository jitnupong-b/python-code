class Person:

    def __init__(self):
        self.noOfHead = 1
        self.noOfNose = 1

    def sayHi(self):
        print("Hello, How are you?")

    def sleep(self):
        print("I'm sleeping")

boonchoo = Person()
boonchoo.sayHi()
boonchoo.sleep()
print(boonchoo.noOfHead)

mary = Person()
mary.sayHi()
mary.sleep()