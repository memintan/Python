days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", 1, 2, 3, 4, 5, 6, 7, True, False)

print(type(days))
print(len(days))

print(days)

print(days[0])
print(days[-1])

days = ('Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

work_days = days[:4]
print(work_days)

weekend = days[-3:]
print(weekend)

reversed_tuple1 = days[::-1]
print(reversed_tuple1)
