# Logical Operators (and, or, not) = Used to check if two or more conditional statements

temp = int(input("What is the temperature outside?: "))

# if temp >= 0 and temp <= 30:
if not(0 <= temp <= 30):  # Same as above
    print("The temperature is bad today")
    print("Stay inside!")
elif not(temp < 0 or temp > 30):
    print("The temperature is good today")
    print("Go outside!")

