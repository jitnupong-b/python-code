import random
import math

def main():
    number = random.randint(1, 10)
    print(number)

for i in range(5):
    main()

number = float(input("Enter the number: "))
result1 = number ** 0.5
result2 = math.sqrt(number)
print("Square root of", number, "is", result1, result2)

number = 2.2
print(math.ceil(number), math.floor(number))
print(math.log10(100))
print(math.log(100))