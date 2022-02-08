import random

class Coin:

    # headup หน้า
    def __init__(self):
        self.sideup = 'Heads'

    # toss() สุ่มหน้า
    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    # getSideup() ตรวจสอบหน้าเหรียญ
    def getSideup(self):
        return self.sideup

class CoinHide:

    # headup หน้า
    def __init__(self):
        self.__sideup = 'Heads'

    # toss() สุ่มหน้า
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    # getSideup() ตรวจสอบหน้าเหรียญ
    def getSideup(self):
        return self.__sideup

#myCoin = Coin()
#print(myCoin.sideup)
#myCoin.sideup = 'Tails'

#print("Now, myCoin is", myCoin.getSideup())
#myCoin.toss()
#print("After Toss(), myCoin is", myCoin.getSideup())

myCoin2 = CoinHide()
myCoin2.__sideup = 'Tails'
print("Now, myCoin2 is", myCoin2.getSideup())
myCoin2.toss()
print("Now, after toss() myCoin2 is", myCoin2.getSideup())
