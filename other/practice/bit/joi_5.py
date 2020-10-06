import numpy as np
r, c = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(r)]
ans = 0
for i in range(2 ** r):
    data_c = data.copy()
    for j in range(r):
        if i >> j & 1:
            data_c[j] ^= 1
    
    reversed_cnt = data_c.sum(axis = 0)
    print(reversed_cnt)
    total = np.maximum(reversed_cnt, r - reversed_cnt)
    ans = max(ans, sum(total))
print(ans)