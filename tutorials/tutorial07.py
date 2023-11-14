# 01
def add_sum(num1, num2):
    total = 0
    for i in range(num1, num2+1):
        total = total + i

    return total


print(add_sum(3, 5))


# 02
def odd_sum(num1, num2):
    odd_total = 0
    for i in range(num1, num2+1):
        if i % 2 != 0:
            odd_total = odd_total + i

    return odd_total


print(odd_sum(1, 11))


# 03
def cubes(num):
    cube_sum = 0
    for i in range(num+1):
        cube_sum = cube_sum + i**3
    return cube_sum


number = int(input("Enter a number: "))
print("The Answer is", cubes(number))



