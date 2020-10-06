n = int(input())
a = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))
for i in range(q):
    flag = False
    for b in range(2 ** n):
        sum = 0
        for j in range(n):
            if b >> j & 1:
                sum += a[j]
        
        if sum == m[i]:
            flag = True
            break
    
    print("yes" if flag else "no")

