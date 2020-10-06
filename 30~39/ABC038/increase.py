from math import factorial
n = int(input())
a = list(map(int, input().split()))

ans = n
i = 0
while i < n:
    j = 0
    if i != n - 1 and a[i] < a[i + 1]:
        while i + j != n - 1 and a[i + j] < a[i + j + 1]:
            j += 1
    ans += (j + 1) * j // 2
    i += j + 1

print(ans)