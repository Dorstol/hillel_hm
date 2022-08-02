# 3.Liskov Substitution Principle
# Любой наследуюмый класс должен выполнять операции, которые может выполнить родительский класс.

class Vehicle:
    def __init__(self, name, engine, accelerate):
        self.name = name
        self.engine = engine
        self.accelerate = accelerate

    def start_engine(self):
        self.engine = True

    def start_accelerate(self):
        self.accelerate = True


class Car(Vehicle):
    def __init__(self, name, engine, accelerate):
        super().__init__(name, engine, accelerate)

    def start_engine(self):
        self.engine = True
        self.__engage_ignition()

    def start_accelerate(self):
        self.accelerate = True

    def __engage_ignition(self):
        print("Ignition is engaged")


class ElectricBus(Vehicle):
    def __init__(self, name, engine, accelerate):
        super().__init__(name, engine, accelerate)

    def start_engine(self):
        self.engine.start()

    def start_accelerate(self):
        self.accelerate = True
        self.__increase_voltage()
        self.__connect_engines()

    def __increase_voltage(self):
        print("Success!")

    def __connect_engines(self):
        print("Success!")

if __name__ == '__main__':
    car = Car("BMW", "5", "10")
    car.start_engine()
    bus = ElectricBus("Tesla", "7", "12")
    bus.start_accelerate()

