h = [2, 4, 5, 7, 9]
p = [0, 1, 6, 8]
b = [3]
n = int(input())
if n % 10 in h:
    print("hon")
elif n % 10 in p:
    print("pon")
else:
    print("bon")