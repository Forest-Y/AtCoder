from collections import deque
n, m = map(int, input().split())
data = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int,input().split())
    data[a - 1].append(b - 1)
    data[b - 1].append(a - 1)

ans = [0] * (n - 1)

def bfs(i, queue, p):
    while len(queue) > 0:
        x = queue.popleft()
        pre = p.popleft()
        for j in range(len(x)):
            if ans[x[j] - 1] == 0 and x[j] != 0:
                ans[x[j] - 1] = pre + 1
                queue.append(data[x[j]])
                p.append(x[j])

queue = deque()
pre = deque()
pre.append(0)
queue.append(data[0])
bfs(0, queue, pre)

if 0 not in ans:
    print("Yes")
    for i in range(len(ans)):
        print(ans[i])
else:
    print("No")