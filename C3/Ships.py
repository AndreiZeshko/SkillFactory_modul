from random import randint
a=[]
lastNiceShot=[]
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"

class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return "Мимо поля!"

class BoardUsedException(BoardException):
    def __str__(self):
        return "Уже стреляли сюда!"

class BoardWrongShipException(BoardException):
    pass

class Ship:
    def __init__(self, bow, l, o):
        self.bow = bow
        self.l = l
        self.o = o
        self.lives = l

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0:
                cur_x += i

            elif self.o == 1:
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots

    def shooten(self, shot):
        return  shot in self.dots

class Board:
    def __init__(self, hid=False, size=6):
        self.size = size
        self.hid = hid

        self.count = 0

        self.field = [["0"] * size for _ in range(size)]

        self.busy = []
        self.ships = []

    def __str__(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) +" |"

        if self.hid:
            res = res.replace("#", "0")
        return  res

    def out(self, d):
        return  not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def contour(self, ship, verb = False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)
                if not(self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = "."
                    self.busy.append(cur)

    def add_ship(self, ship):
        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in ship.dots:
            self.field[d.x][d.y] = "#"
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)

    def shot(self, d):
        if self.out(d):
            raise BoardOutException()

        if d in self.busy:
            raise BoardUsedException()

        self.busy.append(d)
        global q, w, suka
        w=False
        for ship in self.ships:
            if ship.shooten(d):
                ship.lives -= 1
                self.field[d.x][d.y] = "X"         
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("Уничтожен!")
                    w=True
                    q=False
                    suka=False
                    return q
                else:
                    print("Ранен!")
                    w=False
                    q=True
                    suka=True
                    return q
        
        self.field[d.x][d.y] ="."
        print("Мимо!")
        suka=True
        q=False
        return q

    def begin(self):
        self.busy = []

class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)

class AI(Player):
    def ask(self):
        global d, lastShot, lastNiceShot
        if q==True:
            mab=[
            (d.x-1, d.y), (d.x, d.y+1), (d.x, d.y-1),
            (d.x+1, d.y)]
            l=mab[randint(0,3)]
            d = Dot(l[0],l[1])
        elif len(lastNiceShot)!=0 and w!=True and suka==True:
            mab=[
            (shot.x-1, shot.y), (shot.x, shot.y+1), (shot.x, shot.y-1),
            (shot.x+1, shot.y)]
            l=mab[randint(0,3)]
            d = Dot(l[0],l[1])
        else:   
            d = Dot(randint(0, 5), randint(0, 5))
            print(f"Ход компьютера: {d.x+1} {d.y+1}")
        return d

class User(Player):
    def ask(self):
        while True:
            cords = input("Ваш ход").split()

            if len(cords) != 2:
                print("Введите две кординаты!")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print("Ввведите числа!")
                continue

            x, y = int(x), int(y)

            return  Dot(x - 1, y - 1)

class Game:
    def __init__(self, size=6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hid = True

        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def try_board(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)),
                            l, randint(0 ,1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass

        board.begin()
        return  board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def great(self):
        print("Привет")
        print("Это игра морсокй бой")
        print("формат ввода: x, y")
        print("x - строка, у - столбец")

    def loop(self):
        num=0
        while True:
            print("-"*20)
            print("Пользователь:")
            print(self.us.board)
            print("-"*20)
            print("Компьютер")
            print(self.ai.board)
            print("-"*20)
            if num % 2 == 0:
                print("Ход пользователя")
                repeat = self.us.move()
            else:
                print("Ход компьютера")
                repeat = self.ai.move()
                if q==True:
                    lastNiceShot.append(d)

            if repeat:
                num -= 1

            if self.ai.board.count == len(self.ai.board.ships):
                print("-"*20)
                print(" Пользователь выйграл")
                break

            if self.us.board.count == len(self.us.board.ships):
                print("-"*20)
                print("Компьютер выйграл")
                break
            num += 1


    def start(self):
        self.great()
        self.loop()

g = Game()
g.start()


