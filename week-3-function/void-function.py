name = input("Please insert your name: ")
print(name)

# Function for print hello message
def my_function():
    print("Hello from a function")

# Function for receive one argument from caller
def my_function_one_argument(fname):
    print(fname, " Refsnes")

# Function for receive two arguments from caller
def my_function_with_args(username, greeting):
    print("Hello %s, From my function!, I wish you %s"%(username, greeting))
    print("Hello", username, ", From my function, I wish you", greeting)

def sum_two_values(a, b):
    result = a + b
    return result

def sum_four_values(a, b, c, d):
    return a + b + c + d

my_function()
my_function_one_argument(name)
my_function_with_args(name, "HNY1")

my_function()
sum_two_values(1, 2)
x = sum_two_values(1, 2)
print("1+2=", x)
print("1+2=", sum_two_values(1, 2))
print(sum_two_values(sum_two_values(1, 2), sum_two_values(2, 3)))