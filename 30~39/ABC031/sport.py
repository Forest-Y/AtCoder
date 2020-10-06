l, h = map(int, input().split())
n = int(input())
data = []
for i in range(n):
    t = int(input())
    data.append(t)

for i in range(n):
    if data[i] < l:
        print(l - data[i])
    elif data[i] > h:
        print(-1)
    else:
        print(0)