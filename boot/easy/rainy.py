s = input()
ans = 1 if "R" in s else 0
for i in range(1, 3):
    if s[i] == s[i - 1] == "R":
        ans += 1

print(ans)