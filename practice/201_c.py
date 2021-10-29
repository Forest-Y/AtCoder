s = input()

if s.count("o") >= 5:
  print(0)
  exit()
nums = []
for i in range(len(s)):
  if s[i] == "o":
    nums.append(i) 

ans = 0
for i in range(10000):
  num = str(i).zfill(4)
  flag = [0] * 10
  cnt = 0
  
  for x in nums:
    if str(x) in num:
      cnt += num.count(str(x))
      flag[x] = 1
  if sum(flag) < len(nums):
    continue

  for x in num:
    if int(x) not in nums and s[int(x)] == "?":
      cnt += 1
  
  if cnt == 4:
    ans += 1

print(ans)