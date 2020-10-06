from collections import defaultdict
n = int(input())
vote = defaultdict(int)
for i in range(n):
    s = input()
    vote[s] += 1
    
max_vote = max(vote.values())
for k, v in vote.items():
    if v == max_vote:
        print(k)
        exit()