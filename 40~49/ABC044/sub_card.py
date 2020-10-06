
n, a = map(int, input().split())
x = list(map(int, input().split()))
ans = 0
for i in range(1, 2 ** n):
    sum = 0
    cnt = 0
    for j in range(n):
        if i >> j & 1:
            sum += x[j]
            cnt += 1
    
    if sum / cnt == a:
        ans += 1

print(ans)
