from collections import defaultdict

data = defaultdict()
cnt = defaultdict(int)
for i in range(3):
    s = input()
    data[chr(ord("a") + i)] = s

turn = "a"
while 1:
    cnt[turn] += 1
    if cnt[turn] > len(data[turn]):
        ans = ord(turn) - (ord("a") - ord("A"))
        break
    turn = data[turn][cnt[turn] - 1]
print(chr(ans))