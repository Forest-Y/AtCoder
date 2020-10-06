e = list(map(int, input().split()))
b = int(input())
l = list(map(int, input().split()))
flag = False
cnt = 0
for i in range(6):
    if l[i] in e:
        cnt += 1
    elif l[i] == b:
        flag = True
ans = 0
if cnt == 3:
    ans = 5
elif cnt == 4:
    ans = 4
elif cnt == 5:
    ans = 2 if flag else 3
elif cnt == 6:
    ans = 1

print(ans)
