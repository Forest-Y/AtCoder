n = int(input())
x = list(map(int, input().split()))

for i in range(n):
    x[i] = abs(x[i])


def euclid(x):
    res = 0
    for i in x:
        res += i ** 2
    return res ** 0.5
print(sum(x))
print(euclid(x))
print(max(x))