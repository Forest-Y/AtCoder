
n = int(input())
h, s = [0] * n, [0] * n
for i in range(n):
    h[i], s[i] = map(int, input().split())

low = min(h)
high = max(h) + max(s) * (n - 1)
#mid = (low + high) // 2
#print(h)
while low + 1< high:
    mid = (low + high) // 2
    flag = True
    limit = [0] * n
    #print(low, high, mid)
    for i in range(n):
        limit[i] = -(-(mid - h[i]) // s[i])
    limit.sort()
    #print(limit)
    for i in range(n):
        if limit[i] <= i:
            flag = False
        
    if flag:
        high = mid
    else:
        low = mid
print(low)