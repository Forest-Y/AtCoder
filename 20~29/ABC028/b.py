from collections import defaultdict

s = input()
dic = defaultdict(int)

str = "ABCDEF"

for i in range(len(s)):
    dic[s[i]] += 1

for i in range(len(str)):
    if i != len(str) - 1:
        print(dic[str[i]], end = " ")
    else:
        print(dic[str[i]])

