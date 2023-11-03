# sort() method = Used with lists
# sort() function = Used with iterables

students = ["Saman", "Amal", "Sunil", "Nimal", "Sarath", "Asanka"]
students_tup = ("Saman", "Amal", "Sunil", "Nimal", "Sarath", "Asanka")

students.sort()
# students.sort(reverse=True)

sorted_students_tup = sorted(students_tup)
# sorted_students_tup = sorted(students_tup, reverse=True)

for i in students:
    print(i)
print("======================")

for i in sorted_students_tup:
    print(i)
print("======================")

# ---
grad_students = [("Saman", "F", 60),
                 ("Amal", "A", 33),
                 ("Sunil", "D", 36),
                 ("Nimal", "B", 20),
                 ("Sarath", "C", 78),
                 ("Asanka", "E", 55)]

grad_students_tup = (("Saman", "F", 60),
                     ("Amal", "A", 33),
                     ("Sunil", "D", 36),
                     ("Nimal", "B", 20),
                     ("Sarath", "C", 78),
                     ("Asanka", "E", 55))

grade = lambda grades: grades[1]
grad_students.sort(key=grade, reverse=True)

age = lambda ages: ages[2]
grad_students.sort(key=age)
# grad_students.sort(key=age, reverse=True)
sorted_grad_students_tup = sorted(grad_students_tup, key=age)

for i in grad_students:
    print(i)







