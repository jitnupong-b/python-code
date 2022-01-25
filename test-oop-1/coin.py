import random

class Coin:

    def __init__(self):
        self.sideUp = 'Heads'
        
    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideUp = 'Heads'
        else:
            self.sideUp = 'Tails'

    def getSideUp(self):
        return self.sideUp

class Coin2:

    def __init__(self):
        print('test')

myCoin = Coin()
print("For now this coin is:", myCoin.getSideUp())
myCoin.toss()
print("For now this coin is:", myCoin.getSideUp())
print("For now this coin is:", myCoin.sideUp)
myCoin.sideUp = 'Tails'