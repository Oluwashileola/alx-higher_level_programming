#!/usr/bin/python3
# Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase

ecrement = 0
for i in range(-122, -96):
    if abs(i) % 2 == 0:
        decrement = 0
    else:
        decrement = 32
    print("{}".format(chr(abs(i) - decrement)), end="")
