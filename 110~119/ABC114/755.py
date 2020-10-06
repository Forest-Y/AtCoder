from collections import defaultdict as dic

n = int(input())

data = [0] * 10000000
ans = 0

def judge_753(s):
    judge = 1
    flag = dic(int)
    for i in range(len(s)):
        if s[i] != '7' and s[i] != '5' and s[i] != '3':
            judge = 0
            break
        else:
            flag[int(s[i])] = 1

    if flag[3] != 1 or flag[5] != 1 or flag[7] != 1:
        judge = 0
    return judge

def search_num(num):
    ret = 0
    if num > n:
        return 0
    
    if judge_753(str(num)) == 1:
        ret += 1
    
    ret += search_num(num * 10 + 3) + search_num(num * 10 + 5) + search_num(num * 10 + 7)
    return ret


print(search_num(0))