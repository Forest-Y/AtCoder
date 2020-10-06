n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 10 ** 20
for i in range(2 ** n):
    total = 0
    data = a.copy()
    highest = a[0] - 1
    cnt = 0
    for j in range(n):
        if i >> j & 1:
            cnt += 1

    if cnt == k:
        for j in range(n):
            if i >> j & 1:
                if highest >= data[j]:
                    total += highest - data[j] + 1
                    data[j] = max(highest + 1, data[j])
            highest = max(highest, data[j])
        ans = min(ans, total)
        #print(data)
    
print(ans)