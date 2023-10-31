# Dictionary = A changeable, unordered collection of unique key:value pairs
# Fast because they use hashing, allow us to access a value quickly
# In python, the dictionary is similar to hash or maps in other languages.
# It consists of key-value pairs. The value can be accessed by a unique key in the dictionary.

# Create a new dictionary
d = dict()  # or d = {}

# Add a key - value pairs to dictionary
d['xyz'] = 123
d['abc'] = 345

x = type(d)

# print the whole dictionary with type
print(x, ": ", d)

# print only the keys
print(d.keys())

# print only values
print(d.values())

# accessing an element using key
print(d['xyz'])

# accessing a element using get() method
print(d.get('xyz'))

# iterate over dictionary
for i in d:
    print("%s  %d" % (i, d[i]))

# another method of iteration
for index, key in enumerate(d):
    print(index, key, d[key])

# check if key exist
print('xyz' in d)

# delete the key-value pair
del d['xyz']

# check again
print("xyz" in d)

# Time Complexity: O(1)
# Auxiliary Space: O(n)


# -------------------------------------
# Creating a Dictionary
# with dict() method
Dict = dict({1: 'I', 2: 'Matrix', 3: 'Labs'})
print("\nDictionary with the use of dict(): ")
print(Dict)

# --------------------------------------
# Creating a Dictionary
# with each item as a Pair
Dict = dict([(1, 'I'), (2, 'Matrix'), (3, 'Labs')])
print("\nDictionary with each item as a pair: ")
print(Dict)


# ------------------------------------
# Creating a Nested Dictionary
# as shown in the below image
Dict = {1: 'I', 2: 'Matrix',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Labs'}}

print(Dict)

# Accessing element using key of a nested dictionary
print(Dict[3])
print(Dict[3]['A'])
print(Dict[3]['C'])


# --------------------------------------
# Dictionary methods
# dic.clear()	Remove all the elements from the dictionary
# dict.copy()	Returns a copy of the dictionary
# dict.get(key, default = “None”)	 Returns the value of specified key
# dict.items()	 Returns a list containing a tuple for each key value pair
# dict.keys()	 Returns a list containing dictionary’s keys
# dict.update(dict2)	Updates dictionary with specified key-value pairs
# dict.values()	 Returns a list of all the values of dictionary
# pop()	 Remove the element with specified key
# popItem()	Removes the last inserted key-value pair
#  dict.setdefault(key,default= “None”)	set the key to the default value if the key is not specified in the dictionary
# dict.has_key(key)	returns true if the dictionary contains the specified key.
# dict.get(key, default = “None”)	used to get the value specified for the passed key.

# all dictionary methods
dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}

# copy() method
dict2 = dict1.copy()
print(dict2)

# clear() method
dict1.clear()
print(dict1)

# get() method
print(dict2.get(1))

# items() method
print(dict2.items())

# keys() method
print(dict2.keys())

# pop() method
dict2.pop(4)
print(dict2)

# popitem() method
dict2.popitem()
print(dict2)

# update() method
dict2.update({3: "Scala"})
print(dict2)

# values() method
print(dict2.values())

# ---
capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'New York'})

print(capitals)
print(capitals['USA'])
print(capitals.get('Italy'))
print(capitals.values())
print(capitals.keys())
print(capitals.items())
print(capitals.pop('China'))
capitals.clear()

for key, value in capitals.items():
    print(key, value)

