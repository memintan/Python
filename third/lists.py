groceries_list = ['Eggs', 'Milk', 'Rice']
print(groceries_list)
print('------------------------------------')
groceries_list.append('Chicken')
print(groceries_list)
print('------------------------------------')
groceries_list[-2] = 'Cherry'
print(groceries_list)
print('------------------------------------')

numbers_list = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers_list)
print('------------------------------------')
numbers_list[2:-2] = [300, 4000, 5, 60000]
print(numbers_list)
print('------------------------------------')

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
list1 = characters[2: -3]
print(list1)
print('------------------------------------')
list2 = characters[:4]
print(list2)
print('------------------------------------')
list3 = characters[2:]
print(list3)
print('------------------------------------')
characters[2:5] = ['C', "D", 'E', 'C', 'D', 'E', 'X', 'Y', 'Z']
print(characters)
print('------------------------------------')

nums = [10, 20, 30, 40, 50, 60]

for i in range(len(nums)):
    nums[i] = int(nums[i] / 5)

print(nums)
print('------------------------------------')

nums = [10, 20, 30, 40, 50, 60]

for i in reversed(range(len(nums))):
    print(nums[i])

print('------------------------------------')

for x in nums[::-1]:  # same as previous one
    print(x)

print('------------------------------------')

for x in reversed(nums):
    print(x)

print('------------------------------------')

i = 0

while i < len(nums):
    print(nums[i])
    i += 1

print('------------------------------------')

for i in range(1, 6):
    i += 2
    print(i)

print('------------------------------------')

nums = [60, 500, 10, 20, 15, 5, 0]
nums.sort(reverse=True)
print(nums)
nums.sort()
print(nums)

print('------------------------------------')

list1 = [10, 20, 30, 40]
list1.reverse()
print(list1)

print('------------------------------------')

tuple_elements = ('Java', 'Python', 'C#', 'Ruby')
print(tuple_elements)
list_elements = list(tuple_elements)
print(list_elements)
list_elements[-2] = 'C++'
print(list_elements)
list_elements.append('SWIFT')
print(list_elements)
tuple_elements = tuple(list_elements)
print(tuple_elements)

print('------------------------------------')

list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
print(list1 is list2)

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1, 2, 3, 4, 5)
print(tuple1 is tuple2)

print('------------------------------------')

groceries_list = ['Eggs', 'Milk', 'Rice']
print(groceries_list)

groceries_list.append('Chicken')
print(groceries_list)

groceries_list.extend(('Beef', 'Oranges', 'Onion'))
print(groceries_list)

groceries_list.remove('Beef')
print(groceries_list)

groceries_list.pop()
print(groceries_list)

groceries_list.pop(1)
print(groceries_list)

groceries_list.insert(2, 'Apple')
print(groceries_list)

print( groceries_list.index('Eggs'))

print('------------------------------------')

nums = [1, 2, 3, 4, 5, 1, 1, 1, 1, 1]
print(f'one is repeating {nums.count(1)} times')

print('------------------------------------')

print('--------------- Comprehensions -------------------------')

nums = []

for x in range(1, 51):
    nums.append(x)

print(nums)

print('------------------------------------')

divisible_by_5 = []

for x in nums:
    if x % 5 == 0:
        divisible_by_5.append(x)

print(divisible_by_5)

#OR

divisible_by_5 = tuple([x for x in nums if x % 5 == 0])
print(divisible_by_5)

print('------------------------------------')

even_nums = [x for x in nums if x % 2 == 0]
odd_nums = [x for x in nums if x % 2 != 0]

print(f'Even number are => {even_nums}')
print(f'Odd number are => {odd_nums}')

print('------------------------------------')

names = ['Python', 'Java', 'Java', 'JavaScript', 'java', 'JaVA', 'Ruby']

distracting_java = [x for x in names if x.lower() != 'java']
print(f'Languages without java are  => {distracting_java}.')
