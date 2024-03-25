# домашнее задание 5
"""
1. Найдите информацию об организациях.
a. Получите список ИНН из файла traders.txt.
b. Найдите информацию об организациях с этими ИНН в файле ntraders.json.
c. Сохраните информацию об ИНН, ОГРН и адресе организаций из файла traders.txt в файл traders.csv.
"""

# 0 --- импортируем модули

import requests, re, csv

# 1 --- получаем список ИНН из файла traders.txt

# 1.1 --- определяем файл входящих данных с GitHub
file_inn = 'https://raw.githubusercontent.com/sirotinsky/HSE_LegalPy/main/homeworks/lesson3/traders.txt'

# 1.2 --- создаем запрос
response = requests.get(file_inn)

# 1.3 --- удаляем лишние символы с помощью регулярных выражений, преобразуем в список
inn_list = str(re.sub('[^0-9]', ' ', str(response.content))).split()

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

# 3 --- сохраняем информацию об ИНН, ОГРН и адресе организаций из файла traders.txt в файл traders.csv\n",

with open(file_traders, 'w', newline = '') as file:
    writer = csv.writer(file, dialect = 'excel', delimiter=';')
    writer.writerows(list_traders)

# 4 --- напишите регулярное выражение для поиска email-адресов в тексте

# 4.1 --- определяем файл входящих данных с GitHub
file_email = 'https://raw.githubusercontent.com/sirotinsky/HSE_LegalPy/main/homeworks/lesson3/1000_efrsb_messages.json'

# 4.2 --- определяем файл исходящих данных (загружаем на свой комп в текущую папку)
file_dict = 'emails.json'

# 4.3 --- читаем файл входящих данных в датафрейм
# response = requests.get(file_email, allow_redirects = True)
df = pandas.read_json(file_email)
display(df)

# 4.4 --- выгружаем датафрейм в файл excel на комп в текущую папку
df.to_excel('1000_efrsb_messages.xlsx')

# 4.5 --- создаем функцию для идентификации email
def find_email (msg_text):
    
    # создаем пустой список email (для текущего ИНН публикатора)
    list_email = []
    
    # удаляем лишние символы с помощью регулярных выражений, преобразуем в список слов
    msg_text = re.sub('(\.* )|(\,* )|(\:* )|(\;* )|(\!* )|(\?* )|(\&* )|(\#* )|(\"* )|(\'* )|(\)* )', ' ', msg_text)
    msg_text = msg_text.split(sep = None)
    
    for text in msg_text:
        
        # проверяем на основной паттерн
        if re.match(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', text) == None:
            continue

        # проверяем на двойные точки
        if re.findall(r'\.{2}', text) == ['..']:
            continue

        # разбиваем адрес на две части
        user = text[:text.find('@')]
        domen = text[text.find('@') + 1:]

        # проверяем user и domen на длину (1-128)
        if len(user) == 0 or len(user) > 128 or len(domen) == 0 or len(domen) > 256:
            continue

        # проверяем местоположение точек и дефисов
        if re.match(r'\.', user) != None or re.findall(r'\.@', text) or re.findall(r'-\.', domen) == ['-.']:
            continue
        else:
            email = True
        
        if email == True:
            list_email.append(text)
        
    return (list_email)

# 4.6 --- создаем пустой словарь для записи email
dict_emails = {}

# 4.7 --- загружаем датафрейм из файла
df = pandas.read_excel('1000_efrsb_messages.xlsx')

# 4.8 --- проходим циклом по строкам датафрейма
for row in range (0, len(df), 1):
    
    # присваиваем текущее значение ИНН публикатора
    publisher_inn = df['publisher_inn'][row]
    
    # присваиваем текущее сообщения публикатора
    msg_text = df['msg_text'][row]
    
    # исполняем авторскую функцию для идентификации email в тексте сообщения публикатора
    list_email = find_email (msg_text)

    # дополняем словарь email для текущего ИНН публикатора, если авторская функция вернула непустой список email
    if list_email != []:
        dict_emails[str(publisher_inn)] = list_email
    
# 4.9 --- сохраняем список email (в разрезе ИНН публикаторов) в исходящий файл json
with open(file_dict, "w", encoding = "utf-8") as file:
    json.dump(dict_emails, file)

# 4.10 --- примечание
print('В задании 5 (пункт 2) указано сделать словарь с множеством адресов (set), но структура set неитерабельна и не выгружается в json.')
