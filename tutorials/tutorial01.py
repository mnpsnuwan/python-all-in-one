# 01
print(12 + 4 / 2 * 7 - 11 + 9)

# 02
X = 1.3
N = 5
print(X * N)

# 03
a = 3
b = -2
c = 1
eq = b**2 - 4 * a * c  # Without pow()
equation = pow(b, 2) - 4 * a * c  # With pow()
print(eq, ";", equation)

# 04
years = 3
days = 3 * 365 + 268
hours = days * 24
minutes = hours * 60
print(minutes)

# 05
inch_in_cm = 2.54
height_in_inch = 10 * 12 + 10
height_in_cm = height_in_inch * inch_in_cm
print(height_in_cm, 'cm')

# 06 area = pi*r^2
pi = 3.14
radius = 5.4
area = pi * pow(radius, 2)
print(round(area, 2))

# 07 area = pi*r^2
pi = 3.14
outer_radius = 7
inner_radius = 5
area = pi * (pow(outer_radius, 2) - pow(inner_radius, 2))
print(area)

# 08 volume = pi*r^2*h
pi = 3.14
radius = 3.2
height = 10.1
volume = pi * pow(radius, 2) * height
print(round(volume, 2))

# 09 area = pi*r^2 + 2*pi*r*h
surface_area = pi * pow(radius, 2) + 2 * pi * radius * height
print(round(surface_area, 2))

# 10
customer_pays = 150
theatre_cost = 2000
attendees = 520
show_costs = theatre_cost + 30 * attendees
customer_costs = customer_pays * attendees
profit = customer_costs - show_costs
print(round(profit, 2))





