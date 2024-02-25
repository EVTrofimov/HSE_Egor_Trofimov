#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# домашнее задание 3


# In[ ]:


"""
1. Создайте ряд функций для проведения математических вычислений:

а) функция вычисления факториала числа (произведение натуральных чисел от 1 до n).
Принимает в качестве аргумента число, возвращает его факториал;

б) поиск наибольшего числа из трёх. Принимает в качестве аргумента кортеж из трёх чисел, возвращает наибольшее из них;

в) расчёт площади прямоугольного треугольника. Принимает в качестве аргумента размер двух катетов треугольника.
Возвращает площадь треугольника


2. Создайте функцию для генерации текста с адресом суда.
Функция должна по шаблону генерировать шапку для процессуальных документов с реквизитами сторон для отправки
"""


# In[ ]:


# 1 --- факториал

print('Вычисление факториала f(x)=x! через определение регрессионной функции.')

def factorial(n):
    factorial = 1
    if n > 0:
        for i in range(1, n + 1, 1):
            factorial = factorial * i
    return factorial

while True:
    try:
        n = int(input('Введите целое неотрицательное число (без точки) для вычисления факториала: '))
        if n >= 0:
            break
    except ValueError:
        print('Неверный ввод данных!')

print(f'{n}! = {factorial(n)}')


# In[ ]:


# 2 --- наибольшее число

print('Вычисление наибольшего числа из трех заданных.')

def maximum(x):
    max = x[0]
    for i in x:
        if max < i:
            max = i
    return max

list1 = []

for i in range (3):
    while True:
        n = input('Введите число: ')
        try:
            x = int(n)
            list1.append(x)
            break
        except ValueError:
            try:
                x = float(n)
                list1.append(x)
                break
            except ValueError:
                print('Неверный ввод данных!')

tuple1 = tuple(list1)

print(f'Максимальное число в кортеже {tuple1}: {maximum(tuple1)}')


# In[ ]:


# 3 --- вычисление площади прямоугольного треугольника

print('Вычисление площади прямоугольного треугольника по двум катетам.')

def triangle_area(x):
    area = 0.5
    for i in x:
        area = area * i
    return area

list1 = []

for i in range (2):
    while True:
        n = input(f'Введите длину катета № {i + 1}: ')
        try:
            x = int(n)
            list1.append(x)
            break
        except ValueError:
            try:
                x = float(n)
                list1.append(x)
                break
            except ValueError:
                print('Неверный ввод данных!')

print(f'Площадь прямоугольного треугольника с катетами длиной {list1[0]} и {list1[1]} равна {triangle_area(list1)}')


# In[ ]:


# 4 --- функция для генерации заголовка обращения в суд

get_ipython().system('pip install requests')

import requests, time

def save_www_file(link):
    filename = link.split('/')[-1]
    req = requests.get(link, allow_redirects = True)
    open(filename, "wb").write(req.content)
    return

link = 'https://raw.githubusercontent.com/sirotinsky/HSE_LegalPy/main/homeworks/lesson2/lesson_2_data.py'

save_www_file(link)

from lesson_2_data import courts, respondents

def print_title(plaintiff, defendant, court):
    title_list = []
    for i in defendant:
        try:
            title_current = court[i['case_number'][0:3]]['court_name'] + '\n'
            title_current = title_current + court[i['case_number'][0:3]]['court_address'] + '\n' + '\n'
            title_current = title_current + plaintiff + '\n' + '\n'
            title_current = title_current + 'Ответчик:\n' + i['short_name'] + '\n'
            title_current = title_current + i['inn'] + ' ' + i['ogrn'] + '\n'
            title_current = title_current + i['address'] + '\n'
            print('============================' + '\n' + title_current + '============================' + '\n')
            title_list.append(title_current)
        except KeyError:
            print('\n' + '...............' + '\n' + 'Неполные данные' + '\n' + '...............' + '\n')
        time.sleep(0.3)
    return title_list

print_title("Истец:\nТрофимов Егор Викторович\nИНН 272312345678 ОГРНИП 308272312345678\nАдрес: 199178, г. Санкт-Петербург, Невский пр-кт, 1",
            defendant = respondents,
            court = courts
)

print(title_list)

