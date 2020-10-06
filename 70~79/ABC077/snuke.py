from bisect import bisect_left, bisect_right

n = int(input())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))
c = sorted(map(int, input().split()))
ans = 0
def bin_search(x, n, flag):
    if flag == True:
        return bisect_left(x, n)
    else:
        return bisect_right(x, n)



for i in range(n):
    ans += bin_search(a, b[i], True) * (n - bin_search(c, b[i], False))

print(ans)