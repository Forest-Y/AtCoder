t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
b_index = 0
flags = [False] * m
for i in range(n):
    if a[i] <= b[b_index] <= a[i] + t:
        flags[b_index] = True
        b_index += 1
    if b_index == m:
        break
print("yes" if False not in flags else "no")