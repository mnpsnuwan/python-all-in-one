# Method chaining = Calling multiple methods sequentially
# Each call performs an action on the same objects and returns self

class Car:
    def turn_on(self):
        print("You started the engine!")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn offed the engine!")
        return self


car = Car()
# car.turn_on()
# car.drive()

# Method chaining [Should return the method]
# car.turn_on().drive().brake()
car.turn_on().\
    drive().\
    brake().\
    turn_off()

