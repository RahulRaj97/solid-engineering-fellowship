"""
Same Car class to look at Open-Closed Principle.
The open-closed principle says software entities should be open for extension,
not modifiation.
"""

from abc import abstractmethod

# We have our Car class again. Let's say we want to add sound to cars.

# Before 
class Car:
    def __init__(self, name):
        self.name = name

    def get_car_name(self):
        return self.name

    def make_sound(self):
        print("****")

class CarDatabase:
    def __init__(self):
        pass

    def save_car(self, car, file_name):
        with open(file_name, 'w') as f:
            f.write(car.name)

    def load_car(self, file_name):
        with open(file_name, 'r') as f:
            return Car(f.read())

# The better way is to create cars to inherit from Car and implement 
# their own make_sound.

# After
class Car:
    def __init__(self, name):
        self.name = name

    def get_car_name(self):
        return self.name
        
    @abstractmethod
    def make_sound(self):
        pass

class CarDatabase:
    def __init__(self):
        pass

    def save_car(self, car, file_name):
        with open(file_name, 'w') as f:
            f.write(car.name)

    def load_car(self, file_name):
        with open(file_name, 'r') as f:
            return Car(f.read())

class BMW(Car):
    def __init__(self, name):
        super(Car, self).__init__(name)

    def make_sound(self):
        pass


class Audi(Car):
    def __init__(self, name):
        super(Car, self).__init__(name)

    def make_sound(self):
        pass


class Ferarri(Car):
    def __init__(self, name):
        super(Car, self).__init__(name)

    def make_sound(self):
        pass

