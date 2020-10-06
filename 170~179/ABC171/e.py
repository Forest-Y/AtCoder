n = int(input())
a = list(map(int, input().split()))
bit = a[0]
for i in range(1, n):
    bit ^= a[i]
    
for i in range(n):
    print(bit ^ a[i], end = " ")