# List = Used to store multiple items in a single variable
# Lists are one of the most powerful data structures in python. Lists are sequenced data types.

# Declaring a list
l = [1, "a", "string", 1+2]
x = type(l)

# Print list with type
print(x, ": ", l)

# Displaying Second element of the list
print(l[1])

l[0] = 5
for x in l:
    print(x)

# Adding an element in the list
l.append(6)
print(l)

# Remove specific element
l.remove("a")
print(l)

# Deleting last element from a list
l.pop()
print(l)

# Insert element
l.insert(0, 10)
print(l)

# Sort the list
food = ["ice cream", "cake", "pizza", "apple", "pudding"]
food.sort()  # Cannot use under the mixed element (Ex- int, str, float)
print(food)

# Clear all the elements
food.clear()
print(food)

# ------------------------------------
# 2D lists = A list of lists

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hotdog", "hamburger"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

print(food)
print(food[0])  # first list
print(food[0][1])  # second element of first list

