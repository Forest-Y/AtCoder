n, t = map(int, input().split())
a = [0] * n
for i in range(n):
    a[i] = int(input())

ans = 0
i = 0
while i < n:
    start = a[i]
    time = 0
    pre = a[i]
    while  i != n and pre + t >= a[i]:
        time = a[i] - start
        pre = a[i]
        i += 1
    
    ans += time + t
print(ans)