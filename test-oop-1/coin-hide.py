import random

class Coin:

    def __init__(self):
        self.__sideUp = 'Heads'
        
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideUp = 'Heads'
        else:
            self.__sideUp = 'Tails'

    def getSideUp(self):
        return self.__sideUp

myCoin = Coin()
print("For now this coin is:", myCoin.getSideUp())
myCoin.toss()
print("For now this coin is:", myCoin.getSideUp())
myCoin.__sideUp = 'Middle'
print("For now this coin is:", myCoin.getSideUp())
