from math import sqrt, factorial
n = int(input())
x, y = [0] *  n, [0] * n

for i in range(n):
    x[i], y[i] = map(int, input().split())

total = 0
for i in range(n):
    for j in range(i + 1, n):
        #print(sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2))
        total += 2 * sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)

print(total / n)