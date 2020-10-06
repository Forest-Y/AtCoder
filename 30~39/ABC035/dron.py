from collections import defaultdict

s = input()
t = int(input())
cnt = defaultdict(int)

for i in range(len(s)):
    cnt[s[i]] += 1
#print(cnt)
dis = abs(cnt["U"] - cnt["D"]) + abs(cnt["L"] - cnt["R"])
print(dis + cnt["?"] if t == 1 else max(dis - cnt["?"], (dis - cnt["?"]) % 2))