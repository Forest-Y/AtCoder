from bisect import bisect_left

n, q = map(int, input().split())
a = list(map(int, input().split()))
cnt = [0] * n
for i in range(n):
  cnt[i] = a[i] - (i + 1)
print(cnt)
for i in range(q):
  k = int(input())

  if k > cnt[-1]:
    print(a[-1] + k - cnt[-1])
    continue

  r = bisect_left(cnt, k)

  print(a[r] - 1 - cnt[r] + k)
