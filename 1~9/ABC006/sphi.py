n, m = map(int, input().split())

for i in range(2):
    for j in range(n - i + 1):
        k = n - (i + j)
        if i * 3 + j * 2 + k * 4 == m:
            print(j, i, k)
            exit()

print(-1, -1, -1)