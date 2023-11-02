# Abstract class = A class which contains one or more abstract methods.
# Abstract method = A method that has a declaration but does not have an implementation.
# Prevents a user from creating an object of that class.
# Compels a user to override abstract methods in a child class.

# abc >>> acronym for abstract
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stopped the car")


class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stopped the motorcycle")


# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()
