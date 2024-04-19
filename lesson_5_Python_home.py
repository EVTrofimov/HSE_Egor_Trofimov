#!/usr/bin/env python
# coding: utf-8

# # домашнее задание 9
# 
# 1. Сгенерируйте с использованием функции range (случайный шаг от 3 до 5)
# массив, содержащий отсортированные числа от 10 до 250 млн.
# 
# Можно использовать функцию randomint из модуля random для ещё большей
# рандомизации значений, но для целей работы алгоритма бинарного поиска
# проследите, чтобы значения в массиве были отсортированы.
# 
# 2. Сгенерируйте с помощью list comprehensions и функции randomint
# (встроенный модуль random) 10 случайных чисел.
# 
# 3. Напишите функцию для алгоритма линейного поиска.
# 
# 4. Напишите функцию для алгоритма бинарного поиска.
# 
# 5. Проверьте наличие ранее сгенерированных случайных чисел в массиве
# с помощью алгоритмов линейного и бинарного поиска, замерьте время
# 

# In[1]:


# 0 --- импортируем модуль

import random

random.randint(3, 5)

list = [1,2,3,4,5,6]
list[-1]


# In[14]:


# 1 --- Сгенерируйте с использованием функции range (случайный шаг от 3 до 5) массив, содержащий отсортированные числа от 10 до 250 млн.

list_1 = [10]

while list_1[-1] <= 250000000:
    i = list_1[-1] + random.randint(3, 5)
    list_1.append(i)

list_1.pop()

print('первые и последние 10 чисел: ', list_1[:10] + list_1[-10:], '\nдлина массива: ', len(list_1))


# In[33]:


# 2 --- Сгенерируйте с помощью list comprehensions и функции randomint (встроенный модуль random) 10 случайных чисел.

list_2 = [random.randint(0, 99) for i in range (0, 10)]

print(f'случайные числа: {list_2}\nдлина массива: {len(list_2)}')


# In[37]:


# 3 --- Напишите функцию для алгоритма линейного поиска.

def find_bin(mylist, myint):

    while mylist:

        i = len(mylist)//2

        if myint == mylist[i]:

            print(f'число {myint} найдено в массиве')
            break

        elif len(mylist) == 1:
            break

        elif myint < mylist[i]:
            mylist = mylist[:i]

        else:
            mylist = mylist[(i + 1):]

    if myint != mylist[i]:
        print(f'число {myint} не найдено в массиве')

myint = None

while not myint:

    myint = input('введите число от 10 до 250 млн')
    
    try:
        myint = int(myint)
        if myint < 10 or myint > 250000000:
            myint = None
    
    except:
        myint = None
    
    if myint 
    
find_bin (list_1, 16)


# In[45]:


# 4 --- Напишите функцию для алгоритма бинарного поиска.

def find_bin(mylist, myint):

    while mylist:

        i = len(mylist)//2

        if myint == mylist[i]:

            print(f'число {myint} найдено в массиве')
            break

        elif len(mylist) == 1:
            break

        elif myint < mylist[i]:
            mylist = mylist[:i]

        else:
            mylist = mylist[(i+1):]

    if myint != mylist[i]:
        print(f'число {myint} не найдено в массиве')

myint = None

while not myint:

    myint = input('введите число от 10 до 250 млн: ')
    
    try:
        myint = int(myint)
        if myint < 10 or myint > 250000000:
            myint = None
    
    except:
        myint = None
    
find_bin (list_1, myint)



# In[43]:


5. Проверьте наличие ранее сгенерированных случайных чисел в массиве
с помощью алгоритмов линейного и бинарного поиска, замерьте время




# In[ ]:




