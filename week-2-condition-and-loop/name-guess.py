name = 'Harrison'
guess = input("Please guess the name: ")
pos = 0

while guess != name and pos < len(name):
    print('No, you missed :( Hint letter:', end='')
    print(name[pos])