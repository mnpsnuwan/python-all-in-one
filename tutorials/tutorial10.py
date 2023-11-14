# Define list
my_list = ["Java", "Python", "C++", "PHP", "programming", 365, "@", "UCSC"]

# 01
print(my_list[0])

# 02
print(my_list[1:])

# 03
print(len(my_list))

# 04
print(my_list[4])

# 06
my_list.append("teaching")
my_list.append("material")
print(my_list)


# 07
def create_list(num1, num2):
    new_list = []
    for i in range(num1, num2 + 1):
        new_list.append(i)
    return new_list


def sum_of_the_list(numbers):
    total = 0
    for i in numbers:
        total += i
    return total


# 08
def even(num_list):
    for i in num_list:
        if i % 2 == 0:
            print(i)


number_list = create_list(1, 10)
print(number_list)
print(sum_of_the_list(number_list))
even(number_list)

