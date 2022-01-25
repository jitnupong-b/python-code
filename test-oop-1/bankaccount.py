class BankAccount:

    def __init__(self, openCash):
        self.__balance = openCash

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
        else:
            print("Insufficient Amount")

    def getBalance(self):
        print("Your Balance =", self.__balance)

    def addInterest(self):
        self.__balance = self.__balance + (0.05/100 * self.__balance)
