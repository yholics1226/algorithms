# [방 번호] https://www.acmicpc.net/problem/1082

import sys
input = sys.stdin.readline
n = int(input())
p = [*map(int, input().split())]
m = int(input())
dp = [0] * (m+1)
for i in range(1, m+1):
    for j in range(n):
        if p[j] <= i:
            dp[i] = max(dp[i], dp[i-p[j]] * 10 + j)
print(dp[m])
