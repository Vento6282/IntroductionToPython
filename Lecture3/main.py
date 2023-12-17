# функция без возвращения результата
def sum_numbers(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    print(summa)
sum_numbers(5)
print('---------------------------------------------------------------')
# функция возвращает результат
def sum_numbers(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa # return завершает выполнение программы
print(sum_numbers(5))
print('---------------------------------------------------------------')
# функция со значением по умолчанию
def sum_numbers(n, y = "Hello"):
    print(y)
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa # return завершает выполнение программы
print(sum_numbers(5))
print(sum_numbers(5, "Hell"))
print('---------------------------------------------------------------')
# функция, которая может принимать неограниченное количество значений
def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res # return завершает выполнение программы
print(sum_str('q', 'w', 'e'))
print(sum_str('q', 'w', 'e', 'r', 't', 'y'))
print('---------------------------------------------------------------')
# Использование модуля. В этой же папке создан файл modul1.py
import modul1
print(modul1.max1(5,9))

import modul1 as m1
print(m1.max1(52,91))

from modul1 import max1
print(max1(10,3))

from modul1 import *
print(max1(15,6))
print('---------------------------------------------------------------')
print("Рекурсия:") 
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n-1) + fib(n-2)
list_1 = []
for i in range(1,10):
    list_1.append(fib(i))
print(list_1)
print('---------------------------------------------------------------')
print('Быстрая сортировка:')
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
print (quick_sort([2,5,3,1,3,2]))
print('---------------------------------------------------------------')
print('Сортировка слиянием:')
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
list_1 = [3, 6, 9, 2, 5, 1, 7, 3, 9, 4, 1, 3]
merge_sort(list_1)
print(list_1)