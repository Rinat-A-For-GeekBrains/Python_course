# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.

from random import randint

# n = 10
# list_1 = [randint(1, 20) for _ in range(n)]
# count = 0

# for i range(n):

my_list = [1, 2, 3, 2, 4, 1, 5, 2]
duplicates = []

for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print("Повторяющиеся элементы в списке:", duplicates)

from random import randint

n = 10
list_1 = [randint(1, 10) for _ in range(n)]
list_2 = []
count = 0

print(list_1)

for item in list_1:
    if list_1.count(item) > 1 and item not in list_2:
        list_2.append(item)

print(len(list_2))