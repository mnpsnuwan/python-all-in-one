# Thread = A flow of execution. Like a separate order of instructions
# However each thread takes a turn running to achieve concurrency
# GIL = (Global Interpreter Lock)
# Allows only one thread to hold the control of the Python interpreter

# cpu bound = Program/task spends most of it's time waiting for internal events (CPU intensive)
# Use multiprocessing

# io bound = Program/task spends most of it's time waiting for external events (user input, web scripting)
# Use multithreading

import threading
import time

print(threading.active_count())
print(threading.enumerate())  # Print all the list of threads


# ---
def eat_breakfast():
    time.sleep(2)
    print("You eat breakfast!")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee!")


def study():
    time.sleep(5)
    print("You finished study!")


eat_breakfast()
drink_coffee()
study()

print(threading.active_count())
print(threading.enumerate())


# ---
x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

# x.join()
# y.join()
# z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())


