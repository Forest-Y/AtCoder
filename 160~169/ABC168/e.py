from collections import defaultdict
multi_a = defaultdict(int)
multi_b = defaultdict(int)
n = int(input())
A, B = defaultdict(int), defaultdict(int)
a, b = [0] * n, [0] * n
for i in range(n):
    a, b = map(int, input().split())
    A[a] += 1
    B[b] += 1
