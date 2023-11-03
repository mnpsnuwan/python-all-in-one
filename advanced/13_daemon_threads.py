# daemon threads = A thread that runs in the background, not important for program to run
# Your program will not wait for daemon threads to complete before existing
# non-daemon threads cannot normally be killed, stay alive until task is complete
#
# Ex: background tasks, garbage collections, waiting for input, long-running processes

import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for ", count, "seconds")


x = threading.Thread(target=timer, daemon=True)  # Function will stop immediately with the input
x.start()

print(x.__getattribute__("daemon"))

answer = input("Do you wish to exit? ")

