
n, k = map(int, input().split())

h = [0] * n
for i in range(n):
    h[i] = int(input())

h.sort()
ans = h[k - 1] - h[0]
for i in range(n - (k - 1)):
    if h[i + k - 1] - h[i] < ans:
        ans = h[i + k - 1] - h[i]
        
    if ans == 0:
        break

print(ans)
