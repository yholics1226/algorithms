# [RGB거리] https://www.acmicpc.net/problem/1149

import sys
input = sys.stdin.readline
n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
dp[0] = arr[0]
for i in range(1, n):
    for j in range(3):
        dp[i][j] = arr[i][j] + min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])
print(min(dp[-1]))
