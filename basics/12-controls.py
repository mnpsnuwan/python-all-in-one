# Loop Control Statements = Change a loops execution from its normal sequence.
# break = Used to terminate the loop entirely
# continue = Skips to the next iteration of the loop
# pass = Does nothing, act as a place order

# Continue, it returns the control to the beginning of the loop.
# Prints all letters except 't' and 'x'
for letter in 'imatrixlabs':
    if letter == 't' or letter == 'x':
        continue
    print('Current Letter :', letter)

# ---
phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

# -------------------------------------
# Break, it brings control out of the loop.
for letter in 'imatrixlabs':

    # break the loop as soon it sees 't' or 'x'
    if letter == 't' or letter == 'x':
        break
print('Current Letter :', letter)

# ---
while True:
    name = input("Enter your name?: ")
    if name != "":
        break

# -----------------------------------
# Pass, statements to write empty loops. Pass is also used for empty control statements, functions, and classes.
# An empty loop
for letter in 'imatrixlabs':
    pass
print('Last Letter :', letter)

# ---
for i in range(1, 11):
    if i == 6:
        pass
    else:
        print(i)

