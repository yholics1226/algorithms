# [LCS 2] https://www.acmicpc.net/problem/9252

import sys
input = sys.stdin.readline
s1 = input().rstrip()
s2 = input().rstrip()
n, m = len(s1), len(s2)
dp = [[''] * (m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        if s1[i] == s2[j]:
            dp[i+1][j+1] = dp[i][j] + s1[i]
        else:
            if len(dp[i][j+1]) > len(dp[i+1][j]):
                dp[i+1][j+1] = dp[i][j+1]
            else:
                dp[i+1][j+1] = dp[i+1][j]
if dp[n][m]:
    print(len(dp[n][m]))
    print(dp[n][m])
else:
    print(0)

# another solution (faster)
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
ans = []
while n > 0 and m > 0:
    if dp[n-1][m] == dp[n][m]:
        n -= 1
    elif dp[n][m-1] == dp[n][m]:
        m -= 1
    else:
        ans.append(s1[n-1])
        n -= 1
        m -= 1
print(''.join(ans[::-1]))
