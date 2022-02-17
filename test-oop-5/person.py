class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return "Hi, It's " + self.name

class Employee(Person):
    
    def __init__(self, name, age, jobTitle, basePay):
        Person.__init__(self, name, age)
        self.jobTitle = jobTitle
        self.basePay = basePay
    
    def getPay(self):
        return self.basePay

class SalesEmployee(Employee):

    def __init__(self, name, age, jobTitle, basePay, payIncentive):
        Employee.__init__(self, name, age, jobTitle, basePay)
        self.payIncentive = payIncentive

    def getPay(self):
        return self.basePay + self.payIncentive




"""myPerson = Person('Boonchoo', 25)

myEmployee = Employee('Natasha', 36, 'Black Widow')
print(type(myEmployee))
print(type(25))

print(isinstance(myPerson, Person))
print(isinstance(myEmployee, Person))
print(isinstance(myPerson, Employee))

myEmployee = Employee('Natasha', 36, 'Black Widow')
print(myEmployee.greet())

myPerson = Person('Boonchoo', 25)
print(myPerson.name)
myPerson.name = 'Steve'
print(myPerson.name)
print(myPerson.age)"""