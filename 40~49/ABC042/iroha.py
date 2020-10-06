from collections import defaultdict

n, k = map(int, input().split())
d = list(map(int, input().split()))
nums = defaultdict(int)
for i in range(len(d)):
    nums[d[i]] += 1

def judge(n, nums):
    n = str(n)
    for i in range(len(n)):
        if nums[int(n[i])] == 1:
            return False
        
    return True

while 1:
    if judge(n, nums) == True:
        print(n)
        exit()
    n += 1
