n, m, k = map(int, input().split())
friend = [[] for _ in range(n)]
block = [[] for _ in range(n)]
flag = [0] * n
def set_data(n, data):
    for i in range(n):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        data[a].append(b)
        data[b].append(a)

set_data(m, friend)
set_data(k, block)
print(friend)
print(block)
data = []
for i in range(n):
    data.append(friend[i] + block[i])
ans = [[] for _ in range(n)]
for i in range(n):
    if i + 1 in friend[i] and i + 1 not in block[i]:
        flag[i] = 1

def judge_flag(flag, i, j):
    for k in range(i, j):
        if flag[k] == 0:
            return False
    
    return True

print(flag)

for i in range(n):
    for j in range(len(friend[i])):
        for k in range(len(friend[friend[i][j]])):
            if friend[friend[i][j]][k] not in friend[i] and friend[friend[i][j]][k] != i:
                ans[i].append(friend[friend[i][j]][k])
    
for i in range(n):
    print(len(set(ans[i])), set(ans[i]), end = " ")
print()