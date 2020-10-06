from collections import deque
n, q = map(int, input().split())
queue = [deque() for _ in range(n)] 
for i in range(n):
    queue[i].append(i + 1)

for i in range(q):
    f, t, x = map(int, input().split())
    temp = deque()
    while x not in temp:
        temp.append(queue[f - 1].pop())
    while len(temp) > 0:
        queue.append()
    print(queue)

for i in range(n):
    for j in range(n):
        if i + 1 in queue[j]:
            print(j + 1)
            break 
