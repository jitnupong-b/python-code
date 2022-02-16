class BankAccount:
    def __init__(self, bankName, bankBranch, ownerName, accountId, balance):
        self.__bankName = bankName
        self.__bankBranch = bankBranch
        self.__ownerName = ownerName
        self.__accountId = accountId
        self.__balance = balance

    def open(self):
        print("Open Account Complete")

    def close(self):
        print("Closed Account Complete")
    
    def deposit(self, money):
        self.__balance = self.__balance + money

    def withdraw(self, money):
        self.__balance = self.__balance - money

    def addInterest(self):
        self.__balance = self.__balance + (self.__balance * (0.05 / 100))

    def showBalance(self):
        print("Now, you have", self.__balance, "THB")

class GeneralSaving(BankAccount):

    def __init__(self, bankName, bankBranch, ownerName, accountId, balance):
        BankAccount.__init__(bankName, bankBranch, ownerName, accountId, balance)
        if balance >= 100:
            self.__balance = balance
        else:
            print("To open JadTem saving you must pay 100 THB")        
    
    def addInterest(self):
        self.__balance = self.__balance + (self.__balance * (0.1 / 100))

class JadTem(BankAccount):

    def __init__(self, bankName, bankBranch, ownerName, accountId, balance):
        BankAccount.__init__(self, bankName, bankBranch, ownerName, accountId, balance)
        if balance >= 100000:
            self.__balance = balance
        else:
            print("To open general saving you must pay 100000 THB")

    def addInterest(self):
        print(self.__balance)
        if self.__balance < 100000:
            self.__balance = self.__balance + (self.__balance * (0.25 / 100))
        elif self.__balance > 100000 and self.__balance < 3000000:
            self.__balance = self.__balance + (self.__balance * (1.0 / 100))
        else:
            self.__balance = self.__balance + (self.__balance * (0.25 / 100))