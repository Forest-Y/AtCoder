
n = int(input())
ans = 0

def count_div(i):
    ret = 0
    for j in range(1, i + 1):
        if i % j == 0:
            ret += 1
    
    return ret

for i in range(1, n + 1):
    if i % 2 == 1:
        cnt = count_div(i)
        if cnt == 8:
            ans += 1

print(ans)