n = int(input())
a = list(map(int, input().split()))
ans = 0
h = a[0]
for i in range(1, n):
    if h > a[i]:
        ans += h - a[i]
    else:
        h = a[i]
    
print(ans)