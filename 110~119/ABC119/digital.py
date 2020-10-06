
N = int(input())

sum = 0
for i in range(N):
    x, u = input().split()
    if u == "JPY":
        sum += int(x)
    else:
        sum += float(x) * 380000
    

print(sum)