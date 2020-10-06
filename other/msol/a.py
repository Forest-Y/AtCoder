n = int(input())
if n >= 1800:
    ans = 1
elif n >= 1600:
    ans = 2
elif n >= 1400:
    ans = 3
elif n >= 1200:
    ans = 4
elif n >= 1000:
    ans = 5
elif n >= 800:
    ans = 6
elif n >= 600:
    ans = 7
else:
    ans = 8
print(ans)