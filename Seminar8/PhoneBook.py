# Задача №55. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# Этапы работы:
# 1) Создать телефонный справочник:              +++
#     - открыть файл в режиме добавления (a)     +++
# 2) Добавить контакт:                           +++
#     - запросить информацию у пользователя      +++
#     - подготовить данные в необходимом формате +++
#     - открыть файл в режиме добавления (a)     +++
#     - добавить контакт в файл                  +++
# 3) Вывести данные из файла на экран:           +++
#     - открыть файл в режиме чтения (r)         +++
#     - вывести информацию на экран              +++
# 4) Поиск данных                                +++
#     - запросить вариант поиска у пользователя  +++
#     - запросить информацию у пользователя      +++
#     - открыть файл в режиме чтения (r)         +++
#     - сохранить данные в переменную            +++
#     - осуществить поиск по файлу               +++
#     - вывести нужную информацию на экран       +++
# 5) Реализовать UI (user interface)             +++
#     - вывести варианты меню                    +++
#     - получение запроса от пользователя        +++
#     - реализация запроса от пользователя       +++
#     - выход из программы                       +++
import re

def input_name():
    return input('Введите имя: ')

def input_surname():
    return input('Введите фамилию: ')

def input_patronymic():
    return input('Введите отчество: ')

def input_phone():
    return input('Введите номер телефона: ')

def input_address():
    return input('Введите адрес: ')

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic}\n{address}\n\n'

def add_contact(contact):
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(contact)

def copy_contact():
    show_info()
    numbers_contacts_list = []
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        for nn, contact in enumerate(contacts_list,1):
            numbers_contacts_list.append(str(nn))
    print(numbers_contacts_list)

    copy_index = input('Введите номер контакт, который необходимо копировать: ')

    while copy_index not in numbers_contacts_list:
        print('Контакта с таким номер не существует!')
        copy_index = input('Введите номер контакт, который необходимо копировать: ')


def show_info():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        for contact in enumerate(contacts_list,1):
            print(*contact)
        # print(file.read().rstrip())
            
def search_contact():
    print(
        'Возможные варианты поиска:\n'
        '1. По фамилии\n'
        '2. По имени\n'
        '3. По отчеству\n'
        '4. По номеру телефона\n'
        '5. По адресу'
    )
    var_search = input('Выберите варинат поиска: ')
    
    while var_search not in ('1', '2', '3', '4', '5'):
        print('Некорретные данные')
        var_search = input('Выберите варинат поиска: ')

    index_var = int(var_search)-1

    search = input('Введите данные для поиска: ')

    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')

    for contact_str in contacts_list:
        contact_lst = re.split(" |\n", contact_str)
        if search in contact_lst[index_var]:
            print(contact_lst)

def interface():
    with open('phonebook.txt', 'a', encoding='UTF-8'):
        pass
    command = '-1'
    while command != '5':
        print('Возможные варианты взаимодействия:\n'
            '1. Добавить контакт\n'
            '2. Копировать контакт в новую телефонную книгу\n'
            '3. Вывести на экран\n'
            '4. Поиск контакта\n'
            '5. Выход из программы')
        
        command = input('Введите пункт меню: ')
        
        while command not in ('1', '2', '3', '4', '5'):
            print('Некорретные данные')
            command = input('Введите пункт меню: ')

        match command:
            case '1':   
                add_contact(create_contact())
            case '2':   
                copy_contact()                
            case '3':   
                show_info()
            case '4':   
                search_contact()
            case '5':   
                print('Всего хорошего!')
interface()