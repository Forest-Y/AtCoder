from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
cnt = defaultdict(int)

def div_2(num):
    while num % 2 == 0:
        num //= 2
    return num

for i in range(n):
    cnt[div_2(a[i])] += 1
print(len(cnt))
