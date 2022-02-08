import random

class Casino:

    def coinGuess(self, guess, money):
        prize = 0
        if random.randint(0, 1) == guess:
            print("Congratulations :)")
            prize = 10 * money
        else:
            print("Sorry :(")
            prize = -money
        print("Your prize =", prize)
        return prize
    
    def diceGuess(self, guess, money):
        prize = 0
        if random.randint(1, 6) == guess:
            print("Congratulations :)")
            prize = 50 * money
        else:
            print("Sorry :(")
            prize = -money
        print("Your prize =", prize)
        return prize

gambling = Casino()
print("@@@ Canino App @@@")
pocketMoney = float(input("Please insert your pocket money: "))

while True:
    choice = input("\nPlease select your game (1: coin, 2: dice, another to exit): ")
    if choice == '1':
        print()
        guess = int(input("Please select your sideup (0: Tail, 1: Head): "))
        if guess != 0 and guess != 1:
            print("0 or 1 only!")
        else:     
            money = float(input("Please insert bet money: "))
            if pocketMoney >= money:
                prize = gambling.coinGuess(guess, money)
                pocketMoney = pocketMoney + prize
            else:
                print("Not Enough Money")
    elif choice == '2':
        print()
        guess = int(input("Please select your sideup (1-6): "))
        money = float(input("Please insert your bet money: "))
        prize = gambling.diceGuess(guess, money)
        pocketMoney = pocketMoney + prize
    else:
        break

    print("\nNow, You still have money in your pocket =", pocketMoney)

# print(gambling.coinGuess(0, 10))
# print(gambling.diceGuess(4, 50))