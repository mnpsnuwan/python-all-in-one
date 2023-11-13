# 01
def student_result(exam, special):
    if exam > 50:
        if special > 50:
            print("MERIT PASS!")
        else:
            print("PASS!")
    else:
        print("FAIL!")


student_result(80, 60)
student_result(60, 50)
student_result(50, 50)


# 02
def check_numbers(x, y):
    if x > 0 and y > 0:
        print("Both are positive!")
    elif x < 0 and y < 0:
        print("Both are negative!")
    elif x < 0 or y < 0:
        print("One number is negative!")


check_numbers(3, 1)
check_numbers(-1, -4)
check_numbers(8, -2)


