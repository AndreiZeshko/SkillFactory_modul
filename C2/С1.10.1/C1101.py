class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def __str__(self):
        return f"Rectungle({self.x}, {self.y}, {self.width}, {self.height})"

rect = Rectangle(2, 5, 10, 15)

print(rect)
