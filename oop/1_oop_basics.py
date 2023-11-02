from car import Car

car_1 = Car()
car_2 = Car()

car_1.make = "BMW"
car_1.model = "X5"
car_1.year = 2023
car_1.color = "BLACK"

car_2.make = "Rolls Royce"
car_2.model = "Cullinan"
car_2.year = 2023
car_2.color = "BLACK"

print(Car.wheels)
print(car_1.wheels)
car_1.drive()
car_2.drive()
car_1.stop()
car_2.stop()

