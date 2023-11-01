# Function = A block of code which is executed only when it is called.
# Python program to illustrate
# functions
def hello():
    print("hello")
    print("hello again")


# calling function
hello()


# --------------------------------------
# Python program to illustrate
# function with main
def get_integer():
    result = int(input("Enter integer: "))
    return result


def main():
    print("Started")

    # calling the getInteger function and
    # storing its returned value in the output variable
    output = get_integer()
    print(output)


# now we are required to tell Python
# for 'Main' function existence
if __name__ == "__main__":
    main()


# -------------------------------------
# Defining and calling a function with parameters
def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2

    return num3


# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")


# --------------------------------------
# Arbitrary Keyword Arguments, *args, and **kwargs can pass a variable number of arguments
# to a function using special symbols.
# There are two special symbols:
# *args in Python (Non-Keyword Arguments)
# **kwargs in Python (Keyword Arguments)
# Python program to illustrate
# *args variable length non-keywords argument passing as tuple
def my_argv_fun(*argv):
    for arg in argv:
        print(arg)


my_argv_fun('Hello', 'Welcome', 'to', 'IMatrixLabs')


# ---
def add(*stuff):
    total = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        total += i
    return total


print(add(1, 2, 3, 4, 5, 6))


# Python program to illustrate
# *kwargs = Parameter that will pack all arguments into a dictionary
# For variable number of keyword arguments
def my_kwargs_fun(**kwargs):
    print("Hello " + kwargs["first"] + " " + kwargs["mid"])
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
my_kwargs_fun(first='I', mid='Matrix', last='Labs')


# -----------------------------------------
# Adding Docstring to the function

# A simple Python function to check
# whether x is even or odd
def even_odd(x):
    """Function to check if the number is even or odd"""

    if x % 2 == 0:
        print("even")
    else:
        print("odd")


# Driver code to call the function
print(even_odd.__doc__)


# ----------------------------------------
# Python Function within Functions
# Python program to
# demonstrate accessing of
# variables of nested functions

def f1():
    s = 'I love IMatrixLabs'

    def f2():
        print(s)

    f2()


# Driver's code
f1()


# ----------------------------------------
# Anonymous Functions in Python
# Python code to illustrate the cube of a number
# using lambda function
def cube(x): return x * x * x


cubeV2 = lambda x: x * x * x

print(cube(7))
print(cubeV2(7))


# ----------------------------------------
# Pass by Reference and Pass by Value
# Here x is a new reference to same list lst
def my_fun(x):
    x[0] = 20


# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
my_fun(lst)
print(lst)


# -----------------------------------------
# Passing a reference and change the received reference to something else
def my_fun2(x):
    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x = [20, 30, 40]


# Driver Code (Note that lst is not modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
my_fun2(lst)
print(lst)


# ---------------------------------------------

def my_fun3(x):
    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x = 20


# Driver Code (Note that x is not modified
# after function call.
x = 10
my_fun3(x)
print(x)


# ---
def hello(name, age):
    print("Hello, " + name)
    print("Perhaps you are " + str(age) + " years old")
    print("Have a nice day!")


first_name = "Nuwan"
hello(first_name, 25)

# ------------------------------------
# Nested function call = Function calls inside other function call
# Innermost function calls are resolved first
# Returned value is used as argument for the next outer function

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# Above list in one line
print(round(abs(float(input("Enter a whole positive number: ")))))

# ===============================
# Python rule >>>
# L => Local
# E => Enclosing
# G => Global
# B => Built-In

