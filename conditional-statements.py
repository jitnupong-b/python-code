#input
food = 'spammer'

#process
if food == 'spam':
    print("Ummmm, my favourite!")
    print("I feel like saying 100 times...")
    print(100 * (food + '! '))

#output

sales = float(input("Please insert your sales: "))

if sales > 50000:
    bonus = 500
    commissionRate = 0.12
    print("You met your sales quota")
    print("You will get money = ", bonus + sales * commissionRate)
elif sales > 25000:
    bonus = 400
    commissionRate = 0.10
    print("You will get money =", bonus + sales * commissionRate)
else: 
    bonus = 200
    commissionRate = 0.05
    print("You will get money =", bonus + sales * commissionRate)