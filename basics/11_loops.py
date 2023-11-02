# while loop = unlimited
# for loop = limited

# While loop = A statement will execute its block of code as long as its condition remains true
# Until a specified criterion is true, a block of statements will be continuously executed

# prints Hello Nuwan 3 Times
count = 0
while count < 3:
    count = count+1
    print("Hello Nuwan")

# ---
first_name = None

while not first_name:
    first_name = input("Enter your first name: ")

print(first_name)

# ---
last_name = ""

while len(last_name) == 0:
    last_name = input("Enter your last name: ")

print(last_name)


# --------------------------------------
# For loop = A statement that will execute its block of code a limited amount of times
# There is a “for in” loop which is similar to for each loop in other languages

for i in range(5):
    print(i)

# ---
for i in range(50, 55+1):  # Range 50 to 56
    print(i)

# ---
for i in range(50, 60, 2):  # Range 50 to 60 count up by 2
    print(i)

# ---
for i in "Nuwan Samarasinghe":
    print(i)

# Iterating over a list
print("List Iteration")
l = ["I", "Matrix", "Labs"]
for i in l:
    print(i)

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("I", "Matrix", "Labs")
for i in t:
    print(i)

# Iterating over a String
print("\nString Iteration")
s = "Matrix"
for i in s:
    print(i)

# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s %d" % (i, d[i]))


# -------------------------------------
# Nested Loops = the "inner loop" will finish all of it's iterations before finishing one iteration of the outer loop
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()

# ---

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use?: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()


