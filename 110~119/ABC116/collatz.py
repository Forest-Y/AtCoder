
from collections import defaultdict as dic
s = int(input())

flag = dic(int)
flag[s - 1] = 1
def f(n, i):
    if flag[n - 1] == 1:
        print(i)
        exit()
    else:
        flag[n - 1] = 1
        if n % 2 == 1:
            f(3 * n + 1, i + 1)
        else:
            f(int(n / 2), i + 1)
        

if s % 2 == 1:
    f(3 * s + 1, 2)
else:
    f(int(s / 2), 2)
