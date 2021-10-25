class Point:
    all_instances = []

    def __init__(self, x, y):
        self.x = x
        self.y = y

        '''
        Without the string below (if commented) self.all_instances and Point.all_instances will be the same object
        But with this string self.all_instances and Point.all_instances will be different objects
        '''
        self.all_instances = []

        self.all_instances.append(self)
        Point.all_instances.append(self)


p1 = Point(1,2)
p2 = Point(3,4)

print('p1', p1.all_instances)
print('p2', p2.all_instances)
print('Point', Point.all_instances)
