from collections import defaultdict 

n = int(input())
dic = defaultdict(int)
s = [""] * n
flag = True
for i in range(n):
    s[i] = input()
    if i != 0:
        if s[i - 1][len(s[i - 1]) - 1] != s[i][0]:
            flag = False
    
    if dic[s[i]] != 0:
        flag = False
    dic[s[i]] += 1
print("Yes" if flag == True else "No")