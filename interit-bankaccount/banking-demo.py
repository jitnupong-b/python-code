from banking import JadTem

myJadTem = JadTem("SCB", "KUSRC", "Boonchoo", "12345678", 100000)
myJadTem.showBalance()
myJadTem.deposit(1000)
myJadTem.showBalance()
myJadTem.addInterest()
myJadTem.showBalance()