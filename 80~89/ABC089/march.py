from collections import defaultdict
march = "MARCH"
n = int(input())
dic = defaultdict(int)
for i in range(n):
    s = input()
    for j in range(5):
        if s[0] == march[j]:
            dic[march[j]] += 1
            break
        

ans = 0
for i in range(5):
    if dic[march[i]] >= 1:
        for j in range(i + 1, 5):
            if dic[march[j]] >= 1:
                for k in range(j + 1, 5):
                    if dic[march[k]] >= 1:
                        ans += dic[march[i]] * dic[march[j]] * dic[march[k]]


print(ans)