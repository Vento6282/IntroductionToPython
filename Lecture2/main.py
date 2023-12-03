# Создание списков
list_1 = []
list_1 = list()
list_1 = [1, 5, 9, 7]
print("----------")

# Вывод массива
print(list_1)
print(*list_1) # Вывод без [] и запятых
for i in list_1:
    print(i)
print("----------")

# Размер списка
print(len(list_1))
print("----------")

# Добавить элемент в список
list_1.append(11)
print(list_1)
list_1.append(7)
print(list_1)
list_1.append(8)
print(list_1)
list_1.append(2)
print(list_1)
print("----------")

# Удаление элементов
print(list_1)
list_1.pop() # Удаление последнего элемента
print(list_1)
list_1.pop(1) # Удаление элекента по индексу
print(list_1)
print("----------")

# Добавление элемента на конкретную позицию
print(list_1)
list_1.insert(2, 555) # (индекс позиции, значение)
print(list_1)
print("----------")

# Срезы
print(list_1[0])     # Вывод первого элемента (индекс с начала)
print(list_1[-1])    # Вывод последнего элемента (индекс с конца)
print(list_1[1:4])   # Вывод со второго элемента по пятый (не включен в вывод)
print(list_1[1:5:2]) # Вывод со второго элемента по пятый (не включен в вывод) с шагом два
print(list_1[::3])   # Вывод каждого третьего элемента
print("----------")

# Создание кортежа
k = ()
print(type(k))
k = (1, 5, 9, 7)
print(type(k))

# Вывод кортежа
for i in k:
    print(i)
print("----------")
for i in range(len(k)):
    print(k[i])
print("----------")

# Изменение элемента
# k[0] = 33 выдаст ошибку

# Создание словарей
d = {}
d = dict()
d['q'] = 'qwerty'
d['w'] = 'wasd'
print(d)
print("----------")

# Удаление элемента словаря по ключу
print(d)
del d['q']
print(d)
d['d'] = 'dworak'
d['z'] = 'zxc'
print("----------")

# Вывод словаря
for item in d:
    print(item) # вывод только ключей
print("----------")
for item in d:
    print('{} : {}'.format(item, d[item]))
print("----------")
for k,v in d.items():
    print(k, v)
print("----------")

# Создание множеств
colors = {'red', 'green', 'blue'}
print(colors)          # {'red', 'green', 'blue'}
colors.add('red')      # не добавит, т.к. уже есть такой элемент, но ошибку не выдаст  
print(colors)          # {'red', 'green', 'blue'}
colors.add('gray')
print(colors)          # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors)          # {'green', 'blue','gray'}
# colors.remove('red') # выдаст ошибку
colors.discard('red')  # не выдаст ошибку
print("----------")

# Операции с множествами
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {8, 2, 5}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13}
print("----------")

# Генерация списоков
# Создать список чисел от 1 до 100
list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1) # [1, 2, 3,..., 100]
# Тоже самое, используя генератор списков
list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
# Добавить условие (только чётные числа)
list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
# Допустим, вы решили создать пары каждому из чисел (кортежи)
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),..., (100, 100)]
# Также можно умножать, делить, прибавлять, вычитать. Например, умножить значение на 2.
list_1 = [i * 2 for i in range(10) if i % 2 == 0] # [0, 4, 8, 12, 16]