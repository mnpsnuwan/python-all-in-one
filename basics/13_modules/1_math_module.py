# Math module, very rich module library
import math


def main():
    num = -85

    # fabs is used to get the absolute
    # value of a decimal
    num = math.fabs(num)
    print(num)


if __name__ == "__main__":
    main()

x = 1
y = 2
z = 3
pi = 3.14
negative_pi = -3.14

print(round(pi))
print(math.ceil(pi))  # rounding to up number
print(math.floor(pi))
print(abs(negative_pi))  # absolute number
print(pow(pi, 2))  # power of the number
print(math.sqrt(pi))  # sqrt is not working on negative
print(max(x, y, z, pi, negative_pi))
print(min(x, y, z, pi, negative_pi))
