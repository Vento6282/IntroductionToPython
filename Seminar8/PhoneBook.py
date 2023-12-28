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
# 4) Поиск данных
#     - запросить вариант поиска у пользователя  
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
        
def show_info():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        print(file.read().rstrip())

def search_contact():

    var_search = input('Выберите варинат поиска: \n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Выход из программы')



    search = input('Введите данные для поиска: ')
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().split('\n\n')
    for contact_str in contacts_list:
        if search in contact_str:
            print(contact_str)

def interface():
    with open('phonebook.txt', 'a', encoding='UTF-8'):
        pass
    command = '-1'
    while command != '4':
        print('Возможные варианты взаимодействия:\n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Выход из программы')
        
        command = input('Введите пункт меню: ')
        
        while command not in ('1', '2', '3', '4'):
            print('Некорретные данные')
            command = input('Введите пункт меню: ')

        match command:
            case '1':   
                add_contact(create_contact())
            case '2':   
                show_info()
            case '3':   
                search_contact()
            case '4':   
                print('Всего хорошего!')
interface()