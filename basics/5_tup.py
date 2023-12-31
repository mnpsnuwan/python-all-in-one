# Tuple = Collection which is ordered and unchangeable used to group together related data.
# A tuple is a sequence of immutable Python objects.
# Tuples are just like lists with the exception that tuples cannot be changed once declared.
# Tuples are usually faster than lists.

# Declaring a tup
tup = (1, "a", "string", 1+2)
x = type(tup)

# Print tuple with type
print(x, ": ", tup)
print(tup[1])

# ---
student = ("Nuwan", 30, "male")
print(student.count("Nuwan"))
print(student.index("male"))

if "Nuwan" in student:
    print("Nuwan is here!")
