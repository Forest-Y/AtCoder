
k = int(input())
i = 1
cnt = 9

if k <= 12:
    print(k)
    exit()

def judge(s):
    s_list = list(s)
    
    for i in range(len(s) - 1):
        if abs(int(s_list[i]) - int(s_list[i + 1])) > 1:
            return False
    return True

while cnt <= k:
    cnt += 3 ** i * 8 + 
    i += 1

print(cnt)