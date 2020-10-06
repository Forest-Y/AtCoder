from collections import defaultdict

w = input()
cnt = defaultdict(int)

for i in range(len(w)):
    cnt[w[i]] += 1

for k, v in cnt.items():
    if v % 2 == 1:
        print("No")
        exit()

print("Yes")