
a, b = map(int, input().split())

for i in range(10):
    if b / 0.1 + i == int(a / 0.08):
        print(int(a / 0.08))
        exit()

print(int(-1))