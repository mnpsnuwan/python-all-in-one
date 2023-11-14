# 01
def multiple(num1, num2):
    for i in range(num2, num1, -1):
        if i % 10 != 0 and i % 5 == 0:
            print(i)


multiple(1, 100)


# 02
def factorial(n):
    fac = 1
    if n == 0:
        return 1
    else:
        for i in range(n, 1, -1):
            fac = fac*i
        return fac


print(factorial(4))


# 03
def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        # temp = a
        # a = b
        # b = temp + b

        a, b = b, a + b  # above swap in one line
        print(a, end=" ")


fibonacci(6)











