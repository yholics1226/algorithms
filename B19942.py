# [다이어트] https://www.acmicpc.net/problem/19942

from itertools import combinations
import sys
input = sys.stdin.readline
n = int(input())
mp, mf, ms, mv = map(int, input().split())
board = [[]] + [[*map(int, input().split())] for _ in range(n)]
cost = float('inf')
nums = []
for i in range(1, n+1):
    for comb in combinations(range(1, n+1), i):
        p = f = s = v = c = 0
        for x in comb:
            p += board[x][0]
            f += board[x][1]
            s += board[x][2]
            v += board[x][3]
            c += board[x][4]
        if p >= mp and f >= mf and s >= ms and v >= mv:
            if cost > c:
                cost = c
                nums = comb
            elif cost == c:
                nums = sorted((nums, comb))[0]
if cost == float('inf'):
    print(-1)
else:
    print(cost)
    print(*nums)
