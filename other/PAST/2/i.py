n = int(input())
q = int(input())
a = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = n * i + j - 1

for i in range(n):
    print(a[i])
"""
for i in range(q):
    Q = map(int, input().split())
"""
