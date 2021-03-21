from C181 import Pet_house

cat1 = [{
     "name": "Феликс",
     "age": "2",
     "gender": "Мальчик",
    },{
     "name": "Сэм",
     "age": "2",
     "gender": "Мальчик",
    },]

for pet in cat1:
    unit = Pet_house(name=pet.get("name"),
                     gender=pet.get("gender"),
                     age=pet.get("age"))
    print(unit.name,"(",unit.gender,")","возраст:", unit.age)