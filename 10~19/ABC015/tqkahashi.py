n = int(input())
a = list(map(int, input().split()))
cnt = 0
sum = 0
for i in range(n):
    if a[i] != 0:
        sum += a[i]
        cnt += 1
print(-(-sum // cnt))