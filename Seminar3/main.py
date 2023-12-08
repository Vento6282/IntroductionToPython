# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# import random
# m = int(input("Введите количество чисел: "))
# numbers_list = []
# numbers_set = set()
# for i in range(m):
#     number = random.randint(-5,5)
#     numbers_list.append(number)
#     numbers_set.add(number)
# print(numbers_list)
# print(len(numbers_set))
# ------------------------------------------------------------------------
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю 
# последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# import random
# n = int(input("Введите количество чисел: "))
# k = int(input("Введите число, на которое нужно сдвинуть ряд: "))
# numbers_list = []
# for i in range(n):
#     number = random.randint(1,10)
#     numbers_list.append(number)
# print(numbers_list)
# for i in range(k):
#     numbers_list.insert(0, numbers_list[len(numbers_list)-1])
#     numbers_list.pop(len(numbers_list)-1)
# print(numbers_list)
# ------------------------------------------------------------------------
# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Решение 1
list_dicts = [{"V": "S002"}, {"V": "S001", " VIII":" S007"}, {"VI": " S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "},
{" VIII":" S007"}]

# unique_values = set()
#
# for cur_dict in list_dicts:
# for key in cur_dict:
# unique_values.add(cur_dict[key].strip())
#
# print(unique_values)

# Решение 2

# unique_values = set()
#
# for cur_dict in list_dicts:
#   for key in cur_dict.keys():
#       unique_values.add(cur_dict[key].strip())
#
# print(unique_values)

# Решение 3

# unique_values = set()
#
# for cur_dict in list_dicts:
#   for value in cur_dict.values():
#       unique_values.add(value.strip())
#
# print(unique_values)

# Решение 4

# unique_values = set()
#
# for cur_dict in list_dicts:
#    unique_values.add(*cur_dict.values())
#
# print(unique_values)

# Решение 5

# unique_values = set()

# for cur_dict in list_dicts:
#     unique_values.update(cur_dict.values())

# print(unique_values)
# ------------------------------------------------------------------------
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# import random
# qty = int(input("Введите количество целых чисел: "))
# numbers = []
# result = ''
# count = 0
# for i in range(qty):
#     numbers.append(random.randint(-10, 10))
#     if i > 0:
#         if numbers[i] > numbers[i-1] and count == 0:
#             result = result + str(numbers[i-1]) + ' < ' + str(numbers[i])
#             count = count + 1
#         elif numbers[i] > numbers[i-1]:
#             result = result + ' , ' + str(numbers[i-1]) + ' < ' + str(numbers[i])
#             count = count + 1
# print(numbers)
# print(f"{count} ( {result} )")