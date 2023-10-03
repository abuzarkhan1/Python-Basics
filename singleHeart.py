size = 6

heart = "♥"
for i in range(size):
    for j in range(size*2):
        if (i >= size // 2 and (i + j) % (size//2) == 0) or (i < size // 2 and (j - i) % (size//2) == 0):
            print(heart, end="")
        else:
            print(" ", end="")
    print()
