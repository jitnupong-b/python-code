answer = 'Chonburi'
pos = 0
province = input("Please insert Thailand's province name: ")

while answer != province and pos < len(answer):
    print("Wrong!, Hint Letter: ", answer[pos])
    province = input("Please insert again")
    pos = pos + 1

print("Congratulations")