salary = int(input("Plese insert your salary: "))
yearsOnJob = int(input("Please insert your years on job: "))

if salary >= 10000:
    if yearsOnJob >= 5:
        print("OK, You can take benefit form loan")
else: 
    print("You cannot loan")

if salary >= 10000 and yearsOnJob >= 5:
    print("OK, You can take benefit form loan")
else:
    print("You cannot loan")