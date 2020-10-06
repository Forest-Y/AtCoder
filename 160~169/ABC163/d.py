n, k = map(int, input().split())
ans = 0
max = 0
min = 0
for i in range(0, k):
    min += i
    max += n - i
for i in range(k, n + 2):
    #print(ans, max, min, i)
    ans = (ans + max - min + 1) % (10 ** 9 + 7)
    max += n - i
    min += i

print(ans)