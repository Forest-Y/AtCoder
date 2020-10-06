from bisect import bisect_left, bisect_right
n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
c = sorted(list(map(int, input().split())))
ans = 0
for i in range(n):
    a_cnt = bisect_left(a, b[i], 0, n)
    c_cnt = n - bisect_right(c, b[i], 0, n)
    #print(a_cnt, c_cnt)
    ans += a_cnt * c_cnt

print(ans)