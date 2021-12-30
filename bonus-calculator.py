year = 3
salary = 20000
bonus = 0

if year >= 3:
    if salary >= 20000:
        bonus = 5000
    else: 
        bonus = 4000
else:
    if salary >= 20000:
        bonus = 3000
    else:
        bonus = 2000

if year >= 3 and salary >= 20000:
    bonus = 5000
elif year < 3 and salary >= 20000:
    bonus = 4000