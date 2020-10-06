n = int(input())

xy = [[] * n for _ in range(n)]
for i in range(n):
    a = int(input())
    for j in range(a):
        x, y = map(int, input().split())
        xy[i].append((x, y))

ans = 0
def judge(f):
    for i in range(n):
        if flag[i] == 1:
            for j in xy[i]:
                if f[j[0] - 1] != j[1]:
                    return False
        
    return True

for i in range(2 ** n):
    flag = [0] * n
    for j in range(n):
        if i >> j & 1:
            flag[j] = 1
    if judge(flag):
        ans = max(ans, sum(flag))
print(ans)