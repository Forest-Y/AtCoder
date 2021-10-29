from math import ceil

n = int(input())
a = list(map(int, input().split()))
cnt = [[0 * (2 * 10 ** 5)] for _ in range(2 * 10 ** 5)]
