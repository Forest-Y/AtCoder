
s = input()
if len(s) == 1:
    if s == "a":
        print(-1)
    else:
        print(chr(ord(s) - 1))
else:
    print(s[:len(s) - 1])