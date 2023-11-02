# Exception = Events detected during execution that interrupt the flow of program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers")
except Exception as e:
    print(e)
    print("Something went wrong :(")
else:
    print(round(result, 2))
finally:
    print("This will always execute")

