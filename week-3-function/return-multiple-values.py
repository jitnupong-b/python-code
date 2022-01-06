def calculator(a, b):
    plus = a + b
    minus = a - b
    multiply = a * b
    divide = a // b
    return plus, minus, multiply, divide

plus, minus, multiply, divide = calculator(5, 2)
print("5+2=", plus)
print("5-2=", minus)
print("5*2=", multiply)
print("5/2=", divide)