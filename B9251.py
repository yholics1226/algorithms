# [LCS] https://www.acmicpc.net/problem/9251

import sys
input = sys.stdin.readline
s1 = input().rstrip()
s2 = input().rstrip()
n, m = len(s1), len(s2)
dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        dp[i+1][j+1] = dp[i][j] + 1 if s1[i] == s2[j] else max(dp[i][j+1], dp[i+1][j])
print(dp[n][m])

# another solution (faster)
import sys
input = sys.stdin.readline
a = input().rstrip()
b = input().rstrip()
c = [0] * len(b)
for x in a:
    cnt = 0
    for i in range(len(b)):
        if cnt < c[i]:
            cnt = c[i]
        elif x == b[i]:
            c[i] = cnt + 1
print(max(c))
