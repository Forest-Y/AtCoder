from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
nums = defaultdict(int)
for i in range(n):
    nums[a[i]] = i + 1

data = sorted(a, reverse = True)
for i in range(n):
    print(nums[data[i]])
