n, a, b, c, d = map(int, input().split())
s = input()
flag1, flag2 = False, False
if d > c:
    flag = "##" not in s[b: d] and "##" not in s[a: c]
else:
    flag = "..." in s[b - 2: d + 1]

print("Yes" if flag else "No")