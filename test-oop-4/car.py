class Car:
    def start(self):
        print("Start the Car")

    def go(self):
        print("Going")

class Flyable():
    def start(self):
        print("Start the Flyalbe Object")

    def fly(self):
        print("Flying")

class FlyableCar(Flyable, Car):
    def start(self):
        super().start()


myFlyableCar = FlyableCar()
myFlyableCar.start()
