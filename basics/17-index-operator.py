# Index operator [] = Gives access to a sequence's element (str, list, tuples)

name = "nuwan Samarasinghe!"
first_name = name[:5].upper()
last_name = name[6:18].lower()
last_character = name[-1]

if name[0].islower():
    name = name.capitalize()
print(name)

print(first_name)
print(last_name)
print(last_character)
