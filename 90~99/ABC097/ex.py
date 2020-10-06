from math import sqrt
x = int(input())

ans = 1
i = 1
for i in range(2, int(sqrt(x)) + 1):
    j = i
    while j <= x:
        j *= i
    
    ans = max(ans, j // i)

print(ans)