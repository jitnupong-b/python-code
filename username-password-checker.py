#input
username = input("Please insert your username: ")
password = input("Please insert your password: ")

#process
if username == 'jitnupong.b@ku.th':
    if password == '123456':
        print("Permission Granted!")
    else:
        print("Wrong password")
else: 
    print("Wrong username")

if username == 'jitnupong.b@ku.th' and password == '123456':
    print("Permission Granted")
else:
    print("Wrong username and/or password")
print("Test")