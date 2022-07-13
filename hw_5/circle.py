class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def contains(self, instance):
        if instance.x ** 2 + instance.y ** 2 <= self.radius ** 2:
            return True
        else:
            return False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


circle = Circle(10, 11, 5)
point = Point(2, 2)
print(circle.contains(point))
