from collections import deque
k = int(input())

queue = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in range(k):
    x = queue.popleft()
    if x % 10 != 0:
        queue.append(10 * x + (x % 10) - 1)
    queue.append(10 * x + x % 10)
    if x % 10 != 9:
        queue.append(10 * x + x % 10 + 1)
#print(queue)
print(x)
