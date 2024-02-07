#!/usr/bin/env python
# coding: utf-8

"""
1. Поработайте с переменными, создайте несколько, выведите на экран.
Запросите у пользователя некоторые числа и строки и сохраните в переменные,
а затем выведите на экран.
Используйте функции для консольного ввода input() и консольного вывода print(). 
Попробуйте также через встроенную функцию id() понаблюдать, какие типы объектов
могут изменяться и сохранять за собой адрес в оперативной памяти.
"""

# 1 --- целое число

int1 = 2
print(int1)
print(id(int1))
print(type(int1))

int1 = 3
print(int1)
print(id(int1))
print(type(int1))

int2 = int(input("Введите целое число: "))
print(int2)
print(id(int2))
print(type(int2))

# 2 --- число с плавающей точкой

float1 = 1.5
print(float1)
print(id(float1))
print(type(float1))

float1 = 2.5
print(float1)
print(id(float1))
print(type(float1))

# 3 --- значение 'ложь' в Булевой алгебре

bull0 = False
print(bull0)
print(id(bull0))
print(type(bull0))

# 4 --- значение 'истина' в Булевой алгебре

bull1 = True
print(bull1)
print(id(bull1))
print(type(bull1))

# 5 --- строка

string1 = 'ПРИВЕТ'
print(string1)
print(id(string1))
print(type(string1))
print(string1[0:2])

string1 = 'ПОКА'
print(string1)
print(id(string1))
print(type(string1))
print(string1[0:2])

string2 = input('Введите строку: ')
print(string2)
print(id(string2))
print(type(string2))

# 6 --- список

list1 = [123, 234, 345, 456, 567]
print(list1)
print(id(list1))
print(type(list1))
print(list1[0:2])

list1[0] = 321
print(list1)
print(id(list1))
print(type(list1))
print(list1[0:2])

# 7 --- множество

set1 = {1234, 2345, 3456, 4567, 5678}
print(set1)
print(id(set1))
print(type(set1))

set1.add(6789)
print(set1)
print(id(set1))
print(type(set1))

# 8 --- кортеж

tupple1 = (111, 222, 333, 444, 555)
print(tupple1)
print(id(tupple1))
print(type(tupple1))
print(tupple1[0:2])

# 9 --- словарь

dict1 = {'name': 'Egor', 'age': '43'}
print(dict1)
print(id(dict1))
print(type(dict1))

dict1['name'] = 'George'
print(dict1)
print(id(dict1))
print(type(dict1))


"""
2. Пользователь вводит время в секундах.
   Рассчитайте время и сохраните отдельно в каждую переменную количество часов,
   минут и секунд. Переведите время в часы, минуты, секунды и сохраните в отдельных переменных.
   Используйте приведение типов для перевода строк в числовые типы.
   Предусмотрите проверку строки на наличие только числовых данных
   через встроенный строковый метод .isdigit().
   Выведите рассчитанные часы, минуты и секунды по отдельности в консоль.
"""

# 10

time_sec = 'time_sec'
while time_sec.isdigit() == False:
    time_sec = input('Введите время в секундах: ')
time_sec = int(time_sec)
print('Время в секундах: ', time_sec)
hours=time_sec//3600
minutes=(time_sec-hours*3600)//60
seconds=time_sec-hours*3600-minutes*60
print('Часов: ', hours, '   Минут: ', minutes, '   Секунд: ', seconds)


"""
3. Запросите у пользователя через консоль число n (от 1 до 9).
   Найдите сумму чисел n + nn + nnn.
   Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
   Выведите данные в консоль.
"""

# 11

n = 'number'
while n.isdigit() == False or (n.isdigit() == True and (int(n)<1 or int(n)>9)):
    n = input('Введите число от 1 до 9: ')
print('n = ', n)
result = int(n)+int(n+n)+int(n+n+n)
print('n + nn + nnn = ', result)
