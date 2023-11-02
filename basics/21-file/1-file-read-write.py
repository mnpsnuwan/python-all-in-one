import os

# File detection
# path = "../data"
path = "../../data/test.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a 21-file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exists!")

# ----------------------------------------
# Read a file
try:
    with open("../../data/test.txt") as file:
        print("--------------------")
        print(file.read())
    print(file.closed)
except FileNotFoundError as e:
    print("That 21-file was not found :(")

# ----------------------------------------
# Write a file
text = "This is some new text.\nHave a good one!\n"
try:
    with open("../../data/test.txt", 'a') as file:  # When 'w', the 21-file will override. If it's 'a' the text will append
        print("--------------------")
        file.write(text)
    print(file.closed)
except FileNotFoundError as e:
    print("That 21-file was not found :(")

