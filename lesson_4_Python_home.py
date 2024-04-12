# домашнее задание 7


# 1 --- создаем класс CourtCase

class CourtCase:
    
    # метод конструктора экземпляра
    
    def __init__(self,
                 case_number,
                 case_participants = [],
                 listening_datetimes = [],
                 is_finished = False,
                 verdict = ''):
        self.case_number = case_number
        self.case_participants = case_participants
        self.listening_datetimes = listening_datetimes
        self.is_finished = is_finished
        self.verdict = verdict
        
    # метод добавляет в список listening_datetimes судебное заседание
    
    def set_a_listening_datetime (self, listening_date, listening_place, listening_issue):
        self.listening_datetimes.append([listening_date, listening_place, listening_issue])
    
    # метод добавляет участника (ИНН) в список case_participants
    
    def add_participant (self, inn):
        self.case_participants.append(inn)

    # метод убирает участника (ИНН) из списка case_participants

    def remove_participant (self, inn):
        self.case_participants.remove(inn)
        
    # метод добавляет verdict и меняет атрибут is_finished на True
    
    def make_a_decision (self, verdict):
        self.verdict = verdict
        self.is_finished = True


# 2 --- проверка CourtCase

case = CourtCase(case_number = '2-1223/24',
                 case_participants = ['7700123456', '8800123456'])
print('Object:\n', case, '\n')
print('CourtCase:\n', case.case_number, case.case_participants, case.listening_datetimes, case.is_finished, case.verdict, '\n')

case.set_a_listening_datetime(listening_date = '12.04.2024',
                              listening_place = 'Санкт-Петербург, Исаакиевская пл., 1',
                              listening_issue = 'Подготовка к рассмотрению дела')
print('set_a_listening_datetime:\n', case.case_number, case.case_participants, case.listening_datetimes, case.is_finished, case.verdict, '\n')

case.add_participant(inn = '2200123456')
print('add_participant:\n', case.case_number, case.case_participants, case.listening_datetimes, case.is_finished, case.verdict, '\n')

case.remove_participant(inn = '2200123456')
print('remove_participant:\n', case.case_number, case.case_participants, case.listening_datetimes, case.is_finished, case.verdict, '\n')

case.make_a_decision(verdict = 'В удовлетворении иска отказать')
print('make_a_decision:\n', case.case_number, case.case_participants, case.listening_datetimes, case.is_finished, case.verdict, '\n')
