# [약] https://www.acmicpc.net/problem/23560

n = int(input())
m = 3 * n
dp = [[0] * m for _ in range(m)]
for i in range(m):
    dp[i][i] = 0 if i%3 == 1 else 1
for k in range(1, m):
    for i in range(m-k):
        if (k%3 == 1) - ((i+k)%3 == 1) == 0:
            dp[i][i+k] += dp[i][i+k-1]
    for j in range(k, m):
        if (k%3 == 1) - ((j-k)%3 == 1) == 0:
            dp[j-k][j] += dp[j-k+1][j]
print(dp[0][-1])

# From above, can also find the pattern: 2 * 3^(n-1)
n = int(input())
print(2 * 3 ** (n-1))
