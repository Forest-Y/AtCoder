from collections import defaultdict

n, m = map(int, input().split())
x, y = [0] * m, [0] * m
ans = 1

for i in range(m):
    x[i], y[i] = map(int, input().split())

for i in range(2 ** n):
    mem = []
    flag = True
    for j in range(n):
        if i >> j & 1:
            mem.append(j + 1)
    cnt = 0
    for j in range(len(mem) + 1):
        for k in range(j + 1, len(mem)):
            for l in range(m):
                if min(mem[j], mem[k]) == x[l] and max(mem[j], mem[k]) == y[l]:
                    cnt += 1
                    break
    
    if cnt == len(mem) * (len(mem) - 1) // 2:
        #print(mem)
        ans = max(ans, len(mem))

print(ans)