# If statement = a block of code that will execute if it's condition is true

# Python program to illustrate selection statement

num1 = 34
if num1 > 12:
    print("Num1 is good")
elif num1 > 35:
    print("Num2 is not good")
else:
    print("Num2 is great")

# -------------------------------
age = int(input("How old are you?: "))

if age == 100:  # This line should be on top, otherwise it will not execute
    print("You are a century old!")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child!")
