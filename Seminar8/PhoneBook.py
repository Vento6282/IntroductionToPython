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
# 6) Копирование контакта в другой файл                        +++
#     - вывести список контактов                               +++
#     - добавить возможность выхода из режима копирования      +++
#     - запросить информацию для копирования:                  +++
#         а) номер записи                                      +++
#         б) имя файла                                         +++
#     - реализовать проверку имени файла на допустимые символы +++
#     - записать контакт в новый файл                          +++


import re

def input_name():
    name = input('Введите имя: ')
    if name == '':
        name = 'default_имя'
    return name

def input_surname():
    surname = input('Введите фамилию: ')
    if surname == '':
        surname = 'default_фамилия'
    return surname

def input_patronymic():
    patronymic = input('Введите отчество: ')
    if patronymic == '':
        patronymic = 'default_отчество'
    return patronymic

def input_phone():
    phone = input('Введите номер телефона: ')
    if phone == '':
        phone = 'default_012345'
    return phone

def input_address():
    address = input('Введите адрес: ')
    if address == '':
        address = 'default_адрес'
    return address

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
    is_empty_show_info = show_info()
    if is_empty_show_info == 1:
        numbers_contacts_list = []
        with open('phonebook.txt', 'r', encoding='UTF-8') as file:
            contacts_list = file.read().rstrip().split('\n\n')
            contacts_list.append('Выход из режима копирования')
            print(f'{len(contacts_list)} Выход из режима копирования')
            if len(contacts_list) > 0:
                for nn, contact in enumerate(contacts_list,1):
                    numbers_contacts_list.append(str(nn))
                copy_index = input('Введите номер контакта, который необходимо копировать: ')
                while copy_index not in numbers_contacts_list:
                    print('Контакта с таким номером не существует!')
                    copy_index = input('Введите номер контакта, который необходимо копировать: ')
                if copy_index == str(len(numbers_contacts_list)):
                    print('Выход из режима копирования')
                else:
                    file_name = input('Введите имя файла: ')
                    forbidden_file_name = 1
                    for i in file_name:
                        if i in '''\\/:*?"<>|+''' or file_name.endswith('.'): 
                            forbidden_file_name = 1
                            print('Введён недопустимый символ!')
                            file_name = input('Введите имя файла: ')
                        else:
                            forbidden_file_name = 0
                    while forbidden_file_name == 1: 
                        for i in file_name:
                            if i in '''\\/:*?"<>|+''' or file_name.endswith('.'): 
                                forbidden_file_name = 1
                                print('Введён недопустимый символ!')
                                file_name = input('Введите имя файла: ')
                            else:
                                forbidden_file_name = 0
                    file_name += '.txt'
                    with open(file_name, 'a', encoding='UTF-8') as file:
                        file.write(f'{contacts_list[int(copy_index)-1]}\n\n')
                    print(f'Контакт скопирован в файл {file_name}') 

def show_info():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        if contacts_list[0] == '':
            print('Телефонная книга пуста!')
            return 0
        else:
            for contact in enumerate(contacts_list,1):
                print(*contact)
            return 1
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
            '2. Копировать контакт в другой файл\n'
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