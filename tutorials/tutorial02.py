# 01
def calculate_length(string):
    return len(string)


input_string = input("Enter a string?: ")
print("The total number of characters in the string is", calculate_length(input_string))
print()


# 02
def circle_area(radius):
    pi = 3.14
    return pi*radius**2


def ring_area(outer, inner):
    return circle_area(outer) - circle_area(inner)


outer_input = int(input("Enter outer radius?: "))
inner_input = int(input("Enter inner radius?: "))
print("The surface area of the ring is ", round(ring_area(outer_input, inner_input), 2))
print()


# 03
def roots(a, b, c):
    return b**2 - 4*a*c


print("The quadratic formula is ax^2+bx+c=0")
A = int(input("Enter 'a' for quadratic formula?: "))
B = int(input("Enter 'b' for quadratic formula?: "))
C = int(input("Enter 'c' for quadratic formula?: "))

print("b^2-4ac is " + str(roots(A, B, C)))
print()


# 04 F = 9C/5 + 32
def celsius_to_fahrenheit(celsius):
    return celsius*9/5 + 32


celsius_input = float(input("Please input the Celsius temperature value: "))
print("The Fahrenheit value for the given temperature is ", round(celsius_to_fahrenheit(celsius_input), 2))



