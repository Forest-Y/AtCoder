from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))
queue = deque()
for i in range(n):
    if i <= k - 1:
        queue.append(a[i])
    elif i >= k:
        x = queue.popleft()
        if x < a[i]:
            print("Yes")
        else:
            print("No")
        queue.append(a[i])
