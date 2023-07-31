# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

Min = int(input('Введите минимальное значение диапазона значений: '))
Max = int(input('Введите максимальное значение диапазона значений: '))

list_input = [random.randint(1,10) for _ in range(20)]
List_output =[]

print(list_input)

for i in range(0, len(list_input)):
    if Min < list_input[i] < Max:
        List_output.append(i)

# List_output = [i in range (0, len(list_input)) if Min < list_input[i] < Max] # не домучал, где ошибка

print (List_output)

