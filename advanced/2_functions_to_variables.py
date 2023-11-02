def hello():
    print("Hello")

    say = print  # assign print function into say variable
    say("Whoa! I can't believe this works! :O")


# print(hello)
hi = hello
hello()
hi()

