# The coinBetting() function takes two arguments: guess and money. 
# If the user's guess is the same as the random number, 
# the user wins 10 times the money. 
# If the user's guess is different from the random number, 
# the user loses the money.
# 
# The diceBetting() function takes two arguments: guess and money. 
# If the user's guess is the same as the random number, 
# the user wins 50 times the money. 
# If the user's guess is different from the random number,

import random

class Betting:
    
    def coinBetting(self, guess, money):

        sideup = random.randint(0, 1)
        print("Result of random = ", sideup)
        if guess == sideup:
            print("Congratulations :)")
            print("You'll get money =", money * 10)
            return money * 10
        else:
            print("Sorry :(")
            return -money

    def diceBetting(self, guess, money):
        sideup = random.randint(1, 6)
        print("Result of random = ", sideup)
        if guess == sideup:
            print("Congratulations :)")
            print("You'll get money =", money * 50)
            return money * 50
        else:
            return -money
