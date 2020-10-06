s = input()
ans = 0
color = s[0]
for i in range(1, len(s)):
    if color != s[i]:
       color = s[i]
       ans += 1
    
print(ans)