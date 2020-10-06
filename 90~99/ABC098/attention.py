n = int(input())
s = input()
e_cnt = 0
for i in range(n):
    if s[i] == "E":
        e_cnt += 1
ans = e_cnt
w_cnt = 0
for i in range(n):
    if s[i] == "E":
        e_cnt -= 1
        
    ans = min(w_cnt + e_cnt, ans)
    if s[i] == "W":
        w_cnt += 1

print(ans)


