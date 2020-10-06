n = int(input())
total = 0

for i in range(1, 10):
    for j in range(1, 10):
        total += i * j

for i in range(1, 10):
    for j in range(1, 10):
        if i * j == total - n:
            print(i, "x", j)