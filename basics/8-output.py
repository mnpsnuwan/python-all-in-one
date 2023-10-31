# print() method
print("ABC")

# code for disabling the softspace feature
print('A', 'B', 'C')

# -------------------------------------
# Print output with custom sep and end parameter
print("ABC", end="@")

# code for disabling the softspace feature
print('A', 'B', 'C', sep="#")

# -------------------------------------
# Python String formatting using F string
# Declaring a variable
name = "Abc"

# Output
print(f'Hello {name}! How are you?')

# --------------------------------------
# Using format() function to format our output to make it look presentable.
# Initializing variables
a = 20
b = 10

# addition
addition = a + b

# subtraction
sub = a - b

# Output
print('The value of a is {} and b is {}'.format(a, b))
print('{2} is the sum of {0} and {1}'.format(a, b, addition))
print('{sub_value} is the subtraction of {value_a} and {value_b}'.format(value_a=a, value_b=b, sub_value=sub))

# -------------------------------------
#  Using ‘%’ operator. % values are replaced with zero or more value of elements.
# Taking input from the user
num = int(input("Enter a value: "))
add = num + 5

# Output
print("The sum is %d" % add)

