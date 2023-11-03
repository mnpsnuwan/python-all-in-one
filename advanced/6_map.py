# map() = Applies a function to each item in an iterable (list, tuple, etc)
#
# map(function, iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jackets", 50.00),
         ("socks", 10.00)]

to_euros = lambda data: (data[0], round(data[1]*0.94, 2))  # () to represent tuple
to_dollars = lambda data: (data[0], round(data[1]/.94, 2))  # () to represent tuple

store_euros = list(map(to_euros, store))
store_dollars = list(map(to_dollars, store))

for i in store_euros:
    print(i)
print("=====================")

for i in store_dollars:
    print(i)
print("======================")



