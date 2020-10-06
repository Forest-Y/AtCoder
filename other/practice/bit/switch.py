n, m = map(int, input().split())

s = [list(map(int, input().split())) for _ in range(m)]
k = [0] * m
for i in range(m):
    k[i] = s[i][0]
    del s[i][0]
p = list(map(int,input().split()))
ans = 0
for b in range(2 ** n):
    sum = 0
    cnt = [0] * m 
    flag = [False] * m
    for j in range(n):
        if b >> j & 1:
            for k in range(m):
                if (j + 1) in s[k]:
                    cnt[k] += 1
    #print(cnt, b)
    for i in range(m):
        if cnt[i] % 2 == p[i]:
            flag[i] = True
    
    if all(flag[i] == True for i in range(m)):
        """
        print(b)
        print(flag)
        """
        ans += 1
print(ans)