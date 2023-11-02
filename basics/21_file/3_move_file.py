import os

source = "../../data/test.txt"
destination = "../../data/new/test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved to " + destination)
except FileNotFoundError as e:
    print(e)
    print(source + " was not found")
