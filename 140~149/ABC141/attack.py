
n, k, q = map(int, input().split())
score = [k] * n
data = [0] * n

for i in range(q):
    a = int(input())
    data[a - 1] += 1

for i in range(n):
    if(q - data[i] >= k):
        print("No")
    else:
        print("Yes")
    
