class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y}), id: {id(self)}'


a = Point(1, 2)
print(a)
Point.__init__(a, 4, 5)
print(a)
