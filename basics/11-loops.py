# While loop, until a specified criterion is true, a block of statements will be continuously executed
# prints Hello Nuwan 3 Times
from __future__ import print_function

count = 0
while count < 3:
    count = count+1
    print("Hello Nuwan")


# --------------------------------------
# For loop, there is a “for in” loop which is similar to for each loop in other languages
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
# Nested Loops
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()


