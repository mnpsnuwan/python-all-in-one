# zip(*iterables) = Aggregate elements from two or more iterables (list, tuple, set, etc)
# Create a zip object with paired elements stored in tuples for each element


usernames = ["Nuwan", "Saman", "Gayan"]
passwords = ("p@ssword", "abc@123", "guest@123")
login_date = ["11/03/2023", "11/02/2023", "11/02/2023"]

users = zip(usernames, passwords)
print(type(users))

users_list = list(zip(usernames, passwords, login_date))
print(type(users_list))

for i in users_list:
    print(i)
print("=============================")

users_dict = dict(zip(usernames, passwords))
print(type(users_dict))

for key, value in users_dict.items():
    print(key, ":", value)
print("=============================")



