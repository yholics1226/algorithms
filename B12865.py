# [평범한 배낭] https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
wv = [[*map(int, input().split())] for _ in range(n)]
dp = [0] * (k+1)
for w, v in wv:
    for i in range(k, w-1, -1):
        dp[i] = max(dp[i], dp[i-w] + v)
print(dp[k])

# another solution (faster)
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
wv = sorted([[*map(int, input().split())] for _ in range(n)], reverse=True)
d = {0: 0}
for w, v in wv:
    tmp = {}
    for dv, dw in d.items():
        if d.get(v + dv, k+1) > w + dw:
            tmp[v + dv] = w + dw
    d.update(tmp)
print(max(d))
