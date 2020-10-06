
n, m = map(int, input().split())

num = [0] * n
flag = 1
if m == 0 and n == 1:
    print(0)
    exit()
num[0] = 1
for i in range(m):
    s, c = map(int, input().split())
    if num[s - 1] == 0 or (s - 1 == 0 and num[0] == 1):
        num[s - 1] = c
    else:
        if num[s - 1] != c:
            flag = 0
    
if flag == 0 or (n != 1 and num[0] == 0):
    print(-1)
else:
    for i in range(n):
        print(num[i], end="")