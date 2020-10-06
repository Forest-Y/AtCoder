n = int(input())
a, b = [0] * n, [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())
ans = 10 ** 20

def calc_time(s, e, a, b):
    ret = 0
    for i in range(n):
        ret += abs(s - a[i]) + b[i] - a[i] + abs(e - b[i])
    
    return ret
    
for i in range(n):
    start = a[i]
    for j in range(n):
        end = b[j]
        ans = min(ans, calc_time(start, end, a, b))
    
print(ans)