if False:
    print('Python Programming')

print('Java Programming')
print('------------------------------------')

score = 70
if score >= 60:
    print('Congrats! you have passed the exam')

s = 'Fatih Ibrahim Tan'
if 'f' and 'i' in s:
    print(s, 'has', 'f and i')
print('------------------------------------')

if score >=60:
    print('Passed')
else:
    print("Failed")

print('------------------------------------')

age = 20
result = None
if age >= 23:
    result = 'Eligible'
else:
    result = 'Not Eligible'
print(result)

print('------------------------------------')

age = 26
result = 'Eligible' if age >= 23 else 'Not Eligible'
print(result)

print('------------------------------------')

num = 100

if num > 0:
    result = 'Positive'
elif num < 0:
    result = 'Negative'
else:
    result = 'Zero'
print(result)

print('------------------------------------')

score = 200
result = 'Positive' if num >= 0 else 'Zero'
print(result)

print('------------------------------------')

score = -300

if 0 <= score <= 100:
    if score >= 60:
        print('Passed')
    else:
        print('Failed')
else:
    print('Invalid Score')

print('---------------------------------')