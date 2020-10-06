
N, T = map(int, input().split())

c = [0] * N
t = [0] * N
for i in range(N):
    c[i], t[i] = map(int, input().split())

if(min(t) > T):
    print("TLE")
    exit()
else:
    ans = 1000
    for i in range(N):
        if t[i] <= T:
            ans = min(ans, c[i])

print(ans)