# [가장 긴 감소하는 부분 수열] https://www.acmicpc.net/problem/11722

import sys
input = sys.stdin.readline
n = int(input())
s = [*map(int, input().split())]
dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if s[i] < s[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
