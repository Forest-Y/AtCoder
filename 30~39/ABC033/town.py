n = int(input())
s, p = [0] * n, [0] * n
for i in range(n):
    s[i], p[i] = input().split()
    p[i] = int(p[i])

total = sum(p)
ans = "atcoder"
for i in range(n):
    if p[i] > total / 2:
        ans = s[i]
        break
print(ans)