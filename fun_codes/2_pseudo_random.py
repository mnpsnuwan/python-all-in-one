import random

# Rolling dice
dice = random.randint(1, 6)
print(dice)

# Random number
y = random.random()
print(y)

# Random choice
my_list = ['rock', 'paper', 'scissors']
z = random.choice(my_list)
print(z)

# Cards shuffle
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)



