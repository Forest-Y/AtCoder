
n = int(input())
a = list(map(int, input().split()))
"""
before = sort(a[:n // 2], reversed = True)
after = sort(a[-(-n // 2)], reversed = True)
"""
ans = 0
for i in range(n):

