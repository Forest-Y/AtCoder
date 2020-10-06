from bisect import bisect_left
n, m = map(int, input().split())
a = list(map(int, input().split()))
p = [0] * n
ans = [-1] * m
n_min = 10 ** 9
e = 0
for i in range(m):
    """
    if a[i] < n_min:
        ans[i] = e + 1
        if e < n:
           p[e] = a[i]
           e += 1
    else:
    """
    index = bisect_left(p, a[i], 0, n)
    if index != 0:
       p[index - 1] = a[i]
    ans[i] =  n - (index - 1)
    #print(n_min)
    #print(p)
    
for i in range(m):
    #print(p[i])
    print(ans[i] if ans[i] <= n else -1)