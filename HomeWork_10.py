# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

print("Введите число монет")    
n = int (input())
k = 0
for i in range(n):
    v = int(input())
    if v == 1:
        k += 1
if k<n/2:
    print(k)
else:
    print(n-k)
dict = {1:2}
a = dict[0]
print(type (a))

        