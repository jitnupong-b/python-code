import random
import math

def main():
    number = random.randint(1, 10)
    print("random number is", number)

def main2():
    for count in range(5):
        number = random.randint(1, 6)
        print(number)

def testMathModule():
    print(math.floor(2.9))
    print(math.ceil(2.1))
    print(math.log(100))
    print(math.log10(100))
    print(math.sqrt(25))

testMathModule()
#main2()