# [동전 1] https://www.acmicpc.net/problem/2293

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
dp = [0] * (k+1)
dp[0] = 1
for _ in range(n):
    i = int(input())
    for j in range(i, k + 1):
        dp[j] += dp[j - i]
print(dp[k])
