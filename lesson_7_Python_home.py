#!/usr/bin/env python
# coding: utf-8

# # домашнее задание 13
# 
# Задание 1 (парсинг)
# 
# Напишите скрипт, который будет производить сбор данных с выбранной вами
# страницы на сайте ЦБ РФ либо осуществлять загрузку xsl, xslx, pdf, csv или иного
# файла с данными в рабочую директорию с последующим его парсингом.
# 
# У класса должен быть только один публичный метод start(). Все остальные методы,
# содержащие логику по выгрузке и сохранению данных, должны быть приватными.
# 
# Определите структуру для хранения. Для ключевой ставки ЦБ РФ это может быть
# словарь (dict), где ключом будет выступать дата, а значением — размер ключевой
# ставки на указанную дату.
# 
# Оберните весь написанный код парсера в класс ParserCBRF
# 
# Задание преподаватель оценивает на основе следующих критериев:
# ● парсер успешно запустился через вызов Parser.start() и сохранил данные в JSON — 8 баллов;
# ● весь код оформлен в соответствии с общепринятыми правилами (PEP8),
#   в классах реализованы методы сериализации и десериализации — 2 балла.
# Максимально можно получить 10 баллов

# In[ ]:


from bs4 import BeautifulSoup

from datetime import datetime

import json
import requests
import sys


# In[ ]:


class ParserCBRF:
    
    """Класс для сбора с сайта ЦБ РФ данных о ключевой ставке за период."""
    
    
#    def __init__(self):
#        None

        
    def _input_dates (self):
        
        """Метод возвращает даты начала и конца периода сбора данных."""
        
        # задаем формат даты
        format_date = '%d.%m.%Y'
        
        # задаем наиболее раннюю дату для работы с сайтом ЦБ РФ
        early_date = datetime.strptime('17.09.2013', format_date)
        
        # создаем список для начальной и конечной даты
        date_list = [None, None]
        
        # создаем переменные для подсказок пользователю
        date_texts = ['начальную', 'конечную']

        # запускаем цикл для ввода начальной и конечной дат периода
        for i in range (0, 2):

            # зацикливаем алгоритм до получения корректной даты
            while date_list[i] == None:

                date_str = input(f'Введите {date_texts[i]} дату в формате ДД.ММ.ГГГГ'\
                                 ' (не ранее 17.09.2013 и не позднее текущей): ')

                # предусматриваем возможность выхода из цикла
                if date_str == 'exit':
                    sys.exit()
                    
                # проверка корректности формата и диапазона дат
                try:
                    date_input = datetime.strptime(date_str, format_date) 
                    if date_input >= early_date and date_input <= datetime.today():
                        date_list[i] = date_str
                except:
                    None

                # проверка корректности диапазона конечной даты (не ранее начальной)
                try:
                    if i == 1:
                        if datetime.strptime(date_list[0], format_date) > date_input:
                            date_list[i] = None
                except:
                    date_list[i] = None

                # сообщение пользователю о некорректном вводе информации
                if date_list[i] == None:
                    print('ERROR!   ДАТА ВВЕДЕНА НЕВЕРНО!!! '\
                         'Попытайтесь еще или наберите exit для выхода.')

        # метод возвращает список из дат начала и конца периода сбора данных
        return date_list

    
    def _collect_dict (self, date_list):

        """Метод возвращает словарь из дат и значений ключевой ставки."""

        # получаем список из дат начала и конца периода сбора данных
        self.date_list = date_list
        
        # создаем словарь для записи значений ключевой ставки по ключу даты
        rate_dict = {}
        
        # определяем страницу для парсинга с указанием периода запроса данных
        url = f'https://cbr.ru/hd_base/KeyRate/?UniDbQuery.Posted=True&'\
        f'UniDbQuery.From={date_list[0]}&UniDbQuery.To={date_list[1]}'
        
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        try:
            rate = soup.find('table', 'data').find_all('tr')
        except AttributeError:
            print('\nВ заданном Вами периоде данные не найдены.')
            sys.exit()
        
        # итерируем по ячейкам таблицы для извлечения дат и ставок
        for i in rate:
            key = None
            value = None
            for j in i.find_all('td'):
                if key != None:
                    value = float(j.text.replace(',', '.'))
                else:
                    key = j.text
                if value != None:
                    rate_dict[key] = value
                    
        return rate_dict

    
    def _save_dict (self, rate_dict):

        """Метод сохраняет в файл json словарь из дат и ключевой ставки."""
  
        # получаем словарь из ключей-дат и значений ключевой ставки
        rate_dict = rate_dict
        
        # формируем название файла (с указанием даты и времени) для выгрузки
        now_ = str(datetime.now())
        filename = f'{now_[:10]}_{now_[11:13]}-{now_[14:16]}-{now_[17:19]}.json'
        
        # записываем файл json
        with open(filename, 'w') as json_file:
            json.dump(rate_dict, json_file, indent = 4)
        
        print(f'\nСловарь из дат и ключевой ставки сохранен в файл {filename}.')
        
        return filename

    
    def _print_dict (self, filename):

        """Метод выводит на экран словарь и файла json."""
  
        # получаем словарь из ключей-дат и значений ключевой ставки
        filename = filename
        
        # записываем файл json
        with open(filename, 'r') as json_file:
            load_dict = json.load(json_file)
        
        # выводим на экран словарь
        print(f'\nЗначения ключевой ставки по датам - из файла {filename}.\n\n'\
             'Начало\n')

        print(load_dict)
        
        print('\nКонец')

        return None

    
    def start (self):
        """Метод сохраняет файл json ключевую ставку за заданный период."""
        date_list = self._input_dates()
        rate_dict = self._collect_dict(date_list = date_list)
        filename = self._save_dict(rate_dict = rate_dict)
        self._print_dict(filename = filename)
        return None


# In[ ]:


# проверка

def main():
    attempt = ParserCBRF()
    attempt.start()

if __name__ == '__main__':
    main()


# In[ ]:




