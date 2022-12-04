decrement = 0
for i in range(-122, -96):
    if abs(i) % 2 == 0:
        decrement = 0
    else:
        decrement = 32
    print(chr(abs(i) - decrement), end="")
