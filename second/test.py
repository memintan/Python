from utility import sum, calculate

result = sum(10, 40)
print(result)

result = calculate(40, 90, '-')
print(result)

import utility

utility.concat("Java", "Python")
utility.sum(10, 20)
utility.calculate(10, 30, "*")

print('---------------------------------------------------------')

import utility as u

u.sum(10, 20)
u.concat("A", 1, 2)
u.calculate(20, 30, "/")

print('---------------------------------------------------------')

from utility import sum as s

print(s(10, 20))
