n, l = map(int, input().split())
x = list(map(int, input().split()))
t1, t2, t3 = map(int, input().split())
now = 0
ans = 0
i = 0
while now < l:
    if i != n - 1 and x[i] - now < 4:
        if now + 4 < x[i + 1]:
            calc_time(now, 3)
        else:
            calc_time(now, 2)
    elif now + 