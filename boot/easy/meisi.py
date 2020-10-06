n, m, a, b = map(int, input().split())
for i in range(m):
    if n <= a:
        n += b
    c = int(input())
    n -= c
    if n < 0:
        ans = i + 1
        break

print("complete" if n >= 0 else ans)
    
