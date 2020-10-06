nums = list(map(int, input().split()))
print("YES" if nums.count(5) == 2 and nums.count(7) == 1 else "NO")