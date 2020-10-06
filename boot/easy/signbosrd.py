s = "CODEFESTIVAL2016"
S = input()
ans = 0
for i in range(len(s)):
    if s[i] != S[i]:
        ans += 1
print(ans)