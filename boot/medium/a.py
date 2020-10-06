s = list(input())
data = [0] * (len(s) + 1)
for i in range(len(s)):
    if s[i] == "<":
        data[i + 1] = data[i] + 1

for i in range(len(s) - 1, -1, -1):
    if s[i] == ">":
        data[i] = max(data[i], data[i + 1] + 1) 
print(data)
print(sum(data))