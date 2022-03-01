studentScore = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

i = 0
for row in studentScore:
    j = 0
    for col in row:
        myString = "Please insert score of studentScore[" + str(i) +"][" + str(j) + "]: "
        score = input(myString)
        studentScore[i][j] = float(score)
        j = j + 1
    i = i + 1

print(studentScore)
