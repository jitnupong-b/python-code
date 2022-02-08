class BankAccount:

    def __init__(self, bal):
        self.__balance = bal

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
        else:
            print("Error, Insufficient balance")

    def addInterest(self):
        self.__balance = self.__balance + (self.__balance * (0.05/100))

    def getBalance(self):
        return self.__balance