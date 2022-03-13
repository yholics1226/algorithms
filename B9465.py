# [스티커] https://www.acmicpc.net/problem/9465

import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    pts = [[*map(int, input().split())] for _ in range(2)]
    dp = [[0] * (n+1) for _ in range(2)]
    for j in range(n):
        for i in range(2):
            dp[i][j+1] = max(dp[i][j], dp[1-i][j] + pts[i][j])
    print(max(dp[0][n], dp[1][n]))

# another solution (faster)
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0, 0]
    r1 = [*map(int, input().split())]
    r2 = [*map(int, input().split())]
    for i in range(n):
        dp = [max(dp[0], dp[1] + r1[i]), max(dp[1], dp[0] + r2[i])]
    print(max(dp))
