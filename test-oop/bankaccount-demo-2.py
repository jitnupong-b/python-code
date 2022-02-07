import bankaccount

startMoney = float(input("Enter starting balance: "))
boonchooAccount = bankaccount.BankAccount(startMoney)
print("For now, my money =", boonchooAccount.getBalance())

while True:
    choice = input("Please select menu (1=deposit, 2=withdraw, 3=check balance, another to exit): ")

    if choice == '1':
        amount = float(input('Enter money to deposit:'))
        boonchooAccount.deposit(amount)
        print("For now, after deposit you money =", boonchooAccount.getBalance())
    elif choice == '2':
        amount = float(input('Enter money to withdraw:'))
        boonchooAccount.withdraw(amount)
        print("For now, after withdraw your money =", boonchooAccount.getBalance())
    elif choice == '3':
        print("For now, your money =", boonchooAccount.getBalance())
    else:
        break;

boonchooAccount.addInterest()
print("This year, your money after add interest =", boonchooAccount.getBalance())