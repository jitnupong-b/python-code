name = 'Harrison'
guess = input("So, I'm thinking of person's name. Try to guess it: ")
position = 0

while guess != name and position < len(name):
    print("Nope, that's not it: Hint letter")
    print(position + 1, "is", name[position])
    guess = input("Guess again: ")
    position = position + 1

if position == len(name) and name != guess:
    print("Too bad, the name is", name)
else:
    print("Great, you got it in", position, "guesses")