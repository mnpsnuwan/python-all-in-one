# reduce() = Apply a function to an iterable and reduce it to a single cumulative value.
# Performs function on first two elements and process until one value remains
#
# reduce(function, iterable)
import functools

letters = ["H", "E", "L", "L", "O", "W", "O", "R", "L", "D"]

concat = lambda x, y: x + y

word = functools.reduce(concat, letters)

print(word)

# How to work
# ["H", "E", "L", "L", "O", "W", "O", "R", "L", "D"]
# ["HE", "L", "L", "O", "W", "O", "R", "L", "D"]
# ["HEL", "L", "O", "W", "O", "R", "L", "D"]
# ["HELL", "O", "W", "O", "R", "L", "D"]

# ---
factorial = [9, 8, 7, 6, 5, 4, 3, 2, 1]

result = functools.reduce(lambda x, y: x * y, factorial)

print(result)
