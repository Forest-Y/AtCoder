import itertools
n = int(input())

p = list(map(int, input().split()))
q = list(map(int, input().split()))
nums = []
for i in range(n):
    nums.append(i + 1)
p_index, q_index = 0, 0
data = itertools.permutations(nums)
index = 0
for i in data:
    
    if list(i) == p:
        p_index = index
    if list(i) == q:
        q_index = index
    index += 1
    
print(abs(p_index - q_index))