n = int(input())
cnt = 0
m = 100
while m < n:
    m = int(m * 1.01)
    cnt += 1
print(cnt)