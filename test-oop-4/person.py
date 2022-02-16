class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def greet(self):
        return "Hi, It's " + self.name + " " + self.surname

    def calulateAge(self):
        return 80 - self.age

class Employee(Person):
    
    def __init__(self, name, surname, age, jobTitle, salary):
        super().__init__(name, surname, age)
        self.jobTitle = jobTitle
        self.salary = salary

    def getPay(self):
        return self.salary

class SalesEmployee(Employee):
    def __init__(self, name, surname, age, jobTitle, salary, incentive):
        super().__init__(name, surname, age, jobTitle, salary)
        self.incentive = incentive

    def getPay(self):
        return self.salary + self.incentive

sales = SalesEmployee("Natasha", "Romanov", 35, "Black Widow", 2500, 500)
print(sales.getPay())

"""person = Person("Steve", "Rogers", 120)
print(type(person))
print(isinstance(person, Person))
print(isinstance(person, Employee))
print(person.name)
print(person.surname)
print(person.age)
print(person.greet())
print(person.calulateAge())

employee = Employee("Tony", "Stark", 50, "Iron Man", 2000)
print(type(employee))
print(employee.name)
print(employee.surname)
print(employee.age)
print(employee.greet())
print(employee.calulateAge)"""