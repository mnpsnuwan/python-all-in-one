# Walrus operator :=

# new to python 3.8
# assignment expression aka walrus operator
# assign values to variables as part of a large expression

happy = True
print(happy)

# print(happy = True)  # cannot assign as this
print(happy := True)  # When we use walrus happy is always True

# ---
# The below example is without Walrus Operator
foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)
print(foods)

# Below Approach uses Walrus Operator
foods1 = list()
while food := (input("What food do you like?: ")) != "quit":
    foods1.append(food)  # appending True into list
print(foods1)

# ---
sample_data = [
    {"userId": 1, "name": "rahul", "completed": False},
    {"userId": 1, "name": "rohit", "completed": False},
    {"userId": 1, "name": "ram", "completed": False},
    {"userId": 1, "name": "ravan", "completed": True}
]

print("Without Walrus operator:")
for entry in sample_data:
    name = entry.get("name")
    if name:
        print(f'Found name: "{name}"')

print("With Python 3.8 Walrus Operator:")
for entry in sample_data:
    if name := entry.get("name"):
        print(f'Found name: "{name}"')
