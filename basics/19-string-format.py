# str.format() = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"
number = 3.14159
large_number = 20000

# print("The " + animal + " jumped over the " + item)
print("The {} jumped over the {}".format(animal, item))
print("The {0} jumped over the {1}".format(animal, item))  # positional arguments
print("The {b} jumped over the {a}".format(a="moon", b="dog"))  # keyword arguments
print("Today you can see {:10}. It's a poya day".format(item))
print("Today you can see {:<10}. It's a poya day".format(item))  # Left the item
print("Today you can see {:>10}. It's a poya day".format(item))  # Right the item
print("Today you can see {:^10}. It's a poya day".format(item))  # Center the item

print("The number is {:.3f}".format(number))
print("The number is {:.2f}".format(number))
print("The number is {:,}".format(large_number))  # 1000 places
print("The number is {:b}".format(large_number))  # As binary
print("The number is {:o}".format(large_number))  # As octa
print("The number is {:x}".format(large_number))  # As hexa lower case
print("The number is {:X}".format(large_number))  # As hexa upper case
print("The number is {:e}".format(large_number))  # As scientific notation lower case
print("The number is {:E}".format(large_number))  # As scientific notation upper case

