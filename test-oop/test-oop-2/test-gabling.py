from gambling import Betting

bet = Betting()
print('@@@@@ Gambling Apps @@@@@')
pocketMoney = float(input("How many money that you have: "))

while True:
    choice = input("\nPlease select the game (1: coin, 2: dice, another to exit): ")

    if choice == '1':
        print("\n+++ Coin Betting +++")
        guess = input("Please select your sideup (0: tails, 1: heads): ")
        money = input("Please insert your bet: ")
        pocketMoney = pocketMoney + bet.coinBetting(int(guess), float(money))
    elif choice == '2':
        print("\n+++ Dice Betting +++")
        guess = input("Please select your sideup (1-6): ")
        money = input("Please insert your bet: ")
        pocketMoney = pocketMoney + bet.diceBetting(int(guess), float(money))
    else:
        break;
    
    print("Now, you have money =", pocketMoney)