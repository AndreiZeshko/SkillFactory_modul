def hello():
    print("Привет")
    print("Сыграем в Х,О")
    print("тип ввода кординаты x y")
    print(" x - строка")
    print(" y - столбик")

def show():
    print(f"  | 0 | 1 | 2 |")
    print("---------------")
    for i in range(3):
        print(f"{i} | {field[i][0]} | {field[i][1]} | {field[i][2]} |")
        print("---------------")

def ask():
    while True:
        x, y = map(int, input("ход:").split())
        if x < 0 or x > 2 or y < 0 or y > 2:
            print(" Координаты вне диапазона! ")
            continue
        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y

def win():
    win = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0")
            return True
    return False
hello()
field = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win():
        break

    if count == 9:
        print(" Ничья!")
        break


