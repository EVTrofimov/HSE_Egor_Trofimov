# итоговое задание === Задание № 2: парсинг


import sys
import os
import json
import requests
from datetime import datetime
from datetime import timedelta
from decimal import Decimal
import calendar
from bs4 import BeautifulSoup


class InflationRateCBRF:
    """
    Класс для сбора с сайта ЦБ РФ данных об инфляции за период.
    Для корректной работы импортируйте библиотеки
    bs4, datetime, calendar, decimal, json, requests, sys, os.
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
