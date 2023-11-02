# Return statement = Functions send Python values/objects back to the caller.
# These values/objects are known as the function's return value

def multiply(number1, number2):
    result = number1 * number2
    # return number1 * number2  # Oneline return statement
    return result


x = multiply(8, 5)
print(x)
