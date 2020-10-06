from bisect import bisect_left

n, m = map(int, input().split())
x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_s = 0
b_s = 0
ans = 0
while a_s <= a[-1]:
    a_index = bisect_left(a, a_s, 0, n)
    if a_index == n:
        break

    b_s = a[a_index] + x
    b_index = bisect_left(b, b_s, 0, m)
    if b_index == m:
        break
    a_s = b[b_index] + y
    ans += 1

print(ans)