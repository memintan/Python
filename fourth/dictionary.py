employee1 = {}

employee1['name'] = 'james'
print(employee1)

print('------------------------------------')

employee1['name'] = 'daniel'
print(employee1)

print('------------------------------------')

employee1['age'] = 45
employee1['salary'] = 60_000
print(employee1)

print('------------------------------------')

employee2 = {
    'name': 'James',
    'age': 29,
    'salary': 80_000,
    'full_time': False
}

print(employee2)
print(employee2['name'])

print('------------------------------------')

employee2['salary'] += 10000
print(employee2)

print('------------------------------------')

employee2.update({'age': 40})
print(employee2)

print('------------------------------------')

employee2['full_time'] = True
# employee2.update({'full_time': True}) ____same
print(employee2)

print('------------------------------------')

employee2.pop('full_time')
print(employee2)

print('------------------------------------')

employee2.popitem()
print(employee2)

print('--------------IIterating Dictionary----------------------')

employee3 = {
    'name': 'Shay',
    'age': 29,
    'salary': 110_000,
    'full_time': False,
    'Job_title': 'Developer',
    'company': 'Apple Inc'
}

print(list(employee3.keys()))

for key in employee3.keys():
    print(f'{key}: {employee3[key]}')

print('------------------------------------')

values = employee3.values()
print(values)

print('------------------------------------')

for x in employee3.items():
    print(f'{x[0]} : {x[1]}')

print('------------------------------------')

students = {
    'A01': {
        'name': 'James',
        'gender': 'Male',
        'gpa': 3.5,
        'subjects': ['Mathematics', 'Physics']
    },
    'A02': {
        'name': 'Hazel',
        'gender': 'Female',
        'gpa': 3.8,
        'subjects': ['Biology', 'Programming']
    },
    'A03': {
        'name': 'Yulia',
        'gender': 'Female',
        'gpa': 4,
        'subjects': ['Chemistry', 'Programming']
    }
}

print(students)

print('------------------------------------')

students['A01']['gpa'] = 2.5
print(students)

print('------------------------------------')

students['A02'].update({'name': 'Daniel', 'gender': 'male'})
# students['A02']['name'] = 'Daniel'
# students['A02']['gender'] = 'male'
print(students)

print('------------------------------------')

students['A03']['subjects'][1] = 'Biology'
print(students['A03'])

print('------------------------------------')



print('------------------------------------')

for value in students.values():
    print(value)
    for item in value.items():
        print(item[1])

print('------------------------------------')
