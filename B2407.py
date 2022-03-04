# [조합] https://www.acmicpc.net/problem/2407

def comb(n, r):
    if dp[n][r] > 0:
        return dp[n][r]
    if n == r or r == 0:
        return 1
    else:
        dp[n][r] = comb(n-1, r-1) + comb(n-1, r)
        return dp[n][r]
n, m = map(int, input().split())
dp = [[0] * (n+1) for _ in range(n+1)]
print(comb(n, m))

# another solution
from math import factorial as fact
n, m = map(int, input().split())
print(fact(n) // fact(n-m) // fact(m))

# comb() in math module
import math
print(math.comb(*map(int, input().split())))
