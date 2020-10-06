n, a, b = map(int, input().split())
s = input()
total = 0
cnt_b = 0
for i in range(n):
    if s[i] == "c":
        print("No")
    else:
        if total < a + b:
            if s[i] == "a":
                print("Yes")
                total += 1
            elif s[i] == "b" and cnt_b < b:
                print("Yes")
                total += 1
                cnt_b += 1
            else:
                print("No")
        else:
            print("No")


