student = {
    '62900928738': ['Natasha', 'Romanov', 'Female', '9999999'],
    1: 'Mary',
    2: 'Steve',
    3: 'David',
    4: 'Robert',
    '5': 'Tony'   
}

print(student[1])
student['5'] = 'Natasha'
print(student)

del student['5']
print(student)

value = student.get(0, 'Not found')
print(value)

print(student.items())
print(student.keys())
print(student.values())

value = student.pop(4)
print(student)
print(value)

key, value = student.popitem()
print(student)
print(key, value)

key, value = student.popitem()
print(student)
print(key, value)

student['test'] = 'test'
print(student)

studentDetail = student.get('62900928738', 'Not Found')
print(studentDetail)
