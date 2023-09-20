name = 'Python'

print(len(name))
print(name[0])
print(name[len(name)-1])
print('--------------------------------')
s = 'Java Programming Language'
s2 = s[5:6]
print(s2)
print('--------------------------------')
s3 = s[:4]

print(s3)
print('--------------------------------')

s4 = s[::-1]
print(s4)
print('--------------------------------')

s1 = 'Python Programming'

s5 = str(reversed(s1))
reversed(s5)
print(s)
print('--------------------------------')
s = s.capitalize()
print(s)
print('--------------------------------')
s = s.title()
print(s)
print('--------------------------------')
s = 'a'
print(s.isalpha())
print('--------------------------------')
s = '1'
print(s.isdigit())
print('--------------------------------')
s = 'Cydeo School'
print(s.istitle())