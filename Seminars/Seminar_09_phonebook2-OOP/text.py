menu = ['Главное меню',
         'Открыть файл',
        'Сохранить файл',
        'Показать контакты',
        'Создать контакт',
        'Найти контакт',
        'Изменить контакт',
        'Удалить контакт',
        'Выход']
input_menu = 'Выберите пункт меню: '

input_menu_error = f'Ввести число от 1 до {len(menu)-1}'

load_succesful = ' Телефонная книга загружена успешно'
save_succesful = ' Телефонная книга сохранена успешно'

empty_book_error = 'Телефонная книга пуста или не открыта'

def input_contact(new: bool = False) -> list[str]:
    add = 'или Enter, чтобы оставить без изменения ' if new else ''
    return [f'Введите имя нового контакта{add}: ',
                f'Введите номер телефона{add}: ',
                f'Введите комментарий{add}: ']

input_edit_contact = ['Введите имя нового контакта или Enter, чтобы оставить без изменения: ',
                'Введите номер телефона или Enter: ',
                'Введите комментарий или Enter: ']

input_search_word = 'Введите ключевое слово для поиска: '

input_edit_contact_id = 'Введите ID контакта, который хотите изменить: ' 

input_del_contact_id = 'Введите ID контакта, который хотите удалить: '

operation = ['создан', 'изменен','удален' ]

exit_program = 'До свидания, до новых встреч!'

def contact_action(name: str, action: str) -> str:
    return f'Контакт {name} успешно {action}!'

def not_find(word: str) -> str:
    return f'Контакты содержащие "{word}" не найдены'
