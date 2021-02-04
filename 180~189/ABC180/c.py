n = int(input())
data = []

for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        data.append(i)
        data.append(n // i)

data = sorted(set(data))
for i in range(len(data)):
    print(data[i])