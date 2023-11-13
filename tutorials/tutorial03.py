import math


# 01
def interests(amount):
    if 0 < amount <= 1000:
        return amount * 4/100
    elif 1000 < amount <= 5000:
        return amount * 4.5/100
    elif amount > 5000:
        return amount * 5 / 100
    else:
        return 0


input_amount = float(input("Enter deposit amount?: "))
print("The interest for " + str(input_amount) + " of deposit is", interests(input_amount))


# 02
def existing_roots(a, b, c):

    det = b**2 - 4*a*c

    if det == 0:
        root = round(-b/2*a, 2)
        print("One root:", str(root))

    elif det > 0:
        root1 = round((-b+math.sqrt(det))/2*a, 2)
        root2 = round((-b-math.sqrt(det))/2*a, 2)
        print("Two roots:", str(root1), "and", str(root2))

    else:
        print("No roots")


print("The quadratic formula...")
A = int(input("Enter 'a' for quadratic formula?: "))
B = int(input("Enter 'b' for quadratic formula?: "))
C = int(input("Enter 'c' for quadratic formula?: "))
existing_roots(A, B, C)


