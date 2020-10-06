n = int(input())

C, S, F = [0] * n, [0] * n, [0] * n

for i in range(n - 1):
    C[i], S[i], F[i] = map(int, input().split())

for i in range(n):
    time = 0
    for j in range(i, n - 1):
        if time < S[j]:
            time = S[j] + C[j]
        elif time % F[j] == 0:
            time += C[j]
        else:
            time = time + F[j] - (time % F[j]) + C[j]
    print(time)
    
