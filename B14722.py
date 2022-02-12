# [우유 도시] https://www.acmicpc.net/problem/14722

import sys
input = sys.stdin.readline
n = int(input())
grid = [[*map(int, input().split())] for _ in range(n)]
dp = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        if dp[i][j] % 3 == grid[i-1][j-1]:
            dp[i][j] += 1
print(dp[n][n])
