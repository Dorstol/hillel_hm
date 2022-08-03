# 1. Single responsibility principle
# Один класс должен иметь одну ответственность.
from random import random


class Student:
    def __init__(self, name, email):
        self.name = name
        self.age = random.randint(15, 25)
        self.happiness = 0
        self.skill = 0

    def studying_lessons(self):
        self.skill += 1
        return self.skill

    def rest_in_free_time(self):
        self.happiness += 1
        return self.happiness


class Teacher:
    def __init__(self, name, email):
        self.name = name
        self.age = random.randint(30, 40)
        self.salary = 0
        self.enjoyment = 0

    def teaching_lessons(self):
        self.salary += 100
        return self.salary

    def do_the_lovely_thing(self):
        self.enjoyment += 1
        return self.enjoyment
