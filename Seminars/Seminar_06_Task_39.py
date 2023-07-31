# Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
# Пользователь вводит число N - количество элементов в первом массиве, 
# затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. 
# Затем элементы второго массива

from random import randint

n = 10
m = 10
list_1 = [randint(1, 20) for _ in range(n)]

list_2 = [randint(1, 20) for _ in range(m)]
list_3 = []

print(list_1)
print(list_2)

for i in list_1:
    if i not in list_2:
        list_3.append(i)

print(list_3)

from random import randint

n_of_list_1 = int(input('Введите кол-во чисел 1 списка: '))
list_1 = [randint(0,5) for _ in range(n_of_list_1)]
n_of_list_2 = int(input('Введите кол-во чисел 2 списка: '))
list_2 = [randint(0,5) for _ in range(n_of_list_2)]
print(f'1ый набор чисел: {list_1}')
print(f'2ой набор чисел: {list_2}')

list_3 = []
for item in list_1:
    if item not in list_2:
        list_3.append(item)
print(list_3)