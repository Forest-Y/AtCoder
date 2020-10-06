from collections import defaultdict

n = int(input())
s = input()

ans = 0
for i in range(n):
    dic = defaultdict(int)
    for j in range(i):
        for k in range(i, n):
            if s[j] == s[k]:
                dic[s[j]] += 1
                break
    ans = max(ans, len(dic))
    
print(ans)