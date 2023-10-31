# A Set in Python programming is an unordered collection data type that is iterable,
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


