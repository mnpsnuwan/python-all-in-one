# Continue, it returns the control to the beginning of the loop.
# Prints all letters except 't' and 'x'
for letter in 'imatrixlabs':
    if letter == 't' or letter == 'x':
        continue
    print('Current Letter :', letter)


# -------------------------------------
# Break, it brings control out of the loop.
for letter in 'imatrixlabs':

    # break the loop as soon it sees 't' or 'x'
    if letter == 't' or letter == 'x':
        break
print('Current Letter :', letter)


# -----------------------------------
# Pass, statements to write empty loops. Pass is also used for empty control statements, functions, and classes.
# An empty loop
for letter in 'imatrixlabs':
    pass
print('Last Letter :', letter)

