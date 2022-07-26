import math
from colors import bcolors


# 1.
class frange:
    def __init__(self, *args, start=0, step=1):
        if len(args) == 1:
            self.start = start
            self.stop = args[0]
            self.step = step
        elif len(args) == 2:
            self.start, self.stop = args
            self.step = step
        elif len(args) == 3:
            self.start, self.stop, self.step = args
        else:
            raise TypeError("3 arguments were expected.")

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.start + self.step >= self.stop + self.step:
                raise StopIteration
            result = self.start
            self.start = self.start + self.step
        else:
            if self.start + self.step <= self.stop + self.step:
                raise StopIteration
            result = self.start
            self.start = self.start + self.step
        return result


assert (list(frange(5)) == [0, 1, 2, 3, 4])
assert (list(frange(2, 5)) == [2, 3, 4])
assert (list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert (list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert (list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert (list(frange(1, 5)) == [1, 2, 3, 4])
assert (list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert (list(frange(0, 0)) == [])
assert (list(frange(100, 0)) == [])

print('SUCCESS!')


# 2.
class colorizer:
    def __init__(self, color):
        self.colors = {
            'red': bcolors.FAIL,
            'green': bcolors.OKGREEN,
            'blue': bcolors.OKBLUE,
            'yellow': bcolors.WARNING,
            'header': bcolors.HEADER,
            'bold': bcolors.BOLD,
            'underline': bcolors.UNDERLINE,
        }
        self.color = color

    def __enter__(self):
        if self.color in self.colors:
            self.color = self.colors[self.color]
            print(self.color, end='')

    def __exit__(self, color=None, value=None, traceback=None):
        print(bcolors.ENDC, end='')


with colorizer('yellow'):
    print('Hello world!')
print('Hello world!')


# 3.
class Shape:  # class Shape(object)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return 0


class Circle(Shape):

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2

    def __contains__(self, instance):
        return (instance.x - self.x) ** 2 + (instance.y - self.y) ** 2 <= self.radius ** 2


class Rectangle(Shape):

    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        return self.width * self.height


class Parallelogram(Rectangle):

    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width)
        self.angle = angle

    def print_angle(self):
        print(self.angle)

    def __str__(self):
        result = super().__str__()
        return result + f'\nParallelogram: {self.width}, {self.height}, {self.angle}'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def square(self):
        return print(self.width * self.height * math.sin(math.radians(self.angle)))


class Triangle(Parallelogram):

    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width, angle)

    def square(self):
        return print(self.width * self.height * math.sin(math.radians(self.angle)) / 2)


class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures)

    def __str__(self):
        pass


class Point(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)


point = Point(1, 2)
point1 = Point(10, 5)

c = Circle(20, 5, 8)
c1 = Circle(50, 60, 10)

p = Parallelogram(1, 2, 20, 30, 45)
p.square()
p1 = Parallelogram(1, 2, 24, 12, 90)
p1.square()

t = Triangle(1, 2, 20, 30, 45)
t.square()
t1 = Triangle(1, 2, 24, 12, 90)
t1.square()

# 4.
print(point in c)
print(point1 in c1)
