n = int(input())
s = input()

ans = 0
cnt = 0
for i in range(n):
    if s[i] == "I":
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt -= 1
    
print(ans)
