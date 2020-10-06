n = int(input())
a = list(map(int, input().split()))
ans = -10 ** 5
a_score = -10 ** 5
def calc(data, flag):
    ret = 0
    for i in range(len(data)):
        if i % 2 == flag:
            ret += data[i]
    
    return ret
for i in range(n):
    a_score = -10 ** 5
    x = -10 ** 5
    for j in range(n):
        data = a[min(i, j): max(i, j) + 1]
        if i == j:
            continue
        score = calc(data, 1)
        if i == n - 1:
            #print(data)
        if a_score < score:
            x = calc(data, 0)
            a_score = score
    ans = max(ans, x)
print(ans)