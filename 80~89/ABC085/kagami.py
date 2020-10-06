from collections import defaultdict

n = int(input())
dic = defaultdict(int)

for i in range(n):
    dic[int(input())] += 1

print(len(dic))