
from collections import defaultdict as dic

n = int(input())

v = list(map(int, input().split()))
dict1 = dic(int)
dict2 = dic(int)

for i in range(n):
    if i % 2 == 1:
        dict1[v[i]] += 1
    else:
        dict2[v[i]] += 1
    
def search_second_larger(dict):
    if max(dict) == min(dict):
        return 
    largest = max(dict.values())
    ret = min(dict.values())
    for k, v in dict.items():
        if v > ret and v <= largest and k != max(dict):
            ret = v
    return ret


max_1 = max(dict1.values())
second_larger_1 = search_second_larger(dict1)
max_2 = max(dict2.values())
second_larger_2 = search_second_larger(dict2)

if  dict1 == dict2:
    print(n - max_1)
elif max(dict1) == max(dict2):
    print(min(n - max_1 - second_larger_2, n - second_larger_1 - max_2))
else:
    print(n - max_1 - max_2)

"""
if len(dict1) == len(dict2) == 1:
    if len(dict) == 2:
        print(0)
    else:
        print(dict1[v[0]])
else:
    print(n - max(dict1.values()) - max(dict2.values()))
"""