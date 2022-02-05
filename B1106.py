# [호텔] https://www.acmicpc.net/problem/1106

import sys
input = sys.stdin.readline
c, n = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]
arr.sort(key = lambda x: x[0])
dp = [float('inf')] * (c+100)
dp[0] = 0
for cost, num in arr:
    for i in range(num, c+100):
        dp[i] = min(dp[i], dp[i-num] + cost)
print(min(dp[c:]))
