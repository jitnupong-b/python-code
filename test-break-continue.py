from typing import Counter


mySequence = [12, 16, 17, 24, 29]

for i in mySequence:
    if i % 2 == 1:
        break
    print(i)

print('done')

mySequence = [12, 16, 17, 24, 29]

for i in mySequence:
    if i % 2 == 1:
        continue
    print(i)
print('done')