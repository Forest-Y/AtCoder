n = int(input())
a = list(map(int, input().split()))
b = 0
for i in range(n):
    b ^= a[i]

print("Yes" if b == 0 else "No")
