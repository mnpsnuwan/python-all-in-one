# list comprehension = A way to create a new list with less syntax
# Can mimic certain lambda functions, easier to read
#
# list = [expression for item in iterable]
# list = [expression for item in iterable if statement]
# list = [expression (if/else) for item in iterable]

squares = []  # Create an empty list
for i in range(1, 11):  # Create a for loop
    squares.append(i * i)  # Define what each loop iteration should do
print(squares)

squares_list = [i * i for i in range(1, 11)]
print(squares_list)

# ---
students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

passed_students = list(filter(lambda x: x >= 60, students))
print(passed_students)

passed_students_list = [x for x in students if x >= 60]
passed_students_list_new = [x if x >= 60 else "FAILED" for x in students]
print(passed_students_list)
print(passed_students_list_new)
