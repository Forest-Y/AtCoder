import copy
n = int(input())

a = list(map(int, input().split()))
"""
a = [100000000] * n
"""
data1 = [0] * n
for i in range(n):
    data1[i] = data1[i - 1] + a[i]
data2 = copy.copy(data1)
for i in range(1, n):
    data2[i] += data2[i - 1]
index = 1
total = data2[0]
"""
print(data1)
print(data2)
"""
for i in range(n):
    if total < data2[i]:
        total = data2[i]
        index = i
cnt = 0
"""
print(index)
print(data1[:index])
print(total)
"""
ans = total
if index != n - 1:
    ans = max(ans, ans + max(data1[:index]))
print(max(0, ans))