class Purse:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

users = [{
    "name": "Вася Пупкин",
    "balance": "100"},
    {
    "name": "Иван Петров",
    "balance": "50"
    }]

for i in users:
    unit = Purse(name=i.get("name"),
                 balance=i.get("balance"))
    print(f'Клиент:"{unit.name}" Баланс- {unit.balance}')