s = input().split("+")
ans = len(s)
for i in range(len(s)):
    if "0" in s[i]:
        ans -= 1
print(ans)