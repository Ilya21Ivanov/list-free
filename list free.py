import random

lst = []
for lst1 in range(random.randint(3, 10)):
    lst.append(random.randint(1, 100))

lst2 = [lst[0], lst[2], lst[-2]]

print(lst)
print(lst2)