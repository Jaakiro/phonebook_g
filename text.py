main_menu = ['Главное меню',
             'Открыть файл',
             'Сохранить файл',
             'Показать контакты',
             'Создать контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Выход']

main_menu_choice = 'Выберите пункт меню: '
load_successful = 'Телефонная книга успешно загружена!'
save_successful = 'Телефонная книга успешно сохранена!'

empty_phone_book = 'Телефонная книга пуста или не открыта!'

new_contact = ['Введите имя: ',
               'Введите номер телефона: ',
               'Введите комментарий: ']


def new_contact_added_successful(name: str) -> str:
    return f'Контакт {name} успешно добавлен!'


input_search_word = 'Введите слово для поиска: '


def contacts_not_found(word: str) -> str:
    return f'Контакт содержащий {word} не найден'


input_id_change_contact = 'Введите ID контакта, который хотите заменить: '


change_contact = ['Введите новое имя или ENTER, оставляем без изменений: '
                'Введите новый номер телефона или ENTER, оставляем без изменений: '
                'Введите новый комментарий или ENTER, чтобы оставить без изменений: ']


def contact_changed_successful(name: str) -> str:
    return f'Контакт {name} успешно изменен!'


input_id_delete_contact = 'Введите ID контакта который удалить: '


def contact_deleted_successful(name: str) -> str:
    return f'Контакт {name} успешно удален!'


good_bay = 'До свидания'