import json
path = '/Users/halilibrahimtan/Documents/Python/fourth/files/Test.json'

json_file = open(path, 'r')

# print(type(json_file.read()))

dictionary = json.load(json_file)
print(dictionary)
print(type(dictionary))

for x in dict(dictionary).keys():
    print(x)

json_file.close()

print('------------ Write Json file----------------------')

students = {
    'A01': {
        'name': 'James',
        'gender': 'Male',
        'gpa': 3.5,
        'subjects': ['Math', 'Physics']
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

dictionary['name'] = 'Aaron King'
dictionary['age'] = 45

print(dictionary)

json_file = open('/Users/halilibrahimtan/Documents/Python/fourth/files/Test2.json', 'w')

# json_object = json.dumps(dictionary, indent=2)  # converting dictionary object to json object
json_object = json.dumps(students, indent=2)

json_file.write(json_object)
# json_file.write(json_object)

