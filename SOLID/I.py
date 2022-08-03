# 4.Interface segregation principle
# Separate the interface from the implementation
from abc import ABC, abstractmethod


class Teacher(ABC):
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @abstractmethod
    def teach(self):
        pass


class Rector(ABC, Teacher):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
        self.salary = salary * 2

    @abstractmethod
    def take_exams(self):
        pass


class Professor(ABC, Teacher):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
        self.salary = salary * 3

    @abstractmethod
    def pay_salary(self):
        pass