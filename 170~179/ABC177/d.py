from collections import deque
n, m = map(int, input().split())
data = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    data[a].append(b)
    data[b].append(a)

def bfs(data):
    flag = [0] * n
    ans = 1
    for i in range(n):
        if flag[i]:
            continue
        queue = deque()
        queue.append(i)
        cnt = 1
        while queue:
            x = queue.popleft()
            flag[x] = 1
            for j in data[x]:
                if flag[j]:
                    continue
                flag[j] = 1
                cnt += 1
                queue.append(j)
        ans = max(ans, cnt)
    return ans

print(bfs(data))