# Дан массив, состоящий из целых чисел. Напишите программу, 
# которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве 
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

from random import randint

n = 10
list_1 = [randint(1, 20) for _ in range(n)]
count = 0

for i in range(1, n-1):
    if list_1[i - 1] < list_1[i] and list_1[i+1] < list_1[i]:
        count += 1
print (list_1)
print (count)



# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива.
# Массив состоит из целых чисел.

from random import randint

n_of_list_1 = int(input('Введите кол-во чисел в списке: '))
list_1 = [randint(0,5) for _ in range(n_of_list_1)]

print(f'Набор чисел: {list_1}')

count = 0
for i in range(1, len(list_1)-1):
#    if list_1[i] > list_1[i-1] and list_1[i] > list_1[i+1]:
    if list_1[i - 1] < list_1[i] > list_1[i + 1]:
        count += 1
print(count)