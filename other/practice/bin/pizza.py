from bisect import bisect_left
d = int(input())
n = int(input())
m = int(input())
shop = [0] * (n - 1)
goal = [0] * m
for i in range(n - 1):
    shop[i] = int(input())

for i in range(m):
    goal[i] = int(input())

shop.sort()
ans = 0
#print(shop)
#print(goal)
for i in range(m):
    index = bisect_left(shop, goal[i], 0, n - 1)
    if index == 0:
        ans += min(goal[i], shop[index] - goal[i])
    elif index == n - 1:
        ans += min(d - goal[i], goal[i] - shop[index - 1])
    else:
        #print(i, index)
        #print(goal[i] - shop[index - 1])
        #print(shop[index] -goal[i])
        ans += min(goal[i] - shop[index - 1], shop[index] -goal[i])

print(ans)