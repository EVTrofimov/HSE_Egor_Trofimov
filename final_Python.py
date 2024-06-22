#!/usr/bin/env python
# coding: utf-8

# # итоговое задание
# 
# Задание № 2: парсинг
# 
# Необходимо собрать данные с сайта ЦБ РФ с помощью Python.
# 
# В ходе выполнения этого задания вы самостоятельно:
# ● выберите интересующие вас данные на сайте ЦБ РФ,
# ● создадите парсер для их сбора,
# ● подберёте структуру для хранения данных,
# ● создадите модуль для работы с сохранёнными данными.
# 
# Шаг 1
# 
# Выбрать интересующие данные в следующих разделах на сайте ЦБ:
# 
# ● базы данных (https://www.cbr.ru/hd_base/),
# ● реестры (https://www.cbr.ru/registries/),
# ● статистика (https://www.cbr.ru/statistics/).
# 
# Примеры: курс валют, цены на аффинированные драгоценные металлы, реестр
# микрофинансовых организаций и пр.
# 
# ! Для выбора недоступна ключевая ставка, примеры для которой приведены в этом
# задании.
# 
# Шаг 2
# 
# Определите структуру для хранения и работы. Для ключевой ставки ЦБ РФ это может
# быть словарь (dict), где ключом будет выступать дата, а значением — размер
# ключевой ставки на указанную дату:
# 
# {
# 
# …
# 
# datetime.date(2022,4,7): Decimal("0.2000"),
# datetime.date(2022,4,8): Decimal("0.2000"),
# datetime.date(2022,4,11): Decimal("0.1700"),
# datetime.date(2022,4,12): Decimal("0.1700"),
# datetime.date(2022,4,13): Decimal("0.1700"),
# …
# }
# 
# Шаг 3
# 
# Напишите скрипт, который будет производить сбор данных с выбранной страницы на
# сайте ЦБ РФ либо осуществлять загрузку xsl/xslx/pdf/csv или иного файла с данными в
# рабочую директорию с последующим его парсингом.
# 
# Шаг 4
# 
# Сделайте метод сериализации и десериализации данных для сохранения их в JSONфайл и подготовки данных для работы модулем из Шага 7. При написании метода
# используйте dict/list comprehensions.
# 
# Пример сериализованных данных для ключевой ставки:
# 
# {
# 
# …
# 
# '2022-04-07': '0.2000',
# '2022-04-08': '0.2000',
# '2022-04-11': '0.1700',
# '2022-04-12': '0.1700',
# '2022-04-13': '0.1700'
# …
# }
# 
# ! Формат JSON не позволяет хранить данные в виде объектов datetime и decimal.
# 
# Сохранение файла должно производиться в директорию parsed_data внутри папки
# проекта. Путь к директории parsed_data должен быть прописан так, чтобы он был
# кроссплатформенным. Написанный скрипт должен запуститься на любой
# операционной системе и при запуске скрипта из любой директории.
# 
# Шаг 5
# 
# Необходимо привести данные к рабочим типам. Например:
# 1. Даты привести к строковому формату ISO8601 или к типу datetime.
# 2. Числа с плавающей точкой привести к типу decimal или хранить в строковом
# виде.
# 3. И т. д.
# 
# Продумайте и реализуйте методологию заполнения пробелов в данных, если это
# необходимо для работы. Пример для ключевой ставки, которая не публикуется для
# нерабочих дней, однако используется в расчётах:
# 
# {
# 
# …
# 
# '2022-04-07': '0.2000',
# '2022-04-08': '0.2000',
# '2022-04-09': '0.2000',
# '2022-04-10': '0.2000',
# '2022-04-11': '0.1700',
# '2022-04-12': '0.1700',
# '2022-04-13': '0.1700'
# …
# }
# 
# Шаг 6
# 
# Оберните весь написанный код парсера в класс ParserCBRF.
# 
# Запуск парсера должен осуществляться через вызов метода start().
# 
# Шаг 7
# 
# Создайте отдельный класс для работы с собранными данными.
# 
# Для работы с ключевой ставкой можно описать класс KeyRateCBRF, экземпляр
# которого при работе будет обращаться к файлу с сохранёнными данными и через свои
# методы позволит быстро и удобно получать необходимые данные.
# 
# В рассматриваемом случае класс KeyRateCBRF может содержащий следующие
# публичные методы:
# 
# ● 
# keyrate_by_date(date) — возвращает размер ставки на определённую дату
# 
# Input:
# KeyRateCBRF.keyrate_by_date(“2022-04-07”)
# Output:
# "0.2000"
# 
# ● 
# keyrate_last() — возвращает размер ключевой ставки на последнюю доступную
# дату
# 
# Input:
# KeyRateCBRF.keyrate_last()
# Output:
# "0.7500"
# 
# ● keyrate_range_dates(from_date, to_date) — возвращает отсортированный
# список кортеж пар (дата, ключевая ставка) за определённый период
# 
# Input:
# KeyRateCBRF.keyrate_range_dates('2022-04-07', '2022-04-13')
# Output:
# [
# ('2022-04-07', '0.2000'),
# ('2022-04-08', '0.2000'),
# ('2022-04-09', '0.2000'),
# ('2022-04-10', '0.2000'),
# ('2022-04-11', '0.1700'),
# ('2022-04-12', '0.1700'),
# ('2022-04-13', '0.1700')
# ]
# 
# Методы, указанные выше, являются примером для ключевой ставки. Список методов
# класса для работы с данными должен быть составлен в зависимости от вида данных,
# которые вы выбрали.
# 
# 
# Оценка задания №2 производится преподавателем на основе
# следующих критериев:
# ● парсер успешно запустился через вызов Parser.start()
# и сохранил данные в JSON — 6 баллов;
# ● успешно реализован класс и методы для работы с
# загруженными данными — 2 балла;
# ● весь код оформлен в соответствии с общепринятыми
# правилами (PEP8), в классах реализованы методы
# сериализации и десериализации — 2 балла.
# 
# Максимально можно получить 10 баллов

# In[1]:


import sys
import os
import json
import requests
from datetime import datetime
from datetime import timedelta
from decimal import Decimal
import calendar
from bs4 import BeautifulSoup


# In[2]:


class InflationRateCBRF:
    
    """
    Класс для сбора с сайта ЦБ РФ данных об инфляции за период.
    Для корректной работы импортируйте библиотеки
    BeautifulSoup, datetime, calendar, Decimal, json, requests, sys.
    """

    
    def _collect(self):

        """
        Метод возвращает объект BeautifulSoup со спарсенной
        страницей html в пределах доступных данных об инфляции.
        """
        now_ = str(datetime.now().strftime('%d.%m.%Y'))
        url = f'https://www.cbr.ru/statistics/ddkp/infl/?UniDbQuery.Posted=True&'\
        f'UniDbQuery.From=17.09.2013&UniDbQuery.To={now_}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
        

    def _filter(self, soup):
        """
        Метод фильтрует данные объекта BeautifulSoup,
        сериализует даты по ISO (год-месяц) и возвращает
        словарь из месяцев и значений инфляции.
        """
        self.soup = soup
        rate_dict = {}
        try:
            rate = soup.find('table', 'data').find_all('tr')[1:]
        except AttributeError:
            print('Data not found. Change parameter(s).')
            sys.exit()
        for i in rate:
            month_ = i.find_all('td')[0].text
            key = datetime.strptime(month_, '%m.%Y').date().isoformat()[:7]
            value = i.find_all('td')[2].text.replace(',', '.')
            rate_dict[key] = value
        print(rate_dict)
        return rate_dict

    
    def _save(self, rate_dict):
        """
        Метод сохраняет в файл json словарь из месяцев и значений инфляции.
        """
        self.rate_dict = rate_dict
        now_ = str(datetime.now())
        file_ = f'InflationRateCBRF_{now_[:10]}.json'
        dir_ = 'parsed_data'
        path = os.getcwd()
        if not os.path.exists(dir_):
            os.mkdir(dir_)
        name = os.path.join(dir_, file_)
        if not os.path.exists(name):
            with open(name, 'w') as json_file:
                json.dump(rate_dict, json_file, indent = 4)
        return name
    
    
    def _load(self, name):
        """
        Метод загружает словарь из месяцев и значений инфляции из файла json.
        """
        self.name = name
        with open(name, 'r') as json_file:
            rate_dict = json.load(json_file)
        return rate_dict

    
    def _deserial(self, rate_dict):
        """
        Метод десериализует значения словаря из файла json
        (месяцы - в класс datetime.date, значения инфляции в  класс Decimal).
        """
        self.rate_dict = rate_dict
        deserial_dict = {}
        for key in rate_dict:
            date_ = datetime.strptime(key, '%Y-%m').date()
            days_ = calendar.monthrange(date_.year, date_.month)[1]
            date_ += timedelta(days=(days_-1))
            deserial_dict[date_] = Decimal(rate_dict[key])
        return deserial_dict


    def _check(self):
        now_ = str(datetime.now())
        file_ = f'InflationRateCBRF_{now_[:10]}.json'
        dir_ = 'parsed_data'
        path = os.getcwd()
        if not os.path.exists(dir_):
            os.mkdir(dir_)
        name = os.path.join(dir_, file_)
        if not os.path.exists(name):
            soup = self._collect()
            rate_dict = self._filter(soup=soup)
            name = self._save(rate_dict=rate_dict)
        rate_dict = self._load(name=name)
        return self._deserial(rate_dict=rate_dict)

        
    def start(self):
        """
        Метод сохраняет в файл json значения инфляции по месяцам за доступный период.
        """
        soup = self._collect()
        rate_dict = self._filter(soup=soup)
        name = self._save(rate_dict=rate_dict)
        rate_dict = self._load(name=name)
        rate_dict = self._deserial(rate_dict=rate_dict)
        print(f'Значения инфляции за доступный период\n', rate_dict, '\nКонец')
        
        
    def last(self):
        """
        Метод выводит последнее доступное значение инфляции.
        """
        rate_dict = self._check()
        date_ = datetime.now().date()
        days_ = calendar.monthrange(date_.year, date_.month)[1]
        if date_.day < days_:
            days_ = calendar.monthrange(date_.year, date_.month)[1]
            date_ -= timedelta(days=date_.day)
        month_ = date_.strftime('%B')
        year_ = date_.strftime('%Y')
        print(f'The inflation rate in {month_} {year_} was {rate_dict[date_]}.')

        
    def month(self, month):
        """
        Метод выводит значение инфляции за заданный месяц.
        """
        self.month = month
        rate_dict = self._check()
        try:
            date_ = datetime.strptime(month, '%Y-%m').date()
            days_ = calendar.monthrange(date_.year, date_.month)[1]
            date_ += timedelta(days=(days_-1))
            month_ = date_.strftime('%B')
            year_ = date_.strftime('%Y')
            print(f'The inflation rate in {month_} {year_} was {rate_dict[date_]}.')
        except:
            print('Data not found. Change month.')

        
    def period(self, firstmonth, lastmonth):
        """
        Метод выводит значения инфляции за заданный период.
        """
        self.firstmonth = firstmonth
        self.lastmonth = lastmonth
        rate_dict = self._check()
        print(f'Значения инфляции за заданный период')
        try:
            date_ = datetime.strptime(lastmonth, '%m.%Y').date()
            days_ = calendar.monthrange(date_.year, date_.month)[1]
            lastdate = date_ + timedelta(days=(days_-1))
            date_ = datetime.strptime(firstmonth, '%m.%Y').date()
            days_ = calendar.monthrange(date_.year, date_.month)[1]
            date_ += timedelta(days=(days_-1))
            while date_ <= lastdate:
                month_ = date_.strftime('%B')
                year_ = date_.strftime('%Y')
                print(f'The inflation rate in {month_} {year_} was {rate_dict[date_]}.')
                if date_.month == 12:
                    days_ = 31
                else:
                    days_ = calendar.monthrange(date_.year, date_.month+1)[1]
                date_ += timedelta(days=days_)
            print('Конец')
        except:
            print('Data not found. Change month(s).')


# In[3]:


# проверка

def main():
    attempt = InflationRateCBRF()
    print(f'\nMETHOD === start\n')
    attempt.start()
    print(f'\nMETHOD === last\n')
    attempt.last()
    print(f'\nMETHOD === month\n')
    attempt.month(month='04.2024')
    print(f'\nMETHOD === period\n')
    attempt.period(firstmonth='06.2023', lastmonth='05.2024')

if __name__ == '__main__':
    main()


# In[ ]:




