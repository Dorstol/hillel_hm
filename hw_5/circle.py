class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def contains(self, instance):
        return (instance.x - self.x)**2 + (instance.y - self.y)**2 <= self.radius**2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    circle = Circle(5, 5, 5)
    point = Point(2, 2)
    print(circle.contains(point))