# [피보나치 함수] https://www.acmicpc.net/problem/1003

import sys
input = sys.stdin.readline
t = int(input())
dp = [[1, 0], [0, 1]]
def fib(num):
    m = len(dp)
    if num >= m:
        for i in range(m, num+1):
            dp.append([dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]])
    print(*dp[num])
for _ in range(t):
    fib(int(input()))
