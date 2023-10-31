# Taking input from the user
name = input("Enter your name: ")

# Output
print("Hello, " + name)
print(type(name))

# ------------------------------
# Taking input from the user as integer
num = int(input("Enter a number: "))

add = num + 1

# Output
print(add)

# -------------------------------
# Taking multiple inputs of the same data type at a time
a, b, c = map(int, input("Enter the Numbers : ").split())
print("The Numbers are : ")
print(a, b, c)

# --------------------------------
# Taking List/Set elements one by one
List = list()
Set = set()
iList = int(input("Enter the size of the List : "))
iSet = int(input("Enter the size of the Set  : "))
print("Enter the List elements : ")
for i in range(0, iList):
    List.append(int(input()))
print("Enter the Set elements : ")
for i in range(0, iSet):
    Set.add(int(input()))
print(List)
print(Set)

# -----------------------------------
# Using map() and list() / set() Methods
List = list(map(int, input("Enter List elements : ").split()))
Set = set(map(int, input("Enter the Set elements :").split()))
print(List)
print(Set)

# ------------------------------------
# Taking Input for Tuple
T = (2, 3, 4, 5, 6)
print("Tuple before adding new element")
print(T)
L = list(T)
L.append(int(input("Enter the new element : ")))
T = tuple(L)
print("Tuple After adding the new element")
print(T)


