n, l = map(int, input().split())
s = [""] * n
ans = ""
for i in range(n):
    s[i] = input()
s = sorted(s)
for i in range(n):
    ans += s[i]
print(ans)