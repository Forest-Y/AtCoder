
n = int(input())
b = list(map(int,input().split()))

sum = b[n - 2] + b[0]
for i in range(1, n - 1):
    #print("{0}:{1}".format(i, sum))#
    sum += min(b[i - 1], b[i])

print(sum)