# A Set in Python programming is an unordered, un-indexed collection data type that is iterable,
# mutable and has no duplicate elements.
# Set are represented by { } (values enclosed in curly braces)
# The major advantage of using a set, as opposed to a list,
# is that it has a highly optimized method for checking whether a specific element is contained in the set.
# This is based on a data structure known as a hash table.
# Since sets are unordered, we cannot access items using indexes as we do in lists.

# Define a set and its elements
mySet = {"xyz", "abc", "xyz", "def"}
x = type(mySet)

# As set doesn't have duplicate elements so, 1 xyz will not be printed
print(x, " : ", mySet)

# ---
utensils = {"spoon", "knife", "fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup"}

utensils.add("napkin")  # Add element
utensils.remove("fork")  # Remove element

utensils.update(dishes)
dinner_table = utensils.union(dishes)

utensils.clear()

print(dinner_table.difference(dishes))  # Different element of the dinner_table will print
print(dishes.difference(dinner_table))  # Different element of the dishes will print
print(dinner_table.intersection(dishes))  # Same element of the dinner_table will print

for x in utensils:
    print(x)

for x in dinner_table:
    print(x)


