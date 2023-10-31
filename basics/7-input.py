# Taking input from the user
name = input("Enter your name: ")

# Output
print("Hello, " + name)
print(type(name))

# ------------------------------
# Taking input from the user as integer/Float
num = int(input("Enter a number: "))
height = float(input("Enter your height in cm: "))

num = num + 1

# Output
print("Entered number is ", num)
print("Entered number is (using str) " + str(num))
print("You are " + str(height) + " cm")

# -------------------------------
# Taking multiple inputs of the same data type at a time
a, b, c = map(int, input("Enter the Numbers(3) : ").split())
print("The Numbers are : ")
print(a, b, c)

# --------------------------------
# Taking List/Set elements one by one
my_list = list()
my_set = set()
input_list = int(input("Enter the size of the List : "))
input_set = int(input("Enter the size of the Set  : "))
print("Enter the List elements : ")
for i in range(0, input_list):
    my_list.append(int(input()))
print("Enter the Set elements : ")
for i in range(0, input_set):
    my_set.add(int(input()))
print(my_list)
print(my_set)

# -----------------------------------
# Using map() and list() / set() Methods
my_list = list(map(int, input("Enter List elements : ").split()))
my_set = set(map(int, input("Enter the Set elements :").split()))
print(my_list)
print(my_set)

# ------------------------------------
# Taking Input for Tuple
tup = (2, 3, 4, 5, 6)
print("Tuple before adding new element")
print(tup)
my_list = list(tup)
my_list.append(int(input("Enter the new element : ")))
tup = tuple(my_list)
print("Tuple After adding the new element")
print(tup)


