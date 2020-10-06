
n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
sum = 0

for i in range(len(a)):
    sum += b[a[i] - 1]
    print("i:{0} sum{1}".format(i, sum))
    if(i != len(a) - 1 and a[i] + 1 == a[i + 1]):
        sum += c[a[i] - 1]
        #print("i:{0} sum{1}".format(i, sum))#

print(sum)