#Задача 2: Найдите сумму цифр трехзначного числа.
#*Пример:* 123 -> 6 (1 + 2 + 3)   100 -> 1 (1 + 0 + 0) |


# number = int (input ('Введите трехзначное число: '))
# sum = 0
# while (number > 0):
#     i = number % 10
#     sum = sum + i
#     number //= 10
# print (sum)


# 2 способ

# number = str (input ('Введите трехзначное число: '))
# n = len(number)

# sum = 0 
# i = 0

# while (i<n):
#     sum += int (number[i])
#     i += 1
# print(sum)


# 3 Способ

# number = int (input ('Введите трехзначное число: '))

# result = number % 10 + number % 100 // 10 + number // 100
# print (result)



#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, а 
# Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#*Пример:*   6 -> 1  4  1     24 -> 4  16  4          60 -> 10  40  10


# S = int (input ('Введите общее количество журавликов: '))
# Kate = int((S*4)//6)
# Pete = int(S//6)
# Sergey = int(Pete)
# print (f'Петя сделал {Pete} журавликов, Катя сделала {Kate}, а Сергей {Sergey}')




#Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за 
# проезд и получали билет с номером. Счастливым билетом называют такой билет 
# с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*     385916 -> yes     123456 -> no

# number = int (input ('Введите шестизначный номер билета: '))

# if ((number//100000) + ((number // 10000) % 10) + ((number // 1000) % 10)) == (((number // 100) % 10) + ((number // 10) % 10) + (number % 10)):   
#     print ('Билет счастливый')
# else:
#     print ('Билет обычный')





#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить 
# k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*   3 2 4 -> yes     3 2 1 -> no


# n = int (input ('Введите число n: '))
# m = int (input ('Введите число m: '))
# k = int (input ('Введите число k: '))

# if (n % k == 0 or m % k == 0) and (k < n*m):
#     print ('Yes')
# else:
#     print ('No')



#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть


# coins = [0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1]
# if coins.count(0) < coins.count(1):
#     print(coins.count(0)) 
# else:
#     print (coins.count(1))



#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные 
# Петей числа.



# S = int (input ('Введите сумму чисел: '))
# P = int (input ('Введите произведение чисел: '))
# j = 0
# for x in range(S + P):
#     if j:
#         break
#     for y in range(S + P):
#         if x + y == S and x * y == P:
#             c = 1
#             print (f'x = {x}, y = {y}')
#             break



#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N

# N = int(input('Введите число: '))
# p = 1
# while p <= N:
#     print(p, end=' ')
#     p *= 2




#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#*Пример:*
#5     1 2 3 4 5      3 -> 1

# from random import randint
# A = [randint(1, 9) for i in range(int(input('Введите размер массива: ')))]
# print(A)
# print('Встречается', A.count(int(input('Введите искомое число: '))), 'раз')



#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному 
# числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в 
# массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#*Пример:*
#5       1 2 3 4 5       6  -> 5

# from random import randint
# A = [randint(1, 9) for i in range(int(input('Введите количество элементов массива: ')))]
# print(A)
# number= int(input('Введите число: '))
# A = set(A)
# dif = 0
# if number > max(A):
#     print(max(A))
# elif number < min(A):
#     print(min(A))
# else:
#     while True:
#         if number - dif in A and number + dif in A and number - dif != number + dif:
#             print(number - dif, number + dif)
#             break
#         elif number - dif in A:
#             print(number - dif)
#             break
#         elif number + dif in A:
#             print(number + dif)
#             break
#         else:
#             dif += 1






#*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков. 
# Русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только 
# английские, либо только русские буквы.
#*Пример:*   ноутбук         12 очков

# scrable = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1, 
# 'А': 1, 'В': 1, 'Е': 1,'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1, 'D': 2, 'G': 2, 'Д': 2, 
# 'К': 2, 'Л': 2, 'М': 2, 'П': 2,'У': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'Б': 3, 'Г': 3, 'Ё': 3, 
# 'Ь': 3, 'Я': 3, 'F': 4, 'H': 4, 'V': 4,'W': 4, 'Y': 4, 'Й': 4, 'Ы': 4, 'K': 5, 'Ж': 5, 'З': 5, 
# 'Х': 5, 'Ц': 5, 'Ч': 5, 'J': 8, 'X': 8, 'Ш': 8,'Э': 8, 'Ю': 8, 'Q': 10, 'Z': 10, 'Ф': 10, 
# 'Щ': 10, 'Ъ': 10}
# word = str.upper(input('Введите слово: '))
# quantity = 0
# for i in word:
#     quantity += scrable[i]
# print(quantity, 'очков')



#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов 
# второго множества. Затем пользователь вводит сами элементы множеств. (Попробуйте использовать 
# множества и их пересечение)

# from random import randint
# n_set = set(randint(1, 10) for i in range(int(input('Введите кол-во элементов первого множества: '))))
# print(n_set)
# m_set = set(randint(1, 10) for i in range(int(input('Введите кол-во элементов второго множества: '))))
# print(m_set)
# s_set = sorted(n_set.intersection(m_set))
# print(*s_set)


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два 
# соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит 
# из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, 
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних 
# с ним. Напишите программу для нахождения максимального числа ягод, которое может собрать за один 
# заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.


# from random import randint
# list_1 = list(randint(1, 5) for i in range(int(input('Введите кол-во кустов: '))))
# print(list_1)
# a = int(input('Введите № куста: '))
# res = 0
# if a == 1:
#     res = list_1[0] + list_1[1] + list_1[-1]
# elif a == len(list_1):
#     res = list_1[-2] + list_1[-1] + list_1[0]
# else:
#     res = list_1[a-1] + list_1[a-2] + list_1[a]
# print(res, 'ягод')



#Задача 1 Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -. 
# Вычислите результат.
# Пример  Ввод 8-5+2-1  Вывод 4

# from operator import __sub__, __add__
# from functools import reduce
# import re
# expr = '8-5+2-1'
# opf = {'+':__add__, '-':__sub__}
# vals = list(map(int, re.split('[+-]', expr)))
# opl = iter(filter(lambda x:x in '+-', expr))
# print(reduce(lambda x, y: opf[next(opl)](x, y), vals))


# Задача 2 Словом в данной задаче считается последовательность букв, ограниченная пробелами 
# или началом или концом строки.
# Выведите все слова из строки в столбик. НЕЛЬЗЯ ПОЛЬЗОВАТЬСЯ МЕТОДАМИ СТРОК (split)
# Формат ввода Вводится строка.
# Формат вывода  Выведите слова из строки по одному.


# import re
 
# s = 'My heart in the Highland'
 
# s2 = re.sub(r'\s+', '\n', s)
# print(s2)


