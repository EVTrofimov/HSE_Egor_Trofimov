#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# домашнее задание 5

1. Найдите информацию об организациях.
a. Получите список ИНН из файла traders.txt.
b. Найдите информацию об организациях с этими ИНН в файле ntraders.json.
c. Сохраните информацию об ИНН, ОГРН и адресе организаций из файла traders.txt в файл traders.csv.


# In[ ]:


# 0 --- импортируем модули

import requests, re, csv


# In[ ]:


# 1 --- получаем список ИНН из файла traders.txt

# 1.1 --- определяем файл входящих данных с GitHub
file_inn = 'https://raw.githubusercontent.com/sirotinsky/HSE_LegalPy/main/homeworks/lesson3/traders.txt'

# 1.2 --- создаем запрос
response = requests.get(file_inn)

# 1.3 --- удаляем лишние символы с помощью регулярных выражений, преобразуем в список
inn_list = str(re.sub('[^0-9]', ' ', str(response.content))).split()

print(inn_list)


# In[ ]:


# 2 --- находим информацию об организациях с этими ИНН в файле traders.json

# 2.1 --- определяем файл входящих данных
file_companies = 'https://raw.githubusercontent.com/sirotinsky/HSE_LegalPy/main/homeworks/lesson3/traders.json'

# 2.2 --- определяем файл исходящих данных (загружаем на свой комп в текущую папку)
file_traders = 'traders.csv'

# 2.3 --- определяем искомые параметры организаций (списком)
list_head = ['inn', 'address', 'ogrn']

# 2.4 --- создаем запрос
response = requests.get(file_companies, allow_redirects = True)

# 2.5 --- преобразуем объект запроса в формат json (список компаний)
companies_list = response.json()

# 2.6 --- создаем функцию для поиска организации (в списке) по ИНН (в списке)
def find_companies(companies_list, inn_list, list_head):
    list_traders = []
    list_traders.append(list_head)
    for inn in range (0, len(inn_list)):
        for company in range (0, len(companies_list)):
            if companies_list[company]['inn'] == inn_list[inn]:
                current_trader = []
                for head in range (0, len(list_head)):
                    current_trader.append(companies_list[company][list_head[head]])
                list_traders.append(current_trader)
                print(current_trader)
                break
    return(list_traders)

# 2.7 --- исполняем авторскую функцию - для поиска организации (в списке) по ИНН (в списке)
list_traders = find_companies(companies_list, inn_list, list_head)
print(list_traders)


# In[ ]:


# 3 --- сохраняем информацию об ИНН, ОГРН и адресе организаций из файла traders.txt в файл traders.csv\n",

with open(file_traders, 'w', newline = '') as file:
    writer = csv.writer(file, dialect = 'excel', delimiter=';')
    writer.writerows(list_traders)


# In[ ]:


# 4 --- Напишите регулярное выражение для поиска email-адресов в тексте

# 4.1 --- определяем файл входящих данных
file_email = 'https://raw.githubusercontent.com/sirotinsky/HSE_LegalPy/main/homeworks/lesson3/1000_efrsb_messages.json'

# 4.2 --- определяем файл исходящих данных (загружаем на свой комп в текущую папку)
file_traders = 'emails.json'

# 4.3 --- создаем запрос
response = requests.get(file_email, allow_redirects = True)

# 4.4 --- преобразуем объект запроса в формат json (список компаний)
text_list = response.json()

print(text_list)



# In[ ]:




