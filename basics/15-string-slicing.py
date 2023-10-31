# Slicing = Create a substring by extracting elements from another string
#   indexing[] or slice()
#   [start:stop:step]

name = "Nuwan Samarasinghe"

first_name = name[:5]  # Same as first_name = name[0:5]
last_name = name[6:]  # Same as last_name = name[6:18]
# funky_name = name[0:18:2], by step 2 showing every 2 character from the beginning
funky_name = name[::2]  # Same as above
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

# ----------------------------------------
website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice_website = slice(7, -4)  # -4 is getting from the ending position, starting with -1

print(website1[slice_website])
print(website2[slice_website])

