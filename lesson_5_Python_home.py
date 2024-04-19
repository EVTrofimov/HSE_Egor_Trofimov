# домашнее задание 9


# 0 --- импортируем модули

import random
from datetime import datetime


# 1 --- Сгенерируйте с использованием функции range (случайный шаг от 3 до 5) массив, содержащий отсортированные числа от 10 до 250 млн.

list_1 = [10]

while list_1[-1] <= 250000000:
    i = list_1[-1] + random.randint(3, 5)
    list_1.append(i)

list_1.pop()

print(f'первые и последние 10 чисел: {list_1[:10] + list_1[-10:]}\nдлина массива: {len(list_1)}\n')


# 2 --- Сгенерируйте с помощью list comprehensions и функции randomint (встроенный модуль random) 10 случайных чисел.

list_2 = [random.randint(0, 99) for i in range (0, 10)]

print(f'случайные числа: {list_2}\nдлина массива: {len(list_2)}\n')


# 3 --- Напишите функцию для алгоритма линейного поиска.

def find_lin(mylist, myint):

    indicator = False
    
    for i in range(0, len(mylist), 1):

        if myint == mylist[i]:
            print(f'число {myint} найдено в массиве')
            indicator = True
            break

    if indicator == False:
        print(f'число {myint} не найдено в массиве')


# 4 --- Напишите функцию для алгоритма бинарного поиска.

def find_bin(mylist, myint):

    while mylist:

        i = (len(mylist)-1)//2

        if myint == mylist[i]:
            print(f'число {myint} найдено в массиве')
            break

        elif len(mylist) < 2:
            break

        elif myint < mylist[i]:
            mylist = mylist[:i]

        else:
            mylist = mylist[(i+1):]

    if myint != mylist[i]:
        print(f'число {myint} не найдено в массиве')


# 5 --- Проверьте наличие ранее сгенерированных случайных чисел в массиве с помощью алгоритмов линейного и бинарного поиска, замерьте время

def func_imput_num():
    
    myint = None

    while not myint:
        myint = input('введите число от 10 до 250 млн: ')

        try:

            myint = int(myint)

            if myint < 10 or myint > 250000000:
                myint = None
    
        except:
            myint = None

    return myint


print('проверка наличия ранее сгенерированных случайных чисел в массиве с помощью алгоритма линейного поиска')

myint = func_imput_num()
start = datetime.now()
print(f'начало поиска: {start}')        
find_lin (list_1, myint)
final = datetime.now()
print(f'окончание поиска: {final}')
print(f'продолжительность поиска: {final - start}\n')


print('проверка наличия ранее сгенерированных случайных чисел в массиве с помощью алгоритма бинарного поиска')

myint = func_imput_num()
start = datetime.now()
print(f'начало поиска: {start}')        
find_bin (list_1, myint)
final = datetime.now()
print(f'окончание поиска: {final}')
print(f'продолжительность поиска: {final - start}\n')
