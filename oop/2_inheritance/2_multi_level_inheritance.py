# Multi-level inheritance = when a derived (child) class inherits another derived (child) class

class Organism:

    alive = True


class Animal(Organism):

    def eat(self):
        print("This animal is eating")


class Dog(Animal):

    def bark(self):
        print("This animal is barking")


dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()
