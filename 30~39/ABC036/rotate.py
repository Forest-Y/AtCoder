n = int(input())
s = [input() for _ in range(n)]

for i in range(n):
    for j in range(n - 1, -1, -1):
        print(s[j][i], end = "")
    print()
