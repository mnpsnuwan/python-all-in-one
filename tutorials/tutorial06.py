# 01 factorial(n) = n * (n - 1) * ... * 1
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(4))


# 02 fibonacci(n) = num-1 + num-2
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num - 2)


print(fibonacci(4))


# 03
def gcd(a, b):
    if b == 0:
        return a
    elif a > b:
        return gcd(b, (a % b))
    elif a < b:
        return gcd(b, a)


print(gcd(18, 30))


# 04
def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base*power(base, exponent-1)


print(power(3, 4))


# 05
def investment(initial_investment, annual_interest_rate, number_of_years):
    if number_of_years == 0:
        return initial_investment
    else:
        initial_investment = initial_investment + initial_investment * annual_interest_rate/100
        return investment(initial_investment, annual_interest_rate, number_of_years-1)


print(investment(1000, 10, 3))
