from person import Person, Employee, SalesEmployee

myPerson = Person('Natasha', 20)
print(myPerson.greet())

myEmployee = Employee('Steve', 50, 'Captain America', 2000)
print(myEmployee.greet(), "and I have paid:", myEmployee.getPay())

mySalesEmployee = SalesEmployee('Tony', 34, 'Iron Man', 1000, 250)
print(mySalesEmployee.greet(), "and I have paid: ", mySalesEmployee.getPay())