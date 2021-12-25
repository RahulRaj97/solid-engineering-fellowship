""" 
Car class to demonstrate Single Responsibility Principle.
The single responsibility principle says that a class should be responsible for just one thing.
"""

# Before
class Car:
    def __init__(self, name):
        self.name = name

    def get_car_name(self):
        return self.name

    def save_car(self, file_name):
        with open(file_name, 'w') as f:
            f.write(self.name)

    def load_car(self, file_name):
        with open(file_name, 'r') as f:
            self.name = f.read()

# After
class Car:
    def __init__(self, name):
        self.name = name

    def get_car_name(self):
        return self.name

class CarDatabase:
    def __init__(self):
        pass

    def save_car(self, car, file_name):
        with open(file_name, 'w') as f:
            f.write(car.name)

    def load_car(self, file_name):
        with open(file_name, 'r') as f:
            return Car(f.read())
