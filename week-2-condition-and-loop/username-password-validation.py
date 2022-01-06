username = input("Please insert your username: ")
password = input("Please insert your password: ")

if username == 'xxxxx' and password == '123456':
    print("Permission Granted!!")
else:
    print("Wrong username and/or password")

if username == 'xxxxx':
    if password == '123456':
        print("Permission Granted")
    else:
        print("Wrong Password")
else:
    print("Wrong Username")

majorChoice = input("Please select your major (1: CS, 2: IT): ")

if majorChoice == '1':
    print("You are CS student")
elif majorChoice == '2':
    print("You are IT student")
else:
    print("Please select 1 or 2 only!")
