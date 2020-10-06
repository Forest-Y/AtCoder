from collections import defaultdict

s = input()
k = int(input())
pins = defaultdict(int)
for i in range(len(s) - k + 1):
    pins[s[i: i + k]] += 1

print(len(pins))
