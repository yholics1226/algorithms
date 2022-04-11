# [RGB거리 2] https://www.acmicpc.net/problem/17404

import sys
input = sys.stdin.readline
n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
ans = float('inf')
for k in range(3):
    dp = [[float('inf')] * 3 for _ in range(n)]
    dp[0][k] = arr[0][k]
    for i in range(1, n):
        for j in range(3):
            dp[i][j] = arr[i][j] + min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])
    ans = min(ans, dp[-1][(k+1)%3], dp[-1][(k+2)%3])
print(ans)
