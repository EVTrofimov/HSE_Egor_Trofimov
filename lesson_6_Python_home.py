#!/usr/bin/env python
# coding: utf-8

# # домашнее задание 11
# 
# Напишите класс LegalAPI для взаимодействия с API, размещённым по адресу
# https://legal-api.sirotinsky.com/.
# 
# Класс должен содержать в себе функционал для работы со всеми методами,
# указанными в документации к API, которые размещены по адресу
# https://legal-api.sirotinsky.com/docs
# 
# Метод инициализации экземпляра класса должен принимать в качестве аргумента токен для авторизации.
# 
# Методы для получения данных из ЕФРСБ должны быть публичными и содержать
# doc string
# 
# Данные для доступа:
# Token: 4123saedfasedfsadf4324234f223ddf23

# In[1]:


# 0 --- импортируем библиотеки

import requests


# In[2]:


# 1 --- создаем класс

class LegalAPI:
    """
    Класс для взаимодействия с API, размещённым по адресу https://legal-api.sirotinsky.com/
    """
    
    def __init__ (self, token):
        """
        Метод инициализации объекта по токену.
        """
        self.token = token

    def efrsb_publisher_messages (self, inn):
        """
        Метод возвращает объявления заданного публикатора.
        """
        return requests.get(f'https://legal-api.sirotinsky.com/{self.token}/efrsb/publisher_messages/{inn}').json()

    def efrsb_debtor_messages (self, inn):
        """
        Метод возвращает объявления по заданному должнику.
        """
        return requests.get(f'https://legal-api.sirotinsky.com/{self.token}/efrsb/debtor_messages/{inn}').json()

    def efrsb_manager_all (self):
        """
        Метод возвращает данные всех арбитражных управляющих.
        """
        return requests.get(f'https://legal-api.sirotinsky.com/{self.token}/efrsb/manager/all').json()

    def efrsb_manager (self, inn):
        """
        Метод возвращает данные заданного арбитражного управляющего.
        """
        return requests.get(f'https://legal-api.sirotinsky.com/{self.token}/efrsb/manager/{inn}').json()

    def efrsb_trader_all (self):
        """
        Метод возвращает данные всех организаторов торгов.
        """
        return requests.get(f'https://legal-api.sirotinsky.com/{self.token}/efrsb/trader/all').json()

    def efrsb_trader (self, inn):
        """
        Метод возвращает данные заданного организатора торгов.
        """
        return requests.get(f'https://legal-api.sirotinsky.com/{self.token}/efrsb/trader/{inn}').json()

    def efrsb_person (self, inn):
        """
        Метод возвращает данные заданного физического лица - банкрота.
        """
        return requests.get(f'https://legal-api.sirotinsky.com/{self.token}/efrsb/person/{inn}').json()

    def efrsb_organisation (self, inn):
        """
        Метод возвращает данные заданного юридического лица - банкрота.
        """
        return requests.get(f'https://legal-api.sirotinsky.com/{self.token}/efrsb/organisation/{inn}').json()


# In[3]:


# 2 --- создаем экземпляр

a = LegalAPI(token = '4123saedfasedfsadf4324234f223ddf23')
get_ipython().run_line_magic('pinfo', 'a')


# In[4]:


get_ipython().run_line_magic('pinfo', 'a.efrsb_publisher_messages')
print('\nefrsb_publisher_messages\n\n', a.efrsb_publisher_messages(inn = '780533976702'))


# In[5]:


get_ipython().run_line_magic('pinfo', 'a.efrsb_debtor_messages')
print('\nefrsb_debtor_messages\n\n', a.efrsb_debtor_messages(inn = '7810368236'))


# In[6]:


get_ipython().run_line_magic('pinfo', 'a.efrsb_manager_all')
print('\nefrsb_manager_all\n\n', a.efrsb_manager_all())


# In[7]:


get_ipython().run_line_magic('pinfo', 'a.efrsb_manager')
print('\nefrsb_manager\n\n', a.efrsb_manager(inn = '191001529230'))


# In[8]:


get_ipython().run_line_magic('pinfo', 'a.efrsb_trader_all')
print('\nefrsb_trader_all\n\n', a.efrsb_trader_all())


# In[9]:


get_ipython().run_line_magic('pinfo', 'a.efrsb_trader')
print('\nefrsb_trader\n\n', a.efrsb_trader(inn = '2312171566'))


# In[10]:


get_ipython().run_line_magic('pinfo', 'a.efrsb_person')
print('\nefrsb_person\n\n', a.efrsb_person(inn = '667801453240'))


# In[11]:


get_ipython().run_line_magic('pinfo', 'a.efrsb_organisation')
print('\nefrsb_organisation\n\n', a.efrsb_organisation(inn = '7206038280'))


# In[ ]:




