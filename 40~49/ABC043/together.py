import numpy as np
n = int(input())
a = list(map(int, input().split()))
"""
def sign(n):
    if n < 0:
        return -1
    else:
        return 1
"""
mean = int(sum(a) / n + np.sign(sum(a)) * 0.5)
#print(mean)
ans = 0
for i in range(n):
    ans += (a[i] - mean) ** 2

print(ans)