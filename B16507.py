# [어두운 건 무서워] https://www.acmicpc.net/problem/16507

import sys
input = sys.stdin.readline
r, c, q = map(int, input().split())
img = [[*map(int, input().split())] for _ in range(r)]
dp = [[0] * (c+1) for _ in range(r+1)]
for i in range(1, r+1):
    for j in range(1, c+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + img[i-1][j-1]
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    s = dp[r2][c2] - dp[r1-1][c2] - dp[r2][c1-1] + dp[r1-1][c1-1]
    n = (r2-r1+1) * (c2-c1+1)
    print(s // n)
