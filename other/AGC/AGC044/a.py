t = int(input())

def judge(num, x):
    i = 1
    while x ** i < num:
        i += 1
    if abs(num - x ** i) > abs(num - x ** (i - 1)):
        return i - 1
    else:
        return i

for i in range(t):
    ans = 0
    num = 0
    n, a, b, c, d = map(int, input().split())
    ans += min(a, b, c) * d
    num += min(a, b, c) * d
    multi_5 = judge(num, 5)
    mulit_3 = judge(num, 3)
    multi_2 = judge(num, 2)
    total_5 = multi_5
    print(num)
