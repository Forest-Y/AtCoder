from math import sqrt

x = int(input())

for i in range(-int(sqrt(sqrt(x))), int(sqrt(sqrt(x))) + 1):
    for j in range(-int(sqrt(sqrt(x))), int(sqrt(sqrt(x))) + 1):
        if i ** 5 - j ** 5 == x:
            print(i, j)
            exit()
