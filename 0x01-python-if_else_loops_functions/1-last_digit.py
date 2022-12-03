#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
num = number
last = abs(num) % 10
if last == 0:
    print(f"Last digit of {num} is {last} and is 0")
elif last > 5:
    if num < 0:
        print(f"Last digit of {num} is {-last} and is less than 6 and not 0")
    else:
        print(f"Last digit of {num} is {last} and is greater than 5")
elif (last < 6) and (last != 0):
    if num < 0:
        print(f"Last digit of {num} is {-last} and is less than 6 and not 0")
    else:
        print(f"Last digit of {num} is {last} and is greater than 5")
