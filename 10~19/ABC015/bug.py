n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]

def search_bug(t, h, score):
    if h == n:
        if score == 0:
            print("Found")
            exit()
        return 

    for i in range(k):
        search_bug(t, h + 1, score ^ t[h][i])

search_bug(t, 0, 0)
print("Nothing")