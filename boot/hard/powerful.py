import heapq
n, m = map(int, input().split())
a = list(map(lambda x: int(x) * (-1), input().split()))
heapq.heapify(a)

for i in range(m):
    x = heapq.heappop(a)
    heapq.heappush(a, -1 * ((-x) // 2))
print(-sum(a))