class User:
    def __init__(self, full_name=''):
        self.full_name = full_name

    def get_name(self):
        return self.full_name

class Guests(User):
    def __init__(self, full_name='', sity='', status=''):
        super().__init__(full_name)
        self.sity = sity
        self.status = status

    def get_sity(self):
        return self.sity

    def get_status(self):
        return self.status

users = [{
    'full_name': 'Иван Петров',
    'sity': 'Москва',
    'status': 'Наставник'},
    {'full_name': 'Вася Пупкин',
     'sity': 'Минск',
     'status': 'Ученик'}]

for i in users:
    unit = Guests(full_name=i.get('full_name'),
                  sity=i.get('sity'),
                  status=i.get('status'))
    print(f'{unit.full_name}, г.{unit.sity}, статус "{unit.status}"')