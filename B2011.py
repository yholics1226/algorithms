# [암호코드] https://www.acmicpc.net/problem/2011

import sys
s = sys.stdin.readline().strip()
if s[0] == '0':
    print(0)
    sys.exit(0)
else:
    n = len(s)
    dp = [0] * (n+1)
    dp[0] = dp[1] = 1
    for i in range(1, n):
        if s[i] != '0':
            dp[i+1] += dp[i]
        if s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
            dp[i+1] += dp[i-1]
    print(dp[-1] % 1000000)
