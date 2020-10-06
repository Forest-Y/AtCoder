
n, k = input().split()
s = list(input())
k = int(k)
s[k - 1] = s[k - 1].lower()

print("".join(s))