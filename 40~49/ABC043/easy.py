s = input()
ans = []

for i in range(len(s)):
    if s[i] == "0" or s[i] == "1":
        ans.append(s[i])
    elif s[i] == "B" and ans != []:
        del ans[len(ans) - 1]
    
print("".join(ans))