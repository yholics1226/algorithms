# [2*N 타일링] https://www.acmicpc.net/problem/11726

import sys
n = int(sys.stdin.readline())
if n == 1:
    print(1)
    sys.exit(0)
else:
    dp = [1] * n
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n-1] % 10007)
