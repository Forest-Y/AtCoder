n = int(input())
a = list(map(int, input().split()))
flag = [[False, True] for _ in range(n)]
print(flag)
ans = 0
for i in range(n):
    j = 0
    cnt = 0
    while j < a[i]:
        j += 1
        if j % 2 == 1:
            flag[i][0] = True
        else:
            flag[i][0] = False
        
        if j % 3 == 0:
            flag[i][1] = True
        elif j % 3 == 2:
            flag[i][1] = False
        if flag[i][0] and flag[i][1]:
            cnt = a[i] - j
    ans += cnt
print(ans)