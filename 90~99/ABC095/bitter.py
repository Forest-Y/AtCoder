n, x = map(int, input().split())

m = []
for i in range(n):
    a = int(input())
    m.append(a)
    
print(n + (x - sum(m)) // min(m))