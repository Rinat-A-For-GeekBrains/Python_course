# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).

alpha = {'AEIOULNSTRАВЕИНОРСТ': 1,
         'DGДКЛМПУ': 2,
         'BCMPБГЁЬЯ': 3,
         'FHVWYЙЫ': 4,
         'KЖЗХЦЧ': 5,
         'JXШЭЮ': 8,
         'QZФЩЪ': 10}

word = input('Введите слово: ')
total = 0
new_alpha = {}
for letters, score in alpha.items():
    new_alpha.update(dict.fromkeys(letters, score))

for char in word.upper():
    total += new_alpha.get(char)

# for char in word.upper():
#     for letters, score in alpha.items():
#         if char in letters:
#             total += score

print(f'Слово {word} весит {total} очков')