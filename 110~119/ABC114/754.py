
s = input()
ans = abs(753 - int(s[0:3]))
for i in range(1, len(s) - 2):
    ans = min(ans, abs(753 - int(s[i:i + 3])))

print(ans)