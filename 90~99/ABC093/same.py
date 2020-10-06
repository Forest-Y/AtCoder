
abc = list(map(int, input().split()))

abc.sort()
print(abc)
def calc(a, b):
    if (a + b) % 2 == 0:
        return (b - a) // 2
    else:
        return -(-(b - a) // 2) + 1


print(calc(abc[0], abc[1]) + (abc[2] - abc[1]))