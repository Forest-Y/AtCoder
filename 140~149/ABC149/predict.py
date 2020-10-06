from collections import defaultdict
n, k = map(int, input().split())
r, s, p = map(int, input().split())
point = defaultdict(int)
point["r"] = p
point["p"] = s
point["s"] = r
t = input()
ans = 0
hand = [-1] * k
for i in range(n):
    if i < k:
        ans += point[t[i]]
        hand[i] = 1
    elif t[i] != t[i - k] or hand[i % k] != 1:
        ans += point[t[i]]
        hand[i % k] = 1
    elif hand[i % k] == 1:
        hand[i % k] = -1
print(ans)
    