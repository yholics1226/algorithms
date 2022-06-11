# [가장 긴 증가하는 부분 수열 2] https://www.acmicpc.net/problem/12015

import sys, bisect
input = sys.stdin.readline
n = int(input())
a = [*map(int, input().split())]
dp = [a[0]]
for i in range(n):
    if a[i] > dp[-1]:
        dp.append(a[i])
    else:
        k = bisect.bisect_left(dp, a[i])
        dp[k] = a[i]
print(len(dp))
