s = input()
i = 0
ans = 0
atcg = "ACGT"
for i in range(len(s)):
    for j in range(i, len(s)):
        t = s[i: j + 1]
        cnt = 0
        for n in range(4):
            cnt += t.count(atcg[n])
        
        if cnt == len(t):
            ans = max(ans, cnt)
        
    
print(ans)