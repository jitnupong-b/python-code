score = 65
grade = 'A'

if score >= 80:
    grade = 'A'
elif score >= 75:
    grade = 'B+'
elif score >= 70:
    grade = 'B'
else:
    grade = 'C'

print('Your score = ', score, ' and your grade = ', grade)

gpa = 2.1
courseComplete = True

if gpa > 2 and courseComplete == True:
    print('Congratulations!')