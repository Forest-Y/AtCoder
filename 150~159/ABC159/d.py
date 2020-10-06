from collections import defaultdict, Counter

n = int(input())
a = list(map(int, input().split()))
ans = [0] * n
dic = defaultdict(int)
for i in range(n):
    dic[a[i]] += 1

sum = 0
for v in dic.values():
    sum += v * (v - 1) / 2
    
for i in range(n):
    print(int(sum - (dic[a[i]] - 1)))