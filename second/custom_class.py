import numbers


class Employee:
    is_human = True
    planet = 'Earth'

    def __init__(self, name: str = 'Unknown', job_title: str = 'Janitor', salary: numbers = 0):
        self.name = name
        self.job_title = job_title
        self.salary = salary

    def work(self):
        print(f'{self.name} is working')

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


employee1 = Employee('Mehmet', 'QA Engineer', 100_000)
print(employee1.name)
print(employee1.job_title)
print(employee1.salary)

employee2 = Employee('Daniel')
print(employee2.name)
print(employee2.job_title)
print(employee2.salary)

employee3 = Employee('Breanna', 'SDET')
print(employee3.name)
print(employee3.job_title)
print(employee3.salary)

employee4 = Employee('Julia', 'Python Developer', 150_000)
print(employee4.name)
print(employee4.job_title)
print(employee4.salary)

print(employee4.is_human)
print(employee2.planet)
employee1.work()

print('-------------------------------------')
print(employee1)
print('-------------------------------------')
print(employee2)
print('-------------------------------------')
print(employee3)
print('-------------------------------------')
print(employee4)
