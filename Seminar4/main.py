# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
print("Задача 1")
strIn = "a a a b c a a d c d d"
d = {}
strResult = ""
for i in strIn.split():
    if d.get(i) == None:
        d[i] = 0
        strResult += i + " "
    else:
        d[i] = d.get(i) + 1
        strResult += i + "_" + str(d.get(i)) + " "
print(strResult)
print("--------------------------------")
# -----------------------------------------------------------------------------------------
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13
print("Задача 2")
strIn = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
words = set()
for i in strIn.split():
    words.add(i.lower())
print(len(words))
# words.clear
print("--------------------------------")
# -----------------------------------------------------------------------------------------
# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.