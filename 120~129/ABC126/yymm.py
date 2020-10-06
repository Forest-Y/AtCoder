
s = input()
s1 = int(s[:2])
s2 = int(s[2:4])

if s1 == 0 and s2 == 0:
    print("NA")
    exit()

if (s1 >= 13 or s1 <= 0) and (s2 >= 13 or s2 <= 0):
    print("NA")
elif s1 <= 12 and s1 >= 1 and s2 <= 12 and s2 >= 1:
    print("AMBIGUOUS")
elif s2 >= 13 or s2 == 0:
    print("MMYY")
else:
    print("YYMM")
    