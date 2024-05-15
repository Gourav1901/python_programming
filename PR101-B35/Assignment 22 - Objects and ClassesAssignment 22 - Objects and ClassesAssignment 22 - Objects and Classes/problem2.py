import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def distance(self, x=None, y=None, point=None):
        if point is not None:
            
            return math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)
        elif x is not None and y is not None:
            
            return math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2)
        else:
            
            return math.sqrt(self.x ** 2 + self.y ** 2)


first = Point(6, 5)
second = Point(3, 1)
print("distance(0,0)= ", first.distance())
print("distance(second)= ", first.distance(point=second))
print("distance(2,2)= ", first.distance(2, 2))
point = Point()
print("distance()= ", point.distance())
