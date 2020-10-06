n = int(input())
ans = str(n // 3600).zfill(2) + ":" + str(n % 3600 // 60).zfill(2) + ":" + str(n % 3600 % 60).zfill(2)
print(ans)