nums = list(int(input()) for _ in range(3))
data = sorted(nums)
for i in range(3):
    print(3 - data.index(nums[i]))
