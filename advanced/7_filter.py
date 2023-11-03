# filter() = Creates a collection of elements from an iterable for which a  function returns true
#
# filter(function, iterable)

friends = [("Sunil", 20),
           ("Nimal", 21),
           ("Amal", 16),
           ("Kamal", 17),
           ("Anura", 22),
           ("Aruna", 18)]

age = lambda data: data[1] >= 18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)




