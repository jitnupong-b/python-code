def myFunction():
    print('Hello from my function!!')

def myFuntionWithArgs(username, greeting):
    print("Hello, %s, from my function, I wish you %s"%(username, greeting))

def sumTwoNumbers(a, b):
    result = a + b
    return result

myFunction()
myFuntionWithArgs("Boonchoo", "HNY")
x = sumTwoNumbers(1, 2)
print(x)