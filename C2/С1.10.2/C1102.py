class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def get_area(self):
        return self.lenght * self.width

    def __str__(self):
        return f"{self.lenght}, {self.width}"

rect_1 = Rectangle(2, 5)
rect_2 = Rectangle(4, 6)

print(f'Rectangle {rect_1} area={rect_1.get_area()}')