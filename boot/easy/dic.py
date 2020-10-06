n = int(input())
data = []
for i in range(n):
    s = input()
    data.append(s[::-1])

data = sorted(data)
for i in range(n):
    data[i] = data[i][::-1]
    print(data[i])