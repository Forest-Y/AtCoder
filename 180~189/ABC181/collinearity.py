n = int(input())
x, y = [0] * n, [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            x1, y1 = x[i] - x[k], y[i] - y[k]
            x2, y2 = x[j] - x[k], y[j] - y[k]
            if x1 * y2 == x2 * y1:
                print("Yes")
                exit()
print("No")
