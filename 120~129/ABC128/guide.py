

n = int(input())

data = []
for i in range(n):
    s, p = input().split()
    data.append([s, -1 * int(p), i + 1])



data.sort(key = lambda x: x[1])
data.sort(key = lambda x: x[0])

for i in data:
    print(i[2])