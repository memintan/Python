import numbers


def display_message():
    print('Hello World')
    print('Hello Mehmet')


display_message()

print('------------------------------')


def value():
    return 10


print(value())

print('------------------------------')


def return_int() -> int:
    return 10.0


print(return_int())

print('------------------------------')


def square(num: int):
    return num * num


print(square(10))

print('------------------------------')


def multiplying(num1, num2):
    return num1 * num2


print(multiplying(3, 2))

print('------------------------------')


def add(num1: numbers, num2: numbers) -> numbers:
    return num1 + num2


print(add(7, 12))

print('------------------------------')


def calculate(num1: numbers, num2: numbers, operator: str) -> numbers:
    if operator == "-":
        return num1 - num2
    elif operator == "+":
        return num1 + num2
    elif operator == "/":
        return num1 / num2
    elif operator == "*":
        return num1 * num2
    else:
        print("Invalid operator")


print(calculate(10, 20, "*"))

print('------------------------------')


# Method overloading

def sum(n1: numbers, n2: numbers, n3: numbers = 0, n4: numbers = 0) -> numbers:
    return n1 + n2 + n3 + n4


print(sum(10, 20))
print(sum(10, 20, 30))
print(sum(10, 20, 30, 40))

print('------------------------------')


class Test:
    def method(self):
        pass


print('------------------------------')


def concat(a: str, b, c='', d='', e=''):
    print(f'{a} {b} {c} {d} {e}'.strip())


concat('Cydeo', 'School')
concat('Python', 3, 2.5)
concat('Python', 3, 2.5, True)
concat('Python', 3, 2.5, True, False)
