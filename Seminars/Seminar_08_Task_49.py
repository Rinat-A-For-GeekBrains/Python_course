# Задача №49. Общее обсуждение
# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться 
# в файле.
# 1. Программа должна выводить данные 
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной 
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# выводить все контакты на экран
# добавить контакт
# удалить контакт
# изменить контакт
# найти контакт
# открыть или сохранить
# выход

# file = open("slovar.txt", "r+", encoding = "UTF-8")
# #file.write("ghkjgdt")
# #file.close()
# #Ф И О:тел:Коментарий
# list1=list()
# def input_line(str):
#     str=input("Введите Ф И О:тел:Коментарий:")
#     file.write(f"\n{str}")
#     return str
# def sortorov(str):
#     str=input("Введите Ф И О:")
#     if str in file.read():
#         print("Нашел")    
#         return str
# sortorov(str)

#input_line(str)

# file.close()

# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Решение:
# Показывает информацию в файле

def show_data(filename):
    print("\nПП| ФИО | Телефон")
    with open(filename, "r", encoding="utf-8") as data:
        print(data.read())
        print("")

# Записывает информацию в файл

def add_data(filename):
    with open(filename, 'r', encoding="utf-8") as data:
        tel_file = data.read()
        num = len(tel_file.split("\n"))
    with open(filename, 'a', encoding='utf-8') as data:
        fio = input('Введите ФИО: ')
        phone_number = input('Введите номер телефона: ')
        data.write(f'{num} | {fio} | {phone_number}\n')
        print(f'Добавлена запись : {num} | {fio} | {phone_number}\n')

# Изменяет информацию из файла

def edit_data(filename):
    print('\nПП | ФИО | Телефон')
    with open(filename, "r", encoding='utf-8') as data:
        tel_book = data.read()
        print(tel_book)
        print("")
        index_delete_data = int(input('Введите номер строки для редактирования: ')) - 1
        tel_book_lines = tel_book.split('\n')
        edit_tel_book_lines = tel_book_lines[index_delete_data]
        elements = edit_tel_book_lines.split(' | ')
        fio = input('Введите ФИО: ')
        phone = input("Введите номер телефона: ")
        num = elements[0]
    if len(fio) == 0:
        fio = elements[1]
    if len(phone) == 0:
        phone = elements[2]
    edited_line = f"{num} | {fio} | {phone}"
    tel_book_lines[index_delete_data] = edited_line
    print(f'Запись — {edit_tel_book_lines}, изменена на — {edited_line}\n')
    with open(filename, "w", encoding='utf-8') as f:
        f.write('\n'.join(tel_book_lines))

# Поиск записи в файле

def find_data(filename):
       
    with open(filename, "r", encoding='utf-8') as data:
        tel_book = data.read()
        resultSearch = 'Нет совпадений'
        tel_book_lines = tel_book.split('\n')
        find_tel_book_line = input("Введите искомое: ")
        for i in tel_book_lines:
            if find_tel_book_line in i:
                resultSearch = i
        
        print(resultSearch)
            
        
 # Удаляет информацию из файла

def delete_data(filename):
    print('\nПП | ФИО | Телефон')
    with open(filename, "r", encoding='utf-8') as data:
        tel_book = data.read()
        print(tel_book)
        print('')
        index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
        tel_book_lines = tel_book.split('\n')
        del_tel_book_lines = tel_book_lines[index_delete_data]
        tel_book_lines.pop(index_delete_data)
    print(f'Удалена запись: {del_tel_book_lines}\n')
    with open(filename, 'w', encoding='utf-8') as data:
        data.write('\n'.join(tel_book_lines))

def main():
    my_choice = -1
    file_tel = "tel.txt"

# Создает файл если его нет в папке

    with open(file_tel, "a", encoding='utf-8') as file:
        file.write("")

    while my_choice != 0:
        print("Выберите одно из действий:")
        print("1 — Вывести инфо на экран")
        print("2 — Записать данные")
        print("3 — Изменить данные")
        print("4 — Удаление данных")
        print("5 — Найти данные")
        print("0 — Выход из программы")
        action = int(input('Действие: '))
        if action == 1:
            show_data(file_tel)
        elif action == 2:
            add_data(file_tel)
        elif action == 3:
            edit_data(file_tel)
        elif action == 4:
            delete_data(file_tel)
        elif action == 5:
            find_data(file_tel)
        else:
            my_choice = 0
            print("До свидания")

# if name == "main":
main()