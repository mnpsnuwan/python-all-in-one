# Lambda Functions = Function written in 1 line using lambda keyword
# accepts any number of arguments, but only has one expression (Think of it as a shortcut)
# (Useful if needed for a short period of time, throw-away)
#
# lambda parameters : expression


# Without lambda
def double(x):
    return x * 2


print(double(5))

# Using lambda
multiple = lambda x: x * 2
print(multiple(8))

# ---
multiply = lambda x, y: x * y
print(multiply(13, 5))

# ---
full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("Nuwan", "Samarasinghe"))

# ---
age_check = lambda age: True if age >= 18 else False
print(age_check(21))
