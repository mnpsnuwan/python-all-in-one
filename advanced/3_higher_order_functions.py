# Higher Order Functions = A function that either:
# 1. Accepts a function as an argument
# 2. Returns a function (In python, functions are also treated as objects)

# 1.
# ----------------------------------------
def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func):
    text = func("Hello")
    print(text)


hello(loud)
hello(quiet)

# 2.
# ----------------------------------------


def divisor(x):
    def dividend(y):
        return y/x
    return dividend


divide = divisor(2)
subsidy = divide(10)
print(divide(20))
print(subsidy)




