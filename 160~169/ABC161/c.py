
n, k = map(int, input().split())

if n % k ==  0:
    print(0)
    exit()
if n < k:
    ans = min(n, k - n)
else:
    ans = k - (n % k)

print(ans)


"""
elif n % k == 0:
    ans = 0
"""