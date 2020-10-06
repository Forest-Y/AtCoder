from bisect import bisect_right
n = int(input())
l = list(map(int, input().split()))

l = sorted(l)
ans = 0
for i in range(n - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        x = l[i] - l[j]
        index = bisect_right(l, x, 0, n)
        #print(l[i], l[j], i, j, index, max(0, i - index - 1))
        print(j - index)
        ans += max(0, j - index)

print(ans)