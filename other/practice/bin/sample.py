from bisect import bisect_left

data = [1, 5, 12, 17, 24]
x = int(input())
print(bisect_left(data, x, 0, 5))