# 2.Open/closed principle
# Open for extension, closed for modification
import random


class Student:
    def __init__(self, name, faculty=None):
        self.name = name
        self.age = random.randint(15, 25)
        self.faculty = faculty

    def studying_lessons(self):
        return print(f'{self.name} is studying {self.faculty}')

    def rest_in_free_time(self):
        return print(f'{self.name} is resting right now')


class HistoryStudent(Student):
    def __init__(self, name, faculty=None):
        super().__init__(name, faculty)
        self.faculty = 'History'


class MathStudent(Student):
    def __init__(self, name, faculty=None):
        super().__init__(name, faculty)
        self.faculty = 'Math'


if __name__ == '__main__':
    math_student = MathStudent('Marta')
    math_student.studying_lessons()
    history_student = HistoryStudent('John')
    history_student.studying_lessons()
