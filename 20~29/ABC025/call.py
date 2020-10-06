s = input()
n = int(input())
data = []
for i in list(s):
    for j in list(s):
        data.append(i + j)

print(data[n - 1])