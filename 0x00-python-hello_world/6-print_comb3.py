#!/usr/bin/python3
b = 0
c = 0
for b in range(0, 10):
    c = b + 1
    for c in range(c, 10):
        if (b != 8 or c != 9):
            print("{:0d}{:0d}".format(b, c), end=", ")
        else:
            print("{}{}".format(b, c))
