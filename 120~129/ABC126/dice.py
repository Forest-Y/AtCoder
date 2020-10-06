
n, k = map(int, input().split())

ans = 0
for i in range(1, n + 1):
    cnt = 0
    if i >= k:
        ans += 1 / n
    else:
        j = i
        while j < k:
            j *= 2
            cnt += 1
        
        ans += 1 / n * 0.5 ** cnt
    

print(ans)