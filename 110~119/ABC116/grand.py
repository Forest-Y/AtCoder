n = int(input())

h = list(map(int, input().split()))

cnt = 0
ans = 0
low = 0
for i in range(n):
    if cnt < h[i]:
        cnt = h[i]
    elif cnt > h[i]:
        ans += cnt - low
        low = h[i]
        cnt = h[i]
    

ans += cnt - low
print(ans)