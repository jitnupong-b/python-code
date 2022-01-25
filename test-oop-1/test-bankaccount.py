import bankaccount

boonchooAccount = bankaccount.BankAccount(100)
boonchooAccount.getBalance()

boonchooAccount.deposit(1000)
boonchooAccount.getBalance()

boonchooAccount.withdraw(200)
boonchooAccount.getBalance()

boonchooAccount.withdraw(1000)
boonchooAccount.getBalance()

boonchooAccount.__balance = 10000000000000000
boonchooAccount.getBalance()

# 31 / 12 
boonchooAccount.addInterest()
boonchooAccount.getBalance()
