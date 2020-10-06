s = input()
ans = 0
for i in range(len(s)):
    if s[i] == "U":
        ans += i
    else:
        ans += max(0, len(s) - i - 1)
    ans += len(s) - 1
print(ans)