#import bankaccount

from bankaccount import BankAccount

saving = BankAccount(100)
print("Now, my balance =", saving.getBalance())

saving.deposit(500)
print("Now, my balance =", saving.getBalance())

saving.withdraw(700)
print("Now, my balance =", saving.getBalance())

saving.withdraw(200)
print("Now, my balance =", saving.getBalance())
